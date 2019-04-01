import xml.etree.ElementTree as ET
import subprocess
import os




def insertIntoPom(repdir):
    # ET.register_namespace("", "http://maven.apache.org/POM/4.0.0")
    # tree = ET.parse("apollo/pom.xml")
    # plugs = tree.findall("./{http://maven.apache.org/POM/4.0.0}build/{http://maven.apache.org/POM/4.0.0}plugins")

    # cloverplug = ET.fromstring("<plugin> <groupId>org.openclover</groupId> <artifactId>clover-maven-plugin</artifactId> <version>4.2.0</version> <configuration> <generateXml>true</generateXml> </configuration> </plugin>")



    # if len(plugs) != 0:
    #     plugs[0].insert(0, cloverplug)
    #     tree.write("pom.xml")

    stre = "<plugin> <groupId>org.openclover</groupId> <artifactId>clover-maven-plugin</artifactId> <version>4.2.0</version> <configuration> <generateXml>true</generateXml> </configuration> </plugin>"
    fileHandle = open ( repdir + '/pom.xml',"r")
    lines = fileHandle.readlines()
    fileHandle.close()

    lastlineind = len(lines) - 1
    idd = 0
    i = 0

    for line in lines:
        if (line.strip() == "<plugins>"):
            idd = i
            break
        i += 1

    if idd != 0:
        lines.insert(idd+1, stre)

        fileHandle = open(repdir + "/pom.xml", "w")
        contents = "".join(lines)
        fileHandle.write(contents)
        fileHandle.close()
    else:
        projend = 0
        j = 0
        #plugins tag not found so append to end
        for line in lines:
            if (line.strip() == "</project>"):
                projend = j
                break
            j += 1
    
        lines.insert(projend, "<build><plugins><plugin> <groupId>org.openclover</groupId> <artifactId>clover-maven-plugin</artifactId> <version>4.2.0</version> <configuration> <generateXml>true</generateXml> </configuration> </plugin> </plugins> </build>")

        fileHandle = open(repdir + "/pom.xml", "w")
        contents = "".join(lines)
        fileHandle.write(contents)
        fileHandle.close()
        


# runs openclover
def runcov(repdir):
    os.chdir(repdir + "/")
    subprocess.run(["mvn", "clean" ,"clover:setup" ,"test" ,"clover:aggregate" ,"clover:clover"
])






def main():
    # repoURL = "https://github.com/ctripcorp/apollo.git"
    # repoURL = "https://github.com/shuzheng/zheng.git"
    repoURL = "https://github.com/alibaba/arthas.git"
    repdir = repoURL.split("/")[-1]
    repdir = repdir.split(".")[0]
    print(repdir)
    repoPath = "repos/"
    subprocess.run(["rm", "-r", "-f", "apollo/"])
    subprocess.run(["git", "clone", repoURL])
    insertIntoPom(repdir)
    runcov(repdir)


main()