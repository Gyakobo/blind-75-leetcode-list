# Rotate a Matrix by 90 degrees

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

### Methodology

1. Before we even get to the code let's consider the following matrix:
$
A = 
\left(\begin{array}{cc} 
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{array}\right)
$ 

2. To rotate this matrix you to do the following:
* Reverse the order of columns: $A_{j} \rightarrow A^\prime_{j}$
* Transpose the matrix: $A^\prime_{ij} \rightarrow A^\prime_{ji}$

3. In particular here is a mathematical representation:
$$
A = 
\left(\begin{array}{cc} 
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{array}\right)
$$ 

$$
A^\prime \rightarrow 
\left(\begin{array}{cc} 
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{array}\right)^T
\left(\begin{array}{cc} 
0 & 0 & 1\\
0 & 1 & 0\\
1 & 0 & 0\\
\end{array}\right) \rightarrow
\left(\begin{array}{cc} 
1 & 4 & 7\\
2 & 5 & 8\\
3 & 6 & 9\\
\end{array}\right)
\left(\begin{array}{cc} 
0 & 0 & 1\\
0 & 1 & 0\\
1 & 0 & 0\\
\end{array}\right) \rightarrow
\left(\begin{array}{cc} 
7 & 4 & 1\\
8 & 5 & 2\\
9 & 6 & 3\\
\end{array}\right)
$$ 
