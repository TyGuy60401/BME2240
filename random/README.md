# compileFiles.py
This is a script that you can use to combine multiple output files
that you generated from subsets of your larger data. Pass in the output
txt files that were made when you ran the mass_tracker script from
the lab instructions.

To run the script simply run the compileFiles.py and pass arguments
for 
 - a folder path that contains the output data
 - an output file to be written to
 - [optional] The number of seconds between each frame.

Here is an example
```
> python compileFiles.py ./outputFiles/ ./outputFinal.txt
```

It is important that the files be named sequentially. The files are 
going to be compiled in alphabetical order ascending. For example, 
the names of the output files could be:

output1.txt
output2.txt
.
.
.

It is also important that there are no other files in the directory.

Good luck with the lab!
