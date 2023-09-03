mkdir -p "./log"
if [ $# == 1 ]
then
    DIR=$1
else
    DIR="./in_0000"
fi
echo target: ${DIR}
echo "input,score" > ./all_result.csv
parallel_run() {
    echo $1.txt
    ./out < ./$2/$1.txt > ./log/$1.log
}
#for num in $(seq -w 0 99)
#do
#    num="00${num}"
#    input=${DIR}/0$num.txt
#for input in $(ls ${DIR}/*.txt)
#do
    #pypy3 ./a.py < ${input} > ./result.txt
    #./run.sh ${input} > /dev/null
#    ./run.cpp.sh ${input} > /dev/null
#    D=$(head -n1 ${input})
#    SCORE=$(tail -n1 ./result.txt | sed 's/^.*://g')
#    TXT="${input},${D},${SCORE}"
#    echo ${TXT}
#    echo ${TXT} >> ./all_result.csv
#done

export -f parallel_run
seq -f "%04g" 0 99 | xargs -I@ -P4 -n1 bash -c "parallel_run @ ${DIR}"

for num in $(seq -f "%04g" 0 99)
do
    num="${num}"
    input=${DIR}/${num}.txt
    grep ':' ./log/${num}.log > log_short.log
    SCORE=$(tail -n1 ./log_short/${num}.log | sed 's/^.*://g')
    TXT="${input},${SCORE}"
    echo ${TXT}
    echo ${TXT} >> ./all_result.csv
done

sum=$(awk -F, '{sum+=$2} END {print sum}' ./all_result.csv)
echo ",sum, ${sum}"
echo ",sum,${sum}" >> ./all_result.csv

cat ./all_result.csv | clip.exe
