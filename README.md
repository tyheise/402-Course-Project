# 402-Course-Project

 ### Research Question: Is there a relationship between testing practices & release cycles?
 
Team 11
==============================

### Members
Tyler Heise, Ryan Perez, Austin Pennyfeather
 
 Tools
==============================
 [Reaper tool, RepoReapers Contributors, reaper (2015)](https://reporeapers.github.io)
 

Repositories
==============================
```
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
 ```

Replication Instructions
==============================

#### How to calculate LOC and changed LOC in between releases

```
  # Create a virtual environment
  1. python3 virtualenv venv
  
  # Activate the newly-created virtualenv.
  2. source venv/bin/activate
  
  # Install all dependencies
  3. pip install -r requirements.txt
  
  # Clone Repositories
  4. git clone https://github.com/tyheise/402-Course-Project.git
  
  # Naviage to location where you cloned the repository
  5. cd 402-Course-Project
  
  # Execute the script
  6. pyhton findscript.py
  
  # .csv files will be created and stored in the respective folders: LOC/ and changeLOC/
  7.  Example:
           LOC/ActionBarSher k.csv
           LOC/HanLP.csv
           LOC/android-Ultra-Pull-To-Refresh.csv                  
           LOC/apollo.csv
           LOC/arthas.csv
           LOC/auto.csv
           LOC/canal.csv
           LOC/dbeaver.csv
           LOC/dropwizard.csv
           LOC/druid.csv
           LOC/fastjson.csv
           LOC/guava.csv
           LOC/guice.csv
           LOC/incubator-druid.csv
           LOC/incubator-dubbo.csv
           LOC/incubator-shardingsphere.csv
           LOC/jedis.csv
           LOC/junit4.csv
           LOC/libgdx.csv
           LOC/mybatis-3.csv
           LOC/pinpoint.csv
           LOC/proxyee-down.csv
           LOC/redisson.csv
           LOC/retrofit.csv
           LOC/spring-boot.csv
           LOC/symphony.csv
           LOC/webmagic.csv
           LOC/xxl-job.csv
           LOC/zipkin.csv
           LOC/zxing.csv
           
           changeLOC/ActionBarSher k.csv
           changeLOC/HanLP.csv
           changeLOC/android-Ultra-Pull-To-Refresh.csv
           changeLOC/apollo.csv
           changeLOC/arthas.csv
           changeLOC/auto.csv
           changeLOC/canal.csv
           changeLOC/dbeaver.csv
           changeLOC/dropwizard.csv
           changeLOC/druid.csv
           changeLOC/fastjson.csv
           changeLOC/guava.csv
           changeLOC/guice.csv
           changeLOC/incubator-druid.csv
           changeLOC/incubator-dubbo.csv
           changeLOC/incubator-shardingsphere.csv
           changeLOC/jedis.csv
           changeLOC/junit4.csv
           changeLOC/libgdx.csv
           changeLOC/mybatis-3.csv`
           changeLOC/pinpoint.csv
           changeLOC/proxyee-down.csv
           changeLOC/redisson.csv
           changeLOC/retrofit.csv
           changeLOC/spring-boot.csv
           changeLOC/symphony.csv
           changeLOC/webmagic.csv
           changeLOC/xxl-job.csv
           changeLOC/zipkin.csv
           changeLOC/zxing.csv
        
```

#### How to get the branch and statement coverage from a repository 

```
# We are assuming you have done the steps 1-5,on "How to calculate LOC and changed LOC in between releases" mentioned above

# 

```

#### How to generate the .csv for code coverage
```

```
