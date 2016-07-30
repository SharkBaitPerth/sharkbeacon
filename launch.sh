#!/bin/bash
# Because error handling is boring...
while [ 1 ]; do
  /usr/bin/python /opt/sharkbeacon/beacon.py
  sleep 1
done
