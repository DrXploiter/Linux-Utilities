#!/bin/bash

echo "Start Date: "
read startDate

echo "End Date: "
read endDate

echo "How many lines should be created: "
read numLines

d=$startDate
while [ "$d" != $endDate ]; 
do 
  python lorem -n $numLines --randomize > bulk/"$d"
  touch --date $d bulk/"$d"
  d=$(date -I -d "$d + 1 day")
done



