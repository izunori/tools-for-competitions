has_comment=$#

echo ${has_comment}

if [ $# -eq 0 ]
then
    pahcer run --no-result-file --freeze-best-scores | tee ./plog.log
else
    pahcer run -c "$1" | tee ./plog.log
    python3 ./copy_best.py
    cp -r ./best ~/d/atcoder/ahc061
    cp -r ./tools/out ~/d/atcoder/ahc061
fi
