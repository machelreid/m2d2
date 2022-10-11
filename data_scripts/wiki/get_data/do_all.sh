parallel --jobs 80 --bar "python fix_stuff.py {} $HOME/storage/all_wikipedia_files" :::: all_wiki_stuff.txt 

