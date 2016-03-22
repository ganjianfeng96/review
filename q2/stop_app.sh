#!/bin/sh -f
ps aux | grep pri_handler | grep -v grep | awk '{print $2}' > 1
for i in `cat 1`;do kill -9 $i;done
echo "you killed the processid $i"

