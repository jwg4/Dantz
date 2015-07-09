# Dantz
This is a reference implementation of the 'Dancing Links' algorithm from Knuth's paper of the same name:
http://arxiv.org/abs/cs/0011047

The algorithm searches for solutions to the 'exact cover problem' and prints them all out. It does not use the optimization of taking at each stage the column with the smallest number of rows.

To build with Visual Studio 2013, load the solution file. To build with gcc:

    cd Dantz
    make

