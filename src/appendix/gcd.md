# Greatest Common Divisors

If \\( a, b \in Z \\) with \\( a, b \neq 0 \\), then the largest positive integer
which divides both \\( a \\) and \\( b \\) is the __greatest common divisor__
of two integers \\( a \\) and \\( b \\). It is denoted \\( gcd(a, b) \\).
By convention, we define \\( gcd(0, 0) = 0 \\).
For some special case: \\( gcd(0, x) = x \\), where \\( x \in Z \\).
It's obvious because \\( 0 = 0 \cdot x \\).

## Bézout's Lemma

Let \\( a, b \in Z \\) with \\( a, b \neq 0 \\), then
there exist integers \\( s \\) and \\( t \\) such that \\( as + bt = gcd(a,b) \\).
That is, \\( gcd(a, b) \\) is a linear combination of a and b.

$$
\exists s,t \in Z: as + bt = gcd(a,b)
$$

__Proof__

Consider the set
$$
S = {ax + by : x, y \in Z} \cap (N \backslash \{0\})
$$
or
$$
S = {ax + by : x, y \in Z \text{ and } ax + by > 0}
$$

\\( S \\) is definitely non-empty set.
Take \\( x = a, y = b \\), then \\( k = a \cdot a + b \cdot b > 0 \\)
because \\( a, b \neq 0 \\). So, \\( k \in S \\) and \\( S \neq \emptyset \\).

Since \\( S \\) is a nonempty subset of \\( N \\),
\\( \{S \neq \emptyset \} \cap \{S \subseteq N\} \\),
there is a _least element_ by the __Well-Ordering Principle__,
which we denote by \\( d \\).

Then there exist integers \\( x_0, y_0 \\) such that
$$
d = a \cdot x_0 + b \cdot y_0
$$
, \\( d \\) is the minimal positive integer in \\( S \\).

By Division Algorithm, we assume that
\begin{aligned}
a = q_a \cdot d + r_a
\end{aligned}
$$
\text{, where } q_a, r_a \in Z, q_a \text{ is the quotient and } 0 \leq r_a < d
$$

and

\begin{aligned}
b = q_b \cdot d + r_b
\end{aligned}
$$
\text{, where } q_b, r_b \in Z, q_b \text{  is the quotient and } 0 \leq r_b < d
$$

From above, we can get:

\begin{aligned}
r_a &= a - q_a \cdot d \\\\
    &= a - q_a \cdot (a \cdot x_0 + b \cdot y_0) \\\\
    &= a(1 - q_a \cdot x_0) + b(-q_a \cdot y_0)
\end{aligned}

Thus, \\( r_a \\) is a linear combination of \\( a \\) and \\( b \\).
If \\( r_a > 0 \\), then \\( r_a \in S \\), and since \\( r_a < d \\),
it means that there is a element \\( r_a \\) in \\( S \\) smaller than \\( d \\).
We have a __contradiction__ that \\( d \\) is NOT the least element of \\( S \\).

Thus, \\( r_a \\) must be \\( 0 \\), and it means that \\( a = q_a \cdot d \\), so \\( q_a \mid a \\).
In same manner, we can know \\( b = q_b \cdot d \\) and \\( q_b \mid b \\).

Therefore, \\( d \\) is a common divisor of \\( a \\) and \\( b \\).

Next, we will show \\( d \\) is the greatest common divisor of \\( a \\) and \\( b \\).

Let \\( c \\) is another positive common divisor of \\( a \\) and \\( b \\),
\\( c \mid a \\) and \\( c \mid b \\).

Then,

\begin{aligned}
d &= a \cdot x_0 + b \cdot y_0 \\\\
  &= c \cdot m \cdot x_0 + c \cdot n \cdot y_0 \\\\
  &= c \cdot (m \cdot x_0 + n \cdot y_0) \\\\
  &= c \cdot z \\\\
\end{aligned}

$$
\text{, where $m = \frac{a}{c}, n = \frac{b}{c}$ }
\text{ and z is a positive integer(because c, d > 0) }
$$

Thus, we can know \\( c \mid d \\) and \\( c \leq d \\).

In summary,  
1. \\( d \\) is a common divisor of \\( a \\) and \\( b \\)
2. Every positive common divisor of \\( a \\) and \\( b \\), \\( c \\),
can divide \\( d \\).

Therefore,
$$
d = gcd(a, b)
$$

Finally, we prove that:
there exist integers \\( s, t \\) such that \\( d = as + bt = gcd(a, b) \\).

## References

- https://www.math.byu.edu/~bakker/M290/Lectures/Lec30.pdf
- https://math.berkeley.edu/~sagrawal/su14_math55/notes_gcd.pdf
