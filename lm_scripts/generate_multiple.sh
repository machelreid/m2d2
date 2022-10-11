#!/bin/bash

L1_list= #list of all domains
mkdir -p adapting
mkdir -p adapting/l1
mkdir -p adapting/l2
mkdir -p adapting/logs

rm adapting/L1_ft_all.sh

cat $L1_list | while IFS= read -r line;
do
	# replace placeholder from `adapt.sh`
	cat ./adapt.sh | sed "s/__FILL__/$line/g" > adapting/l1/$line"_adapt.sh"
	echo "bash $(pwd)/adapting/l1/$line""_adapt.sh" >> adapting/L1_ft_all.sh
done
