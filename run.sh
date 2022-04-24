#!/bin/bash

# validate inputs

if [ $# -ne 3 ]
    then
        echo "[run.sh] : expected 3 arguments. $# passed. quitting .."
        exit 1
fi

# log arguments

echo "[run.sh] arguments :- "
echo "[run.sh] .csv file : [$1]"
echo "[run.sh] min_sup   : [$2]"
echo "[run.sh] min_conf  : [$3]"

# pass to python script

echo 
echo "[run.sh] executing python script : runner.py"

python3 runner.py $1 $2 $3