#!/bin/bash
for i in $(seq 0 255); do
  echo "Pinging 10.0.0.$i"
  timeout 1 ping -c 1 10.0.0.$i &> /dev/null && echo "Host 10.0.0.$i is up"
done
