#!/usr/bin/env bash

Line1="text line #1"
Line2="text line #2"
Line3="text line #3"
Line4="text line #3"

curl 'http://raspi:5000/sendmsg' -X POST \
-H "Content-type: application/json" -d '{"lcd1":"'"$Line1"'", "lcd2":"'"$Line2"'", "lcd3":"'"$Line3"'", "lcd4":"'"$Line4"'"}'
