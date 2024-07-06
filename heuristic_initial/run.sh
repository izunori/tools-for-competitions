if [ $# == 1 ]
then
    INPUT=$1
    cp ${INPUT} ./input.txt
else
    INPUT="./input.txt"
fi
#pypy3 ./a.py < ${INPUT} > result.txt
./out < ${INPUT} 2>&1 |tee  result.txt

#cat ./result.txt | /mnt/c/WINDOWS/system32/clip.exe
grep -v '#' ./result.txt | /mnt/c/WINDOWS/system32/clip.exe
#grep -v '#' ./result.txt | iconv -f ISO2022JP -t UTF-16le | /mnt/c/WINDOWS/system32/clip.exe

