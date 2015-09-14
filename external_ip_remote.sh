#!/bin/bash

remote=$1

ssh $remote "curl icanhazip.com 2>/dev/null"
