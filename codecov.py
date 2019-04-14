import xml.etree.ElementTree as ET
import subprocess
import os
import glob
import time


def clonerep(url):
    name = url.split("/")[-1].split(".")[0]
    os.system("git"+ " clone " + "https://github.com/" + url + " repos/" + name + "/" )

def insertIntoPom(repdir):
    # ET.register_namespace("", "http://maven.apache.org/POM/4.0.0")
    # tree = ET.parse("apollo/pom.xml")
    # plugs = tree.findall("./{http://maven.apache.org/POM/4.0.0}build/{http://maven.apache.org/POM/4.0.0}plugins")

    # cloverplug = ET.fromstring("<plugin> <groupId>org.openclover</groupId> <artifactId>clover-maven-plugin</artifactId> <version>4.2.0</version> <configuration> <generateXml>true</generateXml> </configuration> </plugin>")



    # if len(plugs) != 0:
    #     plugs[0].insert(0, cloverplug)
    #     tree.write("pom.xml")

    # stre = "<plugin> <groupId>org.openclover</groupId> <artifactId>clover-maven-plugin</artifactId> <version>4.2.0</version> <configuration> <generateXml>true</generateXml> </configuration> </plugin>"

    stre = "<plugin> <groupId>org.codehaus.mojo</groupId> <artifactId>cobertura-maven-plugin</artifactId> <version>2.7</version> <configuration> <formats> <format>html</format> <format>xml</format> </formats><aggregate>true</aggregate> </configuration> </plugin>"
    fileHandle = open ( repdir + '/pom.xml',"r")
    lines = fileHandle.readlines()
    fileHandle.close()

    lastlineind = len(lines) - 1
    idd = 0
    i = 0

    for line in lines:
        if (line.strip() == "<plugin>"):
            idd = i
            break
        i += 1
    idd -= 1

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
        projend -= 1
        
        # lines.insert(projend, "<build><plugins><plugin> <groupId>org.openclover</groupId> <artifactId>clover-maven-plugin</artifactId> <version>4.2.0</version> <configuration> <generateXml>true</generateXml> </configuration> </plugin> </plugins> </build>")

        lines.insert(projend, "<build><plugins><plugin> <groupId>org.codehaus.mojo</groupId> <artifactId>cobertura-maven-plugin</artifactId> <version>2.7</version> <configuration> <formats> <format>html</format> <format>xml</format> </formats> <aggregate>true</aggregate></configuration> </plugin> </plugins> </build>")

        fileHandle = open(repdir + "/pom.xml", "w")
        contents = "".join(lines)
        fileHandle.write(contents)
        fileHandle.close()
    # print(contents)

        


# runs cobertura
def runcov(repdir):
    os.chdir("repos/" + repdir + "/")
    subprocess.call(["mvn", "cobertura:cobertura"])
    # subprocess.run(["mvn", "clean" ,"clover:setup" ,"test" ,"clover:aggregate" ,"clover:clover"])
    os.chdir("../..")




def getAllCovXML(repdir):
    covXMLs = []
    for dirpath, dirnames, files in os.walk('repos/' + repdir + '/'):
        for name in files:
            if name == "coverage.xml":
                covXMLs.append(os.path.join(dirpath, name))
    # print(covXMLs)
    return covXMLs


def getTotalCodeCov(covList):
    linesCovered = 0
    totalLines = 0

    for covFile in covList:
        root = ET.parse(covFile)
        c = root.find(".")
        percent = c.attrib["line-rate"]
        print(percent)
        linesCovered += int(c.attrib["lines-covered"])
        totalLines += int(c.attrib["lines-valid"])
    return float(linesCovered/totalLines)


def main():
    # repoURL = "https://github.com/ctripcorp/apollo.git"
    # repoURL = "https://github.com/shuzheng/zheng.git"
    # repoURL = "https://github.com/alibaba/arthas.git"
    # repoURL = "https://github.com/openzipkin/zipkin"
    """
  'ctripcorp/apollo'
  'google/auto'
  'dbeaver/dbeaver'
  'dropwizard/dropwizard'
  'google/guava'
  'google/guice'
  'hankcs/HanLP'
  'apache/incubator-druid'
  'apache/incubator-shardingsphere'
  'xetorthio/jedis'

  'mybatis/mybatis-3'
  'naver/pinpoint'
  'proxyee-down-org/proxyee-down'
  'redisson/redisson'
  'spring-projects/spring-boot'
  'b3log/symphony'
  'code4craft/webmagic'
  'xuxueli/xxl-job'
  'openzipkin/zipkin'
 """


    hardcodedList = ['ctripcorp/apollo',  'google/auto',  'dbeaver/dbeaver',  'dropwizard/dropwizard',  'google/guava',  'google/guice',  'hankcs/HanLP',  'apache/incubator-druid',  'apache/incubator-shardingsphere',  'xetorthio/jedis',  'mybatis/mybatis-3',  'naver/pinpoint',  'proxyee-down-org/proxyee-down',  'redisson/redisson',  'spring-projects/spring-boot',  'b3log/symphony',  'code4craft/webmagic',  'xuxueli/xxl-job',  'openzipkin/zipkin']

    for hardcoded in hardcodedList:
        
        clonerep(hardcoded)
        repdir = hardcoded.split("/")[-1].split(".")[0]
    
        # for a single repo...
        coms = open("commits/" + repdir + ".csv")
        lines = coms.readlines()

        csv = open("codecov/" + repdir + ".csv", "w")
        csv.write("id,tag_name,covpercent,dayDifference, dayDifferenceHours\n")

        for line in lines:
            llist = line.split(",")
            print(llist)
            os.chdir("repos/" + repdir)
            subprocess.run(["git", "checkout", "--", "."])
            subprocess.run(["git", "checkout", llist[2]])
            subprocess.run(["git", "checkout", "--", "."])
            os.chdir("../..")
            
            insertIntoPom("repos/" + repdir)

            #codecov lines
            runcov(repdir)
            codeCovFiles = getAllCovXML(repdir)
            if (len(codeCovFiles) == 0):
                print("NO COV FILES FOUND SKIP")
                continue
            totalCoveragePercent = getTotalCodeCov(codeCovFiles)

            id = llist[0]
            tag = llist[1]
            daydiff = llist[3].strip()
            toWrite = id + "," + tag + "," + str(totalCoveragePercent)+ "," + daydiff
            if len(llist) == 5:
                daydiffhr = llist[4].strip()
                toWrite += "," + daydiffhr
            toWrite += "\n"
            csv.write(toWrite)
        csv.close




main()