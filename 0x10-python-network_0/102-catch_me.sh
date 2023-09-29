#!/bin/bash
#Bash script that makes a reques that causes server to respond with a message You got me!
curl -X GET -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
