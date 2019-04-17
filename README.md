# 402-Course-Project


Team 11
==============================

### Members
Tyler Heise, Ryan Perez, Austin Pennyfeather

Research Questions
==============================

 ### Research Question 1: Is there a relationship between testing practices & release cycles?
 ### Research Question 2: Does the length of release cycles affect the quality of tests written?
 
 Tools
==============================
 [Cobertural](https://cobertura.github.io/cobertura/) \
 [CLOC](http://cloc.sourceforge.net/)
 

Repositories
==============================
[ActionBarSherlock]() \
[android-Ultra-Pull-To-Refresh]() \
[apollo]() \
[arthas]() \
[auto]() \
[canal]() \
[dbeaver]() \
[dropwizard]() \
[druid]() \
[fastjson]() \
[guava]() \
[guice]() \
[HanLP]() \
[incubator-druid]() \
[incubator-dubbo]() \
[incubator-shardingsphere]() \
[jedis]() \
[junit4]() \
[libgdx]() \
[mybatis-3]() \
[pinpoint]() \
[proxyee-down]() \
[redisson]() \
[retrofit]() \
[spring-boot]() \
[symphony]() \
[webmagic]() \
[xxl-job]() \
[zipkin]() \
[zxing]() 


Replication Instructions
==============================


### Step 1: Setting up project and navigating to root directory
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
```
##### Disclaimer: Before proceeding to attempt to execute the following instructions.<br/> Ensure that you complete "Setting up project and navigating to root directory"

#### Step 2: How to get the major releases from the respetive repositories into .csv files
```
 # Execute the script
 1. python3 script.py csv
 
 # Enter your Github credentials to clone the list of 30 repsositores.
 2. prompt "Github Username:"
    prompt to enter password:
 
 # Major releases will be stored in a folder called "releaseCVS" at the root directory as a .csv files as the name of the reposiotry.
 3. For example: "releaseCSVs/{repository name}.csv"
```

#### Step 3: How to get the commits from the respetive repositories.

```
 # Execute the script
 1. python3 script.py commits
 
 # Enter your Github credentials to clone the list of 30 repsositores.
 2. prompt "Github Username:"
    prompt to enter password:
    


```

#### How to generate the .csv for code coverage
```

```

### How to generate the scatterplots form the code coverage .csv files
```


```


