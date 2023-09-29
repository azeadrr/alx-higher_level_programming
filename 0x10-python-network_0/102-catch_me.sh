#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL -X PUT -H 'You got me!' 0:5000/catch_me_3
