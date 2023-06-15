# Modular-exponentiation
Program for modular exponentiation

In mathematics, more specifically in modular arithmetic, modular exponentiation is a type of exponentiation (exponentiation) performed on integers modulo an integer. It is particularly used in computing, especially in the field of cryptology.

Given a base b, an exponent e and a nonzero integer m, modular exponentiation consists in calculating c such that:

     c ≡ b e ( mod m )
     0 ≤ c < m

For example, if b = 5, e = 3, and m = 13, the calculation of c gives 8.

Calculating modular exponentiation is considered easy, even when the numbers involved are huge. On the contrary, calculating the discrete logarithm (finding e from b, c and m) is recognized as difficult. This one-way function behavior makes modular exponentiation a good candidate for use in cryptology algorithms.
