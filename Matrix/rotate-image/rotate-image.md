# Rotate a Matrix by 90 degrees

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

This [README](https://github.com/Gyakobo/blind-75-leetcode-list/blob/main/Matrix/rotate-image/rotate-image.md) serves as an explanation for how to rotate a matrix by 90 degrees.

### Methodology

1. Let's consider the following matrices:

$$
A = 
\left(\begin{array}{cc} 
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{array}\right)
$$ 

$$ 
B = 
\left(\begin{array}{cc} 
7 & 4 & 1\\
8 & 5 & 2\\
9 & 6 & 3\\
\end{array}\right)
$$ 

> Our aim is to basically convert matrix A into B - short and simple

2. To rotate this matrix you to do the following:
* Reverse the order of columns: $$A_{j} \rightarrow A^\prime_{j}$$
* Transpose the matrix: $$A^\prime_{ij} \rightarrow A^\prime_{ji}$$

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
