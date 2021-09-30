#!/bin/bash
problem='a b c d e f g h'
for n in $problem
do
	script=./$n.py
	if [ ! -f $script ]
	then
		cp ../py_initial.py ./$n.py
	fi
done
