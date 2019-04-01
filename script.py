import os
import sys
import getpass
from github import Github
from datetime import datetime

def searchRepos(maxNumOfRepos):
    git = Github()
    repos = git.search_repositories('stars:>10000 language:Java', sort='stars', order='desc')

    f = open("reposConsidered.txt", "w")
    i=0
    while(i<maxNumOfRepos):
        f.write(repos[i].full_name +"\n")
        i+=1
    f.close()
    return

def getReleaseCSVs():
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)
    reposFile = open("reposConsidered.txt", "r")

    line = reposFile.readline().strip()
    while(line):
        repo = get_repo(line, git)
        releases = repo.get_releases()
        releaseCount = releases.totalCount

        if releaseCount > 1:
            repoName = ((repo.full_name).split("/"))[1]

            releaseDates = open("releaseCSVs/"+repoName+".csv", "w")
            releaseDates.write("repo,id,tag_name,until,since,dayDifference\n")
            prevDate = None
            for i in range(releaseCount - 1):
                currRelease = releases[i]
                prevRelease = releases[i+1]

                currCreatedAt = currRelease.created_at
                prevCreatedAt = prevRelease.created_at

                dayDifference = currCreatedAt - prevCreatedAt

                releaseDates.write(repo.full_name+','+str(currRelease.id)+","+currRelease.tag_name+","+str(currCreatedAt)+","+str(prevCreatedAt)+","+str(dayDifference)+"\n")

        line = reposFile.readline().strip()

    reposFile.close()

def getCommits():
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)

    csvFolder = os.path.join(os.path.curdir, "releaseCSVs")
    fileList = os.listdir(csvFolder)

    for fileName in fileList:
        csvPath = os.path.join(csvFolder, fileName)
        csv = open(csvPath)

        lines = csv.readlines()
        repoName = (lines[1].split(","))[0]
        repo = git.get_repo(repoName)

        repoName2 = (repoName.split("/"))[1]

        repoFile = open(os.path.join(os.path.curdir,'commits',repoName2+".csv"), 'w')
        for i in range(1,len(lines)-1):
            line = lines[i].split(",")

            # 2019-03-26 15:08:13
            until = datetime.strptime(line[3], '%Y-%m-%d %H:%M:%S')
            since = datetime.strptime(line[4], '%Y-%m-%d %H:%M:%S')

            commits = repo.get_commits(until=until, since=since)
            if commits.totalCount > 0:
                repoFile.write(line[1]+","+line[2]+","+commits[0].sha+","+str(until-since)+"\n")

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
    else:
        main(sys.argv[1:])
