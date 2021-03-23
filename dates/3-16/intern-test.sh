#!/bin/bash
 
 cd ../2-25

 STRING="START"
 echo $STRING
#compiling files
  gfortran -O3 -o vectorq.exe vectorq.f
  gfortran -O3 -o omegainv.exe omegainv.f

while read p; do
  #creating exec file
  python writingvectorq_omegainv.py $p


#running execfile
  ./vectorq.exec
  ./omegainv.exec
  echo $p
done <date_list.txt

 STRING="DONE"
 echo $STRING