#/bin/bash

echo "@profile" > ./line_temp.py
echo "def line_prof():" >> ./line_temp.py
sed 's/^/    /g' $1 >> ./line_temp.py
echo "line_prof()" >> ./line_temp.py

kernprof -l -v line_temp.py



