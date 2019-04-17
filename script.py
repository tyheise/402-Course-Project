import os
import sys
import getpass
import re
from github import Github
from datetime import datetime

def searchRepos(maxNumOfRepos):
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)

    repos = git.search_repositories('stars:>5000 language:Java', sort='stars', order='desc')

    f = open("reposConsidered.txt", "w")
    i=0
    while(i<maxNumOfRepos):
        try:
            repoName = ((repos[i].full_name).split("/"))[1]
            file_contents = repos[i].get_file_contents('pom.xml')
            f.write(repos[i].full_name +"\n")
            i+=1
        except:
            print("skipping " + repoName+ " because not a maven proj")
            i+=1

    f.close()
    return

def getReleaseCSVs():
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)
    reposFile = open("reposConsidered.txt", "r")

    non_decimal = re.compile(r'[^\d.]+')

    line = reposFile.readline().strip()
    while(line):
        repo = get_repo(line, git)
        releases = repo.get_releases()

        releaseCount = releases.totalCount

        if releaseCount > 1:
            repoName = ((repo.full_name).split("/"))[1]

            releaseDict = {}

            # prevDate = None
            print("Getting major releases from", repoName)
            for i in range(releaseCount - 1):
                currRelease = releases[i]
                #prevRelease = releases[i+1]

                tagName  = currRelease.tag_name
                tagName = non_decimal.sub('', tagName)

                lst  = tagName.split(".")
                tagName = float(lst[0] + "." + lst[1][0])

                if tagName not in releaseDict:
                    releaseDict[tagName] = currRelease
                else:
                    if releaseDict[tagName].published_at > currRelease.published_at:
                        releaseDict[tagName] = currRelease

            relTups = releaseDict.items()
            relTups = sorted(relTups, key=lambda x: x[0])

            tupLen = len(relTups)

            if tupLen > 1:

                releaseDates = open("releaseCSVs/"+repoName+".csv", "w")
                releaseDates.write("repo,id,tag_name,until,since,dayDifference\n")

                for i in range(1,tupLen):
                    prevReleaseTup = relTups[i-1]
                    currReleaseTup = relTups[i]

                    prevRelease = prevReleaseTup[1]
                    currRelease = currReleaseTup[1]

                    currCreatedAt = currRelease.published_at
                    prevCreatedAt = prevRelease.published_at

                    dayDifference = currCreatedAt - prevCreatedAt

                    if prevCreatedAt < currCreatedAt:
                        releaseDates.write(repo.full_name+','+str(currRelease.id)+","+str(currReleaseTup[0])+","+str(currCreatedAt)+","+str(prevCreatedAt)+","+str(dayDifference)+"\n")
            else:
                print("Skipping", repoName, "because it only has one major release")
        line = reposFile.readline().strip()

    reposFile.close()

def getCommits():
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)

    csvFolder = os.path.join(os.path.curdir, "releaseCSVs")
    fileList = os.listdir(csvFolder)

    for fileName in fileList:
        if fileName != '.gitignore':
            csvPath = os.path.join(csvFolder, fileName)
            csv = open(csvPath)

            lines = csv.readlines()
            try:
                repoName = (lines[1].split(","))[0]
                print("Now getting commits from", repoName)
                repo = git.get_repo(repoName)

                repoName2 = (repoName.split("/"))[1]

                for i in range(1,len(lines)-1):
                    line = lines[i].split(",")

                    # 2019-03-26 15:08:13
                    until = datetime.strptime(line[3], '%Y-%m-%d %H:%M:%S')
                    since = datetime.strptime(line[4], '%Y-%m-%d %H:%M:%S')

                    commits = repo.get_commits(until=until, since=since)
                    if commits.totalCount > 0:
                        repoFile = open(os.path.join(os.path.curdir,'commits',repoName2+".csv"), 'a+')
                        repoFile.write(line[1]+","+line[2]+","+commits[0].sha+","+str(until-since)+"\n")
                        repoFile.close()
                    else:
                        print("Skipping release", line[2], "because there are no commits between" ,str(since), "and", str(until))

            except IndexError:
                continue

def combineCommitCSVs():
    csvFolder = os.path.join(os.path.curdir, "changeLOC")
    fileList = os.listdir(csvFolder)
    allCSVs = open("completeLOC.csv", 'w')

    for fileName in fileList:
        csvPath = os.path.join(csvFolder, fileName)
        csv = open(csvPath, "r")
        repoName = fileName[:len(fileName)-4]
        for line in csv.readlines():
            if 'dayDifference' not in line:
                line = line.split(',')
                days = line[3]
                if 'day' not in days:
                    #print(line)
                    day = 1
                    #print(line)
                    line[3] = str(day)
                    line.append(line[4])
                    line[4] = str(0)
                else:
                    days = days.split(' ')
                    day = days[0]
                    line[3] = str(day)
                line = (',').join(line)

                allCSVs.write(repoName+','+line)

        csv.close()
    allCSVs.close()

def combineCovCSVs():
    csvFolder = os.path.join(os.path.curdir, "codecov")
    fileList = os.listdir(csvFolder)
    allCSVs = open("completeCodeCov.csv", 'w')

    for fileName in fileList:
        csvPath = os.path.join(csvFolder, fileName)
        csv = open(csvPath, "r")
        repoName = fileName[:len(fileName)-4]
        print("Now parsing", repoName)
        for line in csv.readlines():
            if 'dayDifference' not in line:
                line = line.split(',')
                days = line[3]
                if 'day' not in days:
                    #print(repoName, line)
                    day = 1
                    #print(line)
                    line[3] = str(day)+"\n"
                else:
                    days = days.split(' ')
                    day = days[0]
                    line[3] = str(day)
                line = (',').join(line)

                allCSVs.write(repoName+','+line)

        csv.close()
    allCSVs.close()

def getAverages():
    csvFolder = os.path.join(os.path.curdir, "changeLOC")
    fileList = os.listdir(csvFolder)

    avgCsv = open("Avgstats.csv", 'w')
    for fileName in fileList:
        csvPath = os.path.join(csvFolder, fileName)
        csv = open(csvPath, "r")
        repoName = fileName[:len(fileName)-4]

        daySum = 0
        LOCSum = 0
        LOCChangeSum = 0
        lineCount = 0

        for line in csv.readlines():
            #print(line)
            # get sum of line[2], line[3], line[5]
            if 'dayDifference' not in line:
                line = line.strip().split(',')
                days = line[3]
                day = None
                if 'day' not in days:
                    day = 1
                    #print(line)
                else:
                    days = days.split(' ')
                    day = days[0]

                daySum += int(day)
                LOCSum += int(line[2])
                try:
                    LOCChangeSum += int(line[5])
                except:
                    LOCChangeSum += int(line[4])

                lineCount += 1
        line = [repoName, str(daySum/lineCount), str(LOCSum/lineCount), str(LOCChangeSum/lineCount)]
        line = (',').join(line)
        avgCsv.write(line+"\n")
    avgCsv.close()
    csv.close()

def get_repo(repoName, git):
    repo = git.get_repo(repoName)
    return repo


def main(argv):
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)

    return

if __name__== "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == 'search':
            searchRepos(int(sys.argv[2]))
        elif arg == 'csv':
            getReleaseCSVs()
        elif arg == 'commits':
            getCommits()
        elif arg == 'combine':
            combineCommitCSVs()
            combineCovCSVs()
        elif arg == 'average':
            getAverages()
    else:
        main(sys.argv[1:])
