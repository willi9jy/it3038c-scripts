#!/bin/bash 
# This script downloads covid data ad displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
PENDING=$(echo $DATA | jq '.[0].pending') 
DATE=$(2021-03-07)

echo "On $DATE  there were $PENDING pending  COVID cases"

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DATE=$(2021-03-07)

echo "On $DATE, there were $NEGATIVE negative COVID cases"

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
DEATH=$(echo $DATA | jq '.[0].death')
DATE=$(2021-03-07)

echo "On $DATE, there were $DEATH COVID related deaths"

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
DATE=$(2021-03-07)


echo "On $DATE, there were $HOSPITALIZED hospitalized  COVID cases"
