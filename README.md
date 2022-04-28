**Project 2 : COMS 6111 : Advanced Database Systems (Spring 2022)**

---
  - [Team](#team)
  - [List of files](#files)
  - [Running the Project](#running)
  - [Dataset Description](#datasetdesc)
  - [Internal Design](#design)
  - [Compelling Sample Run](#compellingrun)
  - [Other](#other)

---

### Team
- Nihar Maheshwari (`nm3223`)
- Talya Koschitzky (`tk2892`)

---

### List of Files

*Required Files*

- `runner.py` : Driver file for the program. Pass arguments in the order : `INTEGRATED_DATASET.csv`, `MIN_SUPPORT`, `MIN_CONFIDENCE` to run the driver code.
- `run.sh` : Shell script wrapper for `runner.py`. This takes in the same arguments as `runner.py` and simply forwards them to the python driver.
- `apriori.py` : Classes for implementing the Apriori Algorithm [`Apriori` (Abstract), `AprioriBase` (Implementation)]
- `datasets/INTEGRATED_DATASET.csv` : The final integrated dataset passes to the Apriori algorithm

*Additional Files*

- `requirements.txt` : Required for specifying dependencies in `pip`
- `.gitignore`: git ignore file for ensuring binarys and keys are not checked in

---

### Running the Project

*Running Locally*

```zsh
root@ee903ca282f7:/workspaces/$ tar -xvzf 611_3.tar.gz
root@ee903ca282f7:/workspaces/$ cd 6111_3
root@ee903ca282f7:/workspaces/6111_3$ pip install -r requirements.txt
root@ee903ca282f7:/workspaces/6111_3$ chmod +x run.sh
root@ee903ca282f7:/workspaces/6111_3$ ./run.sh INTEGRATEED_DATASET.csv <min_sup> <min_conf>
```

*Running on the Server*

```zsh
nm3223@cs6111-p1-instance:~/$ source ~/.venv/bin/activate
(.venv) nm3223@cs6111-p1-instance:~/$ cd 6111_3
(.venv) nm3223@cs6111-p1-instance:~/6111_3$ chmod +x run.sh
(.venv) nm3223@cs6111-p1-instance:~/6111_3$ ./run.sh INTEGRATEED_DATASET.csv <min_sup> <min_conf>
```

---

### Dataset Description

- **Which NYC Open Dataset(s)**

We choose the following dataset to construct the final `INTEGRATED_DATASET.csv`:

FDNY Monthly Response Times: Average response times to incidents by Year, Month, Incident classification and borough.

Link: https://data.cityofnewyork.us/Social-Services/FDNY-Monthly-Response-Times/j34j-vqvt


- **Mapping Process**
  
  Our goal was for every row of the dataset to correspond to one emergency incident from the year 2017. 

  Steps: 
  1. Select rows that correspond to the year 2017.  
  2. Filter out rows where an incident is 'All Fire/Emergency Incidents' or the borough is 'Citywide', as these rows are aggregates of other rows. 
  3. Duplicate all remaining rows by the number of INCIDENTCOUNT for that row, so that we have one row per incident
  4. Convert average response time to number of seconds
  5. Bucket average response time into four quartiles 
  6. Select the columns INCIDENTCLASSIFICATION, which corresponds to the type of incident 'False Alarm, Fire, Medical, etc.', INCIDENTBOROUGH, which corresponds to the borough, and 'AVERAGERESPONSETIME', which describes avg. response time range for the event
  7. Our final dataset contained 585,368 rows
    

- **Choice of Dataset**

  We chose this dataset because it is very important for a neighborhood to have fast emergency services, and small differences in response time could be the difference between life and death. We thought that it would be interesting to know if the average response time would differ between different boroughs, and whether different types of emergencies were more likely in ceratin boroughs, or whether certain types of emergencies had significantly different response times. 
  
  Another reason we chose this dataset is that it was very large, and allowed us to generate high confidence rules with good support as well.  

---

### Internal Design

- Our program is driven by the `runner.py` file. This file is responsible for reading the CSV and feeding it to the `Apriori` algorithm (implemented in `apriori.py`)
- `apriori.py` contains classes [ `Apriori` (Abstract) and `AprioriBase` (Implementation)] implementing the apriori algorithm. 
- The apriori algorithm is structured according to the following pseudo-code (as described in the paper):

---

### Compelling Sample Run

---

### Other

