Task2:

-	How big is the dataset?

the size of the file is 4.7 MB  **(ls -lh)** \
there are 36860 lines **(wc -l clean_dialog.csv)**

-	What’s the structure of the data? (i.e., what are the field and what are values in them)

it's a csv file with 4 cols: "title","writer","pony","dialog" **(head -n 1 clean_dialog.csv)** \

-	How many episodes does it cover?
there are 196 episode names \
(**cut -d, -f1 clean_dialog.csv | tail -n +2 | uniq | wc -l** \
cut -d, -f1 : to filter the first col \
clean_dialog.csv: name of the file \
tail -n +2 : last line is just the header of the col in this case "title" \
uniq: to ignore repitition \
wc -l: to count the number of lines )

-	During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.

By checking the names of the ponies in the third col basically we should be able to have a clean set of data with the name of the pony we want to analize but using (**cut -d, -f3 clean_dialog.csv | tail -n +2 | sort | uniq** ) we can clearly see that the data is not really clear cut, in some cases the names are accompnied with other names sometimes the names are abrrivated or accompanied by an adjective or for example it's just called all, who is all?

