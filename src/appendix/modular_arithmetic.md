# Modular Arithmetic

## Congruence Relation

If
\begin{aligned}
p \mid a - b
\end{aligned}

$$
\text{, where $a, b, p \in Z$ with $0 \leq a, b < p$}
$$

then we denote:

$$
a \equiv b \pmod p
$$

### Assumptions for Following Operations

If
$$
a \equiv b \pmod p
$$

and

$$
c \equiv d \pmod p
$$

### Addition and Subtraction

$$
a \pm c \equiv b \pm d \pmod p
$$

Proof:

We know \\( p \mid a-b \\) and \\( p \mid c-d \\), so

\begin{aligned}
a - b = mp \\\\
c - d = np
\end{aligned}

$$
\text{, where $m,n \in Z$}
$$

The above equations can be represented as:

\begin{aligned}
a = mp + b \\\\
c = np + d
\end{aligned}

Thus,

\begin{aligned}
a \pm c =& (mp + b) \pm (np + d) \\\\
        =& (m \pm n)p + (b \pm d) \\\\
        =& kp + (b \pm d)
\end{aligned}

$$
\text{, where } k \in Z
$$

and it's obviously that

$$
a \pm c \equiv b \pm d \pmod p
$$

### Multiplication

$$
a \cdot c \equiv b \cdot d \pmod p
$$

Proof:
\begin{aligned}
a - b = mp \Rightarrow a = mp + b
\end{aligned}

$$
\text{, where } m \in Z
$$

\begin{aligned}
c - d = np \Rightarrow c = np + d
\end{aligned}

$$
\text{, where } n \in Z
$$

\begin{aligned}
a \cdot c =& (mp + b) \cdot (np + d) \\\\
          =& (mnp + md + nb) \cdot p + (b \cdot d) \\\\
          =& kp + (b \cdot d)
\end{aligned}

$$
\text{, where } k \in Z
$$

Thus,

$$
a \cdot c \equiv b \cdot d \pmod p
$$

The other obvious truth is that:

\begin{aligned}
r \cdot a \equiv r \cdot b \pmod p
\end{aligned}

$$
\text{, where } r \in Z
$$

This is pretty easy to prove by:

$$
a = mp + b
$$

$$
\begin{aligned}
r \cdot a =& r \cdot (mp + b) \\\\
          =& (rm) \cdot p + r \cdot b \\\\
          =& q \cdot p + r \cdot b
\end{aligned}
$$

### Exponentiation

\begin{aligned}
a^n \equiv b^n \pmod p
\end{aligned}

$$
\text{, where } n \in Z
$$

Proof:

I. __Bottom-up Approach__

By \\( a \cdot c \equiv b \cdot d \pmod p \\)
, if we replace \\( c \\) with \\( a \\) and \\( d \\) with \\( b \\),
then

$$
a \cdot a \equiv b \cdot b \pmod p
$$

$$
\Rightarrow a^2 \equiv b^2 \pmod p
$$

Next, by replacing \\( c \\) with \\( a^2 \\) and \\( d \\) with \\( b^2 \\),
we can get

$$
a \cdot a^2 \equiv b \cdot b^2 \pmod p
$$

$$
\Rightarrow a^3 \equiv b^3 \pmod p
$$

Finally you can run to \\( a^n \equiv b^n \pmod p \\).

II. __Mathematical Induction__

Formally, we can use _mathematical induction_ to prove it.

__1. Basis__: the statement is true for \\( n = 1 \\)
because \\( a \equiv b \pmod p \\) is true.

__2. Inductive step__:
Show that if \\( n = k \\) holds, then also \\( n = k + 1 \\) holds.
Assume \\( a^k \equiv b^k \pmod p \\) is true.
By \\( a \cdot c \equiv b \cdot d \pmod p \\):

$$
a \cdot a^k \equiv b \cdot b^k \pmod p
$$

$$
\Rightarrow a^{k+1} \equiv b^{k+1} \pmod p
$$

thereby showing that indeed \\( n = k + 1 \\) holds.

## Modular Operation

Suppose that \\( a, b, p \in Z \\)

### Addition and Subtraction

$$
(a \pm b) \bmod p = (a \bmod p \pm b \bmod p ) \bmod p
$$

Proof:

Assume that
\begin{aligned}
a = mp + i \Rightarrow a \bmod p = i \\\\
\end{aligned}

$$
\text{, where } m, i\in Z \text{ and } 0 \leq i < p
$$

and

\begin{aligned}
b = np + j \Rightarrow b \bmod p = j \\\\
\end{aligned}

$$
\text{, where } n, j \in Z \text{ and } 0 \leq j < p
$$

Therefore,
$$
\begin{aligned}
(a \pm b) \bmod p &= ((m \pm n)p + (i \pm j)) \bmod p \\\\
                  &= (i \pm j) \bmod p \\\\
                  &= (a \bmod p \pm b \bmod p) \bmod p
\end{aligned}
$$

### Multiplication

$$
(a \cdot b) \bmod p = (a \bmod p \cdot b \bmod p ) \bmod p
$$

Proof:

The step is basically same as above.
First, we assume that
\begin{aligned}
a = mp + i \Rightarrow a \bmod p = i
\end{aligned}

$$
\text{, where } m, i\in Z \text{ and } 0 \leq i < p
$$

and

\begin{aligned}
b = np + j \Rightarrow b \bmod p = j
\end{aligned}

$$
\text{, where } n, j \in Z \text{ and } 0 \leq j < p
$$

Therefore,

\begin{aligned}
(a \cdot b) \bmod p &= ((mp + i) \cdot (np + j)) \bmod p \\\\
                    &= ((mnp + mj + ni)p + i \cdot j) \bmod p \\\\
                    &= (i \cdot j) \bmod p \\\\
                    &= (a \bmod p \cdot b \bmod p) \bmod p
\end{aligned}

On the other hand, another multiplication operation is:
\begin{aligned}
(x \cdot y) \bmod p = x \cdot (y \bmod p) \bmod p
\end{aligned}

$$
\text{, where } x, y \in Z
$$

This is easy to prove:

\begin{aligned}
(x \cdot y) \bmod p &= (x \cdot (mp + r)) \bmod p \\\\
                    &= (x \cdot mp + x \cdot r) \bmod p \\\\
                    &= x \cdot r \bmod p \\\\
                    &= x \cdot (y \bmod p) \bmod p
\end{aligned}

$$
\text{, where } y = mp + r, m, r \in Z \text{ and } 0 \leq r < p
$$

### Exponentiation

\begin{aligned}
a^n \bmod p = (a \bmod p)^n \bmod p
\end{aligned}

$$
\text{, where } n \in Z
$$

Proof:

I. __Mathematical Induction__

1. __Basis__: the statement is true for \\( n = 1 \\)
because \\( (a \bmod p) \bmod p \\) still equal to \\( a \bmod p \\).

2. __Inductive step__:
Show that if \\( n = k \\) holds, then also \\( n = k + 1 \\) holds.
Assume \\( a^k \bmod p = (a \bmod p)^k \bmod p \\) is true, then

\begin{aligned}
(a \cdot a^k) \bmod p &= (a \bmod p \cdot a^k \bmod p) \bmod p \\\\
                    &= (a \bmod p \cdot (a \bmod p)^k \bmod p) \bmod p \\\\
                    &= (a \bmod p \cdot (a \bmod p)^k) \bmod p \\\\
                    &= (a \bmod p)^{k+1} \bmod p
\end{aligned}

- The first equation is derived by replacing
\\( b \\) with \\( a^k \\) in \\( (a \cdot b) \bmod p = (a \bmod p \cdot b \bmod p ) \bmod p \\)
- The second equation is derived from the assumption:
\\( a^k \bmod p = (a \bmod p)^k \bmod p \\)
- The third equation is derived by replacing \\( x \\) with \\( a \bmod p \\)
and \\( y \\) with \\( (a \bmod p)^k \\) in \\( x \cdot (y \bmod p) \bmod p = (x \cdot y) \bmod p \\)

Finally, we can get:
$$
\Rightarrow a^{k+1} \bmod p = (a \bmod p)^{k+1} \bmod p
$$
thereby showing that indeed \\( n = k + 1 \\) holds.


II. __Bottom-up Approach__

By \\( (a \cdot b) \bmod p = (a \bmod p \cdot b \bmod p ) \bmod p \\),
if we replace \\( b \\) with \\( a \\), then

$$
(a \cdot a) \bmod p = (a \bmod p \cdot a \bmod p ) \bmod p
$$

$$
\Rightarrow a^2 \bmod p = (a \bmod p)^2 \bmod p
$$

Next, by replacing \\( b \\) with \\( a^2 \\), we can get:

\begin{aligned}
(a \cdot a^2) \bmod p
&= (a \bmod p \cdot a^2 \bmod p ) \bmod p \\\\
&= (a \bmod p \cdot (a \bmod p)^2 \bmod p ) \bmod p
\end{aligned}

By \\( (x \cdot y) \bmod p = x \cdot (y \bmod p) \bmod p \\),
if we put \\( a \bmod p \\) to \\( x \\) and \\( (a \bmod p)^2 \\) to \\( y \\),
then the above equation will be

\begin{aligned}
a^3 \bmod p
&= (a \cdot a^2) \bmod p \\\\
&= (a \bmod p \cdot (a \bmod p)^2 \bmod p ) \bmod p \\\\
&= (a \bmod p \cdot (a \bmod p)^2) \bmod p \\\\
&= (a \bmod p)^3 \bmod p
\end{aligned}

Again and again, you finally can run to \\( n \\) by same technique.

## Modular Multiplicative Inverse

the modular multiplicative inverse of an integer a modulo \\( p \\)
is an integer \\( a^{-1} \\) such that

$$
a \cdot a^{-1} \equiv 1 \pmod p
$$

or

$$
a \cdot a^{-1} \bmod p = 1
$$

The \\( a^{-1} \\) exists if and only if \\( a \\) and \\( p \\) are
coprime (i.e., if \\( gcd(a, p) = 1 \\)).

__Theorem.__ _Let \\( a, p \in Z \\) with \\( p > 0 \\).
Then \\( a \\) has a multiplicative inverse modulo \\( p \\)
if and only if \\( a \\) and \\( p \\) are relatively prime._

__Proof__:

First ,we prove that:
if \\( a \\) has an inverse mod \\( p \\), then \\( a \\) and \\( p \\) must be coprime.

\\( a \cdot a^{-1} \equiv 1 \pmod p \\) implies that
\\( p \mid a \cdot a^{-1} - 1 \\). Thus,

\begin{aligned}
a \cdot a^{-1} - 1 = mp
\end{aligned}

$$
\text{, where } m \in Z
$$

and it can be rewritten into

\begin{aligned}
a \cdot a^{-1} + np = 1
\end{aligned}

$$
\text{, where } n = -m
$$

Then, assume \\( s \\) is the product of all the prime factors that
\\( a \\) and \\( p \\) share, \\( s > 0 \\), which is actually the
__greatest common divisors__ of \\( a \\) and \\( p \\):

$$
s = gcd(a, p)
$$

and

\begin{aligned}
a = s \cdot x
\end{aligned}

$$
\text{, where } x \in Z
$$

\begin{aligned}
p = s \cdot y
\end{aligned}

$$
\text{, where } y \in Z
$$

Therefore,

\begin{aligned}
a \cdot a^{-1} + n \cdot p
&= (s \cdot x) \cdot a^{-1} + n \cdot (s \cdot y) \\\\
&= s \cdot (x \cdot a^{-1} + n \cdot y) \\\\
&= 1
\end{aligned}

and we get:

$$
x \cdot a^{-1} + n \cdot y = \frac{1}{s}
$$

The left side \\( x \cdot a^{-1} + n \cdot y \\) is the sum of products of integers,
so it must be an integer.
Thus, the right side \\( \frac{1}{s} \\) must also be an integer.
We have only two choices: \\( s = \pm 1 \\).
However, \\( s > 0 \\), so \\( s = 1 \\).

Finally, we can know that:
_If \\( a \\) has an inverse mod \\( p \\), then \\( a \\) and \\( p \\) must be coprime._

Second, we prove that:
if \\( a \\) and \\( p \\) is coprime, then \\( a \\) has an inverse mod \\( p \\).

From [Bézout's identity](gcd.md):

$$
ax + py = gcd(a, p) = 1
$$

Thus,

$$
ax \equiv 1 \pmod p
$$

The \\( x \\) here is actually the \\( a^{-1} \\).


## References

- [KHANacademy: What is modular arithmetic](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
