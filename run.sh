#!/bin/bash
dir="$(pwd)"
extension="/src/day_"
dir2="$dir$extension"
ARGV=$1
ENDLINE=""
finaldir=""
if [[ $ARGV == '1' ]]; then
  ENDLINE="01"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '2' ]]; then
  ENDLINE="02"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '3' ]]; then
  ENDLINE="03"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '4' ]]; then
  ENDLINE="04"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '5' ]]; then
  ENDLINE="05"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '6' ]]; then
  ENDLINE="06"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '7' ]]; then
  ENDLINE="07"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '8' ]]; then
  ENDLINE="08"
  finaldir="$dir2$ENDLINE"
elif [[ $ARGV == '9' ]]; then
  ENDLINE="09"
  finaldir="$dir2$ENDLINE"
else
  finaldir="$dir2$ARGV"
fi

printout="Running solution located at... "
echo "$printout$finaldir"
echo ""
cd "$finaldir" && python3 main.py
