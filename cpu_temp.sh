#!/bin/bash

core=$1

sensors | grep "Core ${core}" | cut -c16-22 | sed '/^$/d' | sed 's/\+//' | sed 's/\.0/c/'
