# matrix_sort
Sort big matrix with Int's on python with minimal use of RAM

## How to use

1 clone repository and go to directory matrix_sort

2 run make_matrix.py to generate example CSV-file with 50k rows and 50k columns of Integer 

3 run reader.py to read CSV-file and write all Integers to interim binary file

4 use binary sort & merge by send binary stream to binary_sorter.py and sent output to next binary file with Integers sorted within as follows:
 cat binary.numbers | ./binary_sorter.py > binary.numbers.sorted

5 now we can read resulting file and write CSV-file by rows or even by columns (To be continued)

## Caveats

As we trying to use as low RAM as possible we always use smallest potion of data. Text files we read by one byte. Disadvantage is wasting too much time on big files.
Binary sort algorithm from Gvido van Rossum uses many temporary files. So you may need to adjust OpenFiles limit, use command 
```ulimit -n 262144```

