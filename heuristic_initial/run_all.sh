mkdir -p "./log"
if [ $# == 1 ]
then
    DIR=$1
else
    DIR="./in_0000"
fi
echo target: ${DIR}
#echo "input,N,D,Q,score" > ./all_result.csv
echo "diff,score" > ./all_result.csv
parallel_run() {
    FILE=$1
    echo ${FILE}
    NUM=${FILE:10:4}
    ./out < $1 > ./log/${NUM}.log
}

export -f parallel_run
#seq -f "%04g" 0 ${MAX} | xargs -I@ -P4 -n1 bash -c "parallel_run @ ${DIR}"

ls -1 ${DIR}/*.txt | xargs -I@ -P10 -n1 bash -c "parallel_run @ ${DIR}"

MAX=99
#ORDER=$(cat ./order.txt)
#for LOG in ${ORDER}
for num in $(seq -f "%04g" 0 ${MAX})
do
    LOG=./log/${num}.log
    #TXT=${INPUT},$(python3 ./getLogInfo.py ./log/${num}.log N D Q score)
    TXT=$(python3 ./getLogInfo.py ${LOG} diff score)
    echo ${LOG},${TXT}
    echo ${TXT} >> ./all_result.csv
done

sum=$(awk -F, '{sum+=$NF} END {print sum}' ./all_result.csv)
diff=$(awk -F, '{sum+=$1} END {print sum}' ./all_result.csv)
echo "${diff},${sum}"
echo "${diff},${sum}" >> ./all_result.csv

cat ./all_result.csv | clip.exe
