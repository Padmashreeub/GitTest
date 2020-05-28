#!/bin/bash

#echo "testing shell script"
tempip='\<(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]?)\>'
ip=($tempip\.){3}$tempip

function checkipping()
{
  if  echo $1|grep -Eo "$ip" >/dev/null
            then
              #echo "$1 is proper ip"
               if  ping -c 2 $1  >/dev/null
                   then
                     echo "$1 : UP"
               else
                     echo "$1 : Down"
               fi

        else
           echo "$1 is not a proper ip"
  fi
}

  
if [[ $# -gt 0 ]]
then
 for i in $*
  do
    checkipping $i
  done


elif [[ -p /dev/stdin ]]
then
    read line
    checkipping $line
  


else
  echo "you did't enter the ip's either through cmd line arg or stdin pipe"

fi
