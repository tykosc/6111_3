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

  We chose this dataset because it is very important for a neighborhood to have fast emergency services, and small differences in response time could be the difference between life and death. We thought that it would be interesting to know if the average response time would differ between different boroughs, and whether different types of emergencies were associated with ceratin boroughs, or whether certain types of emergencies were associated with different response times. 
  
  Another reason we chose this dataset is that it was very large, and allowed us to generate high confidence rules with good support as well.  

---

### Internal Design

- Our program is driven by the `runner.py` file. This file is responsible for reading the CSV and feeding it to the `Apriori` algorithm (implemented in `apriori.py`)
- `apriori.py` contains classes [ `Apriori` (Abstract) and `AprioriBase` (Implementation)] implementing the apriori algorithm. 
- The apriori algorithm is structured according to the pseudo-code in [fig. 1](http://www.cs.columbia.edu/~gravano/Qual/Papers/agrawal94.pdf) of Fast Algorithms for Mining Association Rules (Agrawal, Srikant)
- We first begin by initializing all `1-itemsets` for the dataset via the method `get_f1_items`. This method is called once during initialization of the algorithm.
- `run` method encapsulates the main apriori algorithm. This method loops through possible values of `k` and generated candidates `C_k` using the apriori algorithm
- `run` internally calls `apriori_gen` which is responsible for joining the `c_{k-1}` sets to generate candidate `c_{k}` itemsets using the `sql` query mentioned in the paper.
- `generate_association_rules` is a function to carry out the final step of generating the association rules for the frequent itemsets generated. 
- methods `ppfrequencies`, `pprint_association_rules` are utility methods to print formatted text to standard output.

*Variation*
- We implement the algorithm from [fig. 1](http://www.cs.columbia.edu/~gravano/Qual/Papers/agrawal94.pdf) while handling speacial bucketing for continuous time values.
- We bucket the average response times into 4 quantiles [(222-283s, 283-294s, 294-333s, 333-336s)] (using [pd.cut](https://pandas.pydata.org/docs/reference/api/pandas.cut.html)) in order to better infer the association rules involving the response times.

---

### Compelling Sample Run

Use the following command specification for a compelling sample run.
- `min_sup`: 0.01
- `min_conf`: 0.7
- `dataset` : INTEGRATED-DATASET.csv

```zsh
root@ee903ca282f7:/workspaces/6111_3$ ./run.sh INTEGRATED-DATASET.csv 0.01 0.7
```
*Explaination*

Note that per our dataset choice (mentioned above), we wanted to examine the nuances between the FDNY response times for different Boroughs of New York City. Per our investigation, following were the observations we found:

- Response Times for ambulance services followed the following trend:
(For medical emergencies):

`Brooklyn = Queens = Staten Island (222-283 s) < Bronx (283-294 s)< Manhattan (294-333 s)`

(For non-medical emergencies)
`Brooklyn (283-294 s) < Queens = Staten Island (294-333 s) < Manhattan = Bronx (333-336 s)`



This is an interesting result as it clearly indicates that emergency services (medical emergencies) in Manhattan were considerably slower (even a few second difference matters here) than rest of the New York Boroughs. This could be attributed due to the traffic in Manhattan or other reasons such as fewer emergency stations.

Also, another intersting fact that can be seen is that the FDNY does a good job in prioritizing tasks in the sens that medical emergencies are adressed to quicker than non-medical emergencies in general.

*Output Example*
```
['response time 222-283s'] ==> ['Medical Emergencies'] (Conf: 79%, Supp: 25%)
['response time 333-336s'] ==> ['NonMedical Emergencies'] (Conf: 100%, Supp: 20%)
['Brooklyn', 'Medical Emergencies'] ==> ['response time 222-283s'] (Conf: 100%, Supp: 13%)
'Manhattan', 'Medical Emergencies'] ==> ['response time 294-333s'] (Conf: 100%, Supp: 13%)
.
.
```
Note : This is not the complete output. Please refer to the `example-run.txt` file for the complete output.

---

### Other

The `.ipynb` files present in this project are a code description of all the pre-processing steps we carried out.
