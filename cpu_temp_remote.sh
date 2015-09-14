#!/bin/bash

core=$1
remote=$2

ssh $remote "sensors" | grep "Core ${core}" | cut -c15-22 | sed '/^$/d' | sed 's/\+//' | sed 's/\.0//'
