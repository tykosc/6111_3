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

We choose the following datasets to construct the final `INTEGRATED_DATASET.csv`:

1. 2017 - 2018 Schools NYPD Crime Data Report : 
https://data.cityofnewyork.us/Education/2017-2018-Schools-NYPD-Crime-Data-Report/kwvk-z7i9
2. 2017 - 2018 Current Year Monthly Attendence : 
https://data.cityofnewyork.us/Education/2017-2018-Current-Year-Monthly-Attendance/7u63-ib3x
3. 2017 - 2018 November2017 Avg Class Size School PTR - Open Data Portal : 
https://data.cityofnewyork.us/Education/2017-2018-November2017-Avg-Class-Size-School-PTR-O/szn6-bbuk

- **Mapping Process**
    1. Note that each of these datasets has a column named `DBN`, which is a unique identifier for a school. We use this column to perform a join across these datasets to get a more diversified dataset with respect to School Crimes, Attendence and Student/Teacher Ratio. Note that since all these datasets are for the same year and for roughly the same schools, joining them does not add a lot of variance ...
    2. For the first dataset ...
    3. For the second dataset ...
    4. For the third dataset ...
    5. Our final dataset has the columns ... and has ... rows.

- **Choice of Dataset**

---

### Internal Design

---

### Compelling Sample Run

---

### Other

