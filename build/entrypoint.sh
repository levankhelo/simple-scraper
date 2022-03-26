#!/bin/bash

if [[ $(ps -a | grep chromedriver | wc -l) -lt 1 ]]; then 
    # echo "STARTING WEB DRIVER"
    # chromedriver; 
    echo;
fi

echo "display: $DISPLAY"

cd /etc/app
python3 main.py
echo ------------;
echo "waiting for $(cat /etc/app/sleep_time)"
sleep $(cat /etc/app/sleep_time)
bash /entrypoint.sh