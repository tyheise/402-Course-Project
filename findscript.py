import os
import subprocess

# hardcodedlist = "JakeWharton/ActionBarSherlock liaohuqiu/android-Ultra-Pull-To-Refresh ctripcorp/apollo alibaba/arthas google/auto alibaba/canal dbeaver/dbeaver dropwizard/dropwizard alibaba/druid alibaba/fastjson google/guava google/guice hankcs/HanLP apache/incubator-druid apache/incubator-dubbo apache/incubator-shardingsphere xetorthio/jedis junit-team/junit4 libgdx/libgdx mybatis/mybatis-3 naver/pinpoint proxyee-down-org/proxyee-down redisson/redisson square/retrofit spring-projects/spring-boot b3log/symphony code4craft/webmagic xuxueli/xxl-job openzipkin/zipkin zxing/zxing".split(" ")
# hardcodedlist = ['ctripcorp/apollo',  'google/auto',  'dbeaver/dbeaver',  'dropwizard/dropwizard',  'google/guava',  'google/guice',  'hankcs/HanLP',  'apache/incubator-druid',  'apache/incubator-shardingsphere',  'xetorthio/jedis']
# hardcodedlist = ['apache/incubator-shardingsphere', ]
# hardcodedlist = ['xetorthio/jedis',  'mybatis/mybatis-3',  'naver/pinpoint',  'broken builds proxyee-down-org/proxyee-down',  'broken builds redisson/redisson',  'broken build spring-projects/spring-boot',  'b3log/symphony',  'code4craft/webmagic',  'xuxueli/xxl-job',  'openzipkin/zipkin']
hardcodedlist = ['ctripcorp/apollo', 'google/auto', 'dbeaver/dbeaver', 'dropwizard/dropwizard', 'google/guava', 'google/guice', 'hankcs/HanLP', 'apache/incubator-druid', 'apache/incubator-shardingsphere', 'xetorthio/jedis', 'mybatis/mybatis-3', 'naver/pinpoint', 'proxyee-down-org/proxyee-down', 'redisson/redisson', 'spring-projects/spring-boot', 'b3log/symphony', 'code4craft/webmagic', 'xuxueli/xxl-job', 'openzipkin/zipkin']
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
    clocstr = subprocess.check_output("cloc " + filepath + " --csv", shell=True).decode('ascii').split(",")[-1].strip()
    # print("LOC FOR " + filepath + " " + clocstr)
    if clocstr.startswith('0 text files.'):
        return 0
    return int(clocstr)
    # i = 0
    # with open(filepath) as f:
    #     for i, l in enumerate(f):
    #         pass

    # if i:
    #     return i + 1
    # else:
    #     return 0



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
    print("git"+ " clone " + "https://github.com/" + url + " repos/" + name + "/")
    os.system("git"+ " clone " + "https://github.com/" + url + " repos/" + name + "/" )

def main(hardcodedlist):
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

        for line in lines:
            llist = line.split(",")
            print(llist)
            os.chdir("repos/" + reponame)
            subprocess.run(["git", "checkout", "--", "."])

            subprocess.run(["git", "checkout", llist[2]])
            subprocess.run(["git", "checkout", "--", "."])

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

def getLOCChanges(hardcodedlist):

    for rep in hardcodedlist:
        reponame = rep.split("/")[1]
        csv = open("LOC/" + reponame + ".csv", "r")
        lines = csv.readlines()
        LOClist =  []
        i = 0
        for l in lines[1:]:
            LOClist.append(int(l.split(",")[2].strip()))
            i += 1

        LOCChangelist = []
        i = 0
        while i < len(LOClist) - 1:
            LOCChangelist.append(-1*(LOClist[i] - LOClist[i+1]))
            i+= 1
        LOCChangelist = [0] + LOCChangelist

        newCSV = open("changeLOC/" + reponame + ".csv", "w")
        newCSV.write(lines[0].strip() + ",changeLOC\n")

        i = 0
        for l in lines[1:]:
            newCSV.write(l.strip() + "," + str(LOCChangelist[i]) + "\n")
            i+=1
        newCSV.close()

if __name__ == '__main__':
    main(hardcodedlist)
    getLOCChanges(hardcodedlist)
