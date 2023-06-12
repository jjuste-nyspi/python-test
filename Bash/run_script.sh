#!/bin/bash
python3 $1 $2

python_status=$?

current_date=`date "+%D %T"`

msg="A script has ran to error:

Server"