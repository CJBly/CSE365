#!/bin/bash

while true; do
    timeout 1 nc '10.0.0.2' 31337 &
    sleep 0.0001
done
