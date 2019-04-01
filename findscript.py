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
    i = 0
    with open(filepath) as f:
        for i, l in enumerate(f):
            pass

    if i:
        return i + 1
    else:
        return 0



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
    os.system("git"+ " clone " + "https://github.com/" + url + " repos/" + name + "/" )

def main():
    hardcodedlist = "liaohuqiu/android-Ultra-Pull-To-Refresh ctripcorp/apollo alibaba/arthas google/auto alibaba/canal dbeaver/dbeaver dropwizard/dropwizard alibaba/druid alibaba/fastjson google/guava google/guice hankcs/HanLP apache/incubator-druid apache/incubator-dubbo apache/incubator-shardingsphere xetorthio/jedis junit-team/junit4 libgdx/libgdx mybatis/mybatis-3 naver/pinpoint proxyee-down-org/proxyee-down redisson/redisson square/retrofit spring-projects/spring-boot b3log/symphony code4craft/webmagic xuxueli/xxl-job openzipkin/zipkin zxing/zxing".split(" ")
    """
JakeWharton/ActionBarSherlock
 liaohuqiu/android-Ultra-Pull-To-Refresh
 ctripcorp/apollo
 alibaba/arthas
 google/auto
 alibaba/canal
 dbeaver/dbeaver
 dropwizard/dropwizard
 alibaba/druid
 alibaba/fastjson
 google/guava
 google/guice
 hankcs/HanLP
 apache/incubator-druid
 apache/incubator-dubbo
 apache/incubator-shardingsphere
 xetorthio/jedis
 junit-team/junit4
 libgdx/libgdx
 mybatis/mybatis-3
 naver/pinpoint
 proxyee-down-org/proxyee-down
 redisson/redisson
 square/retrofit
 spring-projects/spring-boot
 b3log/symphony
 code4craft/webmagic
 xuxueli/xxl-job
 openzipkin/zipkin
 zxing/zxing
 """
    for hardcoded in hardcodedlist:
        clonerep(hardcoded)
        reponame = hardcoded.split("/")[-1].split(".")[0]
        
        coms = open("commits/" + reponame + ".csv")
        lines = coms.readlines()
        #     print(lines)

        csv = open("LOC/" + reponame + ".csv", "w")
        #     releaseDates.write("repo,id,tag_name,until,since,dayDifference\n")
        csv.write("id,tag_name,LOC,dayDifference, dayDifferenceHours\n")

        #  skip first line
        #     iterlines = iter(lines)
        #     next(iterlines)
        for line in lines:
            llist = line.split(",")
            print(llist)
            os.chdir("repos/" + reponame)
            subprocess.run(["git", "checkout", llist[2]])
            os.chdir("../..")
                
            # get LOC for each test file
            testfilepaths = search_files("repos/" + reponame + "/")
            loc = 0
            for f in testfilepaths:
                loc += getLOC(f)

            id = llist[0]
            tag = llist[1]
            daydiff = llist[3].strip()
            toWrite = id + "," + tag + "," + str(loc)+ "," + daydiff
            if len(llist) == 5:
                daydiffhr = llist[4].strip()
                toWrite += "," + daydiffhr
            toWrite += "\n"
            csv.write(toWrite)
        csv.close


main()