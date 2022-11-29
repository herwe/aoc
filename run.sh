#!/bin/bash
ARGV=$1
ARGV2=$2
dir="$(pwd)"
extension="/$ARGV/day_"
dir2="$dir$extension"
ENDLINE=""
finaldir=""
if [[ $ARGV2 == '1' ]]; then
  ENDLINE="01"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '2' ]]; then
  ENDLINE="02"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '3' ]]; then
  ENDLINE="03"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '4' ]]; then
  ENDLINE="04"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '5' ]]; then
  ENDLINE="05"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '6' ]]; then
  ENDLINE="06"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '7' ]]; then
  ENDLINE="07"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '8' ]]; then
  ENDLINE="08"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV2 == '9' ]]; then
  ENDLINE="09"
  finaldir="$dir2$ENDLINE"
else
  finaldir="$dir2$ARGV2"
fi

printout="Running solution located at... "
echo "$printout$finaldir"
echo ""
cd "$finaldir" && python3 main.py
