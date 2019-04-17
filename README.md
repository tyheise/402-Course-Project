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

### Step 0: Download R and R Studio
```
These steps apply specifically to windows users. If you have another operating system, the same steps apply just choose the files that apply to your operating system.

1. Download R from http://cran.us.r-project.org/.

2. Click on Download R for Windows. Click base. Click on Download R-3.5.3 for Windows (32/64 bit) (or a newer version that appears).

3. Install R. Leave all default settings in the installation options

4. Download RStudio Desktop for windows from http://rstudio.org/download/desktop. Select Download (RStudio Desktop Open Source License). It will allow you to select from a list of installers. Choose (it should be called something like RStudio 1.2.1335 - Windows 7+. Choose default installation options.

5. Open RStudio.
```

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
 # Commits will be stored in a folder called "commits" at the root directory as a .csv files as the name of the reposiotry.
 3. For example: "commits/{repository name}.csv"
```

#### Step 4: How to get the code coverage for the respective repositiroes.
```
# Execute the script
1. python3 codecov.py

# Code coverage will be stored in a folder called "codeCov" at the root directory as .csv files as the name of the repository.
2. For example: "codeCov/{repository name}.csv"
```

### Step 5: We compile all .csv in Steps 1 - Steps 4 into two large .csv files to get complete lines of code and complete code coverage:
```
# Execute the script
1. python3 script.py combine

# complete lines of code and complete code coverage will be will be stored in the respective file names "completeLOC.csv"
# and completeCodeCov.csv at the root direcotry
```

### Step 6: 


