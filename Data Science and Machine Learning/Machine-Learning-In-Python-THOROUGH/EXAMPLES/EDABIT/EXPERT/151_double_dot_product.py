"""
https://edabit.com/challenge/38SP9cjt6BfRbLowA    EXPERT

Double Dot Product
In this challenge, you'll write a function that calculates the double dot product of a pair of dyadics. What's a dyadic? And what's the double dot product?

First, let's talk about (Euclidean) vectors. A vector is a geometric object. Its existence doesn't depend on the choice of the coordinate system, or indeed on choosing a coordinate system at all!

But coordinate systems are useful, and in particular, it's often convenient to represent a vector as a matrix of its Cartesian components, either a single column or a single row. We'll use the notation [v] to indicate the column-matrix representation of a vector v (called a column-vector). To indicate its row-matrix representation (called a row-vector), we'll use the transpose and write [v]ᵀ.

(We'll work only in three-dimensional space, so each vector has three Cartesian components: x, y, and z.)

If we matrix-multiply a row-vector with a column-vector (in that order), the result is a 1-by-1 matrix whose single element is the dot product of the two vectors:

a • b = Tr([a]ᵀ[b])
(where we've used the trace). Note that the dot product is commutative (i.e., a • b = b • a).

If we matrix-multiply in the opposite order (column-vector first), the result is a 3-by-3, the matrix representation of a geometric object called a dyad. To notate the dyad formed by vectors a and b, we'll write ab, and we'll notate its matrix-representation [ab]. So:

[ab] = [a][b]ᵀ
Note that unlike the dot product, the dyadic product is not commutative, and in fact:

[ab] = [ba]ᵀ
Now we can talk about dyadics. Dyadics are dyads and sums of dyads. Every dyadic can be represented as a square-matrix of its 9 components. For example, the dyadic (ab + cd):

[ab + cd] = [ab] + [cd] = [a][b]ᵀ + [c][d]ᵀ
The double dot product of a pair of dyadics is an operation that outputs a scalar (a number). For a pair of dyads, it's defined like this:

(ab):(cd) = (a • c)(b • d)
This definition can be extended to arbitrary dyadics by putting the dyadics in sum-of-dyads form and distributing:

(ab + cd):(ef + gh) = (ab):(ef) + (ab):(gh) + (cd):(ef) + (cd):(gh)
Your task is to write a function that takes as parameters the 3-by-3 matrix-representations of a pair of dyadics (each will be a two-dimensional list with numbers for elements) and returns their double dot product (as a number).

The hard part here isn't the coding so much as it is coming up with a matrix-representation of the double dot product that works for arbitrary dyadics. (You might be able to arrive at the answer by trial and error, but try to work it out mathematically!) If you're stuck, see the Comments for a hint.

Examples
double_dot(
  [
    [265, -385, -115],
    [-741, -148, 916],
    [235, -410, 433]
  ],
  [
    [440, -359, 453],
    [-453, -254, 169],
    [-314, 403, -331]
  ]
) ➞ 348446
double_dot(
  [
    [709, -422, 612],
    [761, 495, 852],
    [-473, 614, 443]
  ],
  [
    [-305, 345, 858],
    [931, -747, -422],
    [855, -156, 109]
  ]
) ➞ -309469
double_dot(
  [
    [-545, -641, -533],
    [130, 871, 699],
    [712, -375, 164]
  ],
  [
    [157, -647, -631],
    [381, -956, -223],
    [878, -589, -155]
  ]
) ➞ 547053
Notes
There's a second species of double dot product, which for dyads is defined like this:
(ab) • • (cd) = (a • d)(b • c)
Dyadics aren't used very often these days. In the more powerful framework of tensor analysis, dyadics are contravariant rank-2 tensors, the dyadic product is a special case of the tensor product, and both species of double dot product are tensor contractions (as is the normal dot product between vectors, by the way).
"""
def double_dot(d1, d2):
	return sum(d1[i][j]*d2[i][j] for i in range(3) for j in range(3))

double_dot(
  [
    [-545, -641, -533],
    [130, 871, 699],
    [712, -375, 164]
  ],
  [
    [157, -647, -631],
    [381, -956, -223],
    [878, -589, -155]
  ])