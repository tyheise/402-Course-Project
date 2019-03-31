import os
import sys
import getpass
from github import Github

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
            releaseDates.write("id,tag_name,until,since,dayDifference\n")
            prevDate = None
            for i in range(releaseCount - 1):
                currRelease = releases[i]
                prevRelease = releases[i+1]

                currCreatedAt = currRelease.created_at
                prevCreatedAt = prevRelease.created_at

                dayDifference = currCreatedAt - prevCreatedAt

                releaseDates.write(str(currRelease.id)+","+currRelease.tag_name+","+str(currCreatedAt)+","+str(prevCreatedAt)+","+str(dayDifference)+"\n")

        line = reposFile.readline().strip()

    reposFile.close()


def get_repo(repoName, git):
    repo = git.get_repo(repoName)
    return repo


def main(argv):
    username = input("Github Username:")
    pw = getpass.getpass()
    git = Github(username, pw)


    # orgName = argv[0]
    # repoName = argv[1]
    #
    # git = Github()
    # org = git.get_organization(orgName)
    # repo = org.get_repo(repoName)
    #
    # print(repo.html_url)
    #
    # releases = repo.get_releases()
    # print(releases.totalCount)
    #
    # #for release in releases:

    return

if __name__== "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == 'search':
            searchRepos(int(sys.argv[2]))
        elif arg == 'csv':
            getReleaseCSVs()
    else:
        main(sys.argv[1:])
