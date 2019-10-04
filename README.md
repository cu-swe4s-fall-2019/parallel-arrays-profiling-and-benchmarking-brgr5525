# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

Make sure that you have matplotlib installed:
```
$ conda install --yes matplot lib
```

## updates
- created the plot_gtex.py script that creates a boxplot of gene read counts
  for given information and gene
- used linear and binary search to profile the performance of the two methods
- updated data_viz to plot multiple boxplots as well as take user input to
  assign title and labels
- added unit and functional testing for plot_gtex script

## calls to program
The main script should be run with the arguments as follows:
```
$ python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.png
```

For explanations on parameters run:
```
$ python plot_gtex.py -h
```

## profiling
Using cProfile we are able to see how long a program took to run and how much
of that time was spent on certain functions or calls.

This allows us to see what parts of a script are consuming the most time.

In this instance, we can see that linear search is what is causing the script
to run for a marked amount of time.

(For the full profiles on both search methods see plot_gtex.linear_search.txt
and plot_gtex.binary_search.txt)

Linear Search:
```
707617 function calls (700695 primitive calls) in 13.677 seconds

Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
45904   12.919    0.000   12.923    0.000 plot_gtex.ls.py:8(linear_search)
```

## benchmarking
Benchmarking can then be used to show the difference in runtimes between
different methods.

Using python's ```time``` function, we can mark how long each a script spends
on certain parts of our program.

Linear Search:
```
Time searching = 12.927680015563965
Total time = 13.151285171508789
```

Binary Search:
```
Time sorting = 0.0016019344329833984
Time searching = 0.0730128288269043
Total time = 0.2862279415130615
```

This shows us how much of an improvement binary search makes in our script.
Binary search is performing roughly much better with the program 177 times
less time searching. And even though we must spend time sorting our list that
is to be run through a binary search, together the operations take only a fraction
of the time needed to use linear search.
