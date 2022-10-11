# cat domains.txt | while read line || [[ -n $line ]];
line=$1
# do
echo $line
rm -r "$line/SPLIT" 2> /dev/null
mkdir -p "$line/SPLIT"
for i in $(find $line -type l -name "VALID__*txt" | shuf); do cat $i >> $line/SPLIT/eval.txt;done
shardize "$line/SPLIT/eval.txt" 2 "$line/SPLIT"
mv "$line/SPLIT/eval.txt_sharded.0" "$line/SPLIT/valid.txt"
mv "$line/SPLIT/eval.txt_sharded.1" "$line/SPLIT/test.txt"
rm "$line/SPLIT/eval.txt_sharded.2" 2> /dev/null
for i in $(find $line -type l -name "*txt" | grep -v "VALID__");do cat $i >> $line/SPLIT/train.txt; done 
# done
# wait
