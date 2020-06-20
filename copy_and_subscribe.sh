#!/bin/bash
# Cygwin
#cat $1 > /dev/clipboard
# WSL
cat $1 | clip.exe
echo "copy succeeded"
