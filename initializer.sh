#!/usr/bin/bash
problem='A B C D E F'

for n in $problem
do
	script=./$n.py
	if [ ! -f $script ]
	then
		cp ../initial.py ./$n.py
	fi
done

cp ../lib.py ./lib.py
