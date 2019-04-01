import os
import subprocess

def search_files(directory='.', extension='java'):
    testfiles = []
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            nameNoExt = name.split(".")[0]
            if extension and name.lower().endswith(extension) and nameNoExt.endswith("Test"):
                testfiles.append(os.path.join(dirpath, name))
    return testfiles



def getLOC(filepath):
    with open(filepath) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def t():
    testfilepaths = search_files()
    print(testfilepaths[0])
    print(getLOC(testfilepaths[0]))


    # test stuff
    i = 0
    for f in testfilepaths:
        name = f.split("/")[-1]
        print(name + " has " + str(getLOC(f)))

def clonerep(url):
    name = url.split("/")[-1].split(".")[0]
    subprocess.run(["git", "clone", url, "repos/" + name + "/"])


def main():
    hardcoded = "https://github.com/spring-projects/spring-boot.git"
    clonerep(hardcoded)
    name = hardcoded.split("/")[-1].split(".")[0]
    testfilepaths = search_files("repos/" + name + "/")
    for f in testfilepaths:
        name = f.split("/")[-1]
        print(name + " has " + str(getLOC(f)))


    

main()