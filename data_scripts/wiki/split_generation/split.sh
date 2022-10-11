parallel --jobs 80 --bar "bash split_one.sh {}" :::: domains.txt
