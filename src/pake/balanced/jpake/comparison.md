# Comparison

J-PAKE scheme looks too computationally expensive,
but actually it's not.

| Item | Description                                                                          | No of Exp |
| ---- | ------------------------------------------------------------------------------------ | --------- |
| 1    | Compute g<sup>x1</sup>, g<sup>x2</sup> and ZKPs for { x<sub>1</sub>, x<sub>2</sub> } | 4         |
| 2    | Verify ZKPs for { x<sub>3</sub>, x<sub>4</sub> }                                     | 4         |
| 3    | Compute A and ZKP for { x<sub>2</sub> • s }                                          | 2         |
| 4    | Verify ZKP for { x<sub>4</sub> • s }                                                 | 2         |
| 5    | Compute K                                                                            | 2         |
|      | Total                                                                                | 14        |

Recall that [_EKE_][eke] and [_SPEKE_][speke] use only 2 exponentiations
compared with 14 exponentiations in [_J-PAKE_][jpake],
we might think _J-PAKE_ is computationally expensive.
However, both _EKE_ and _SPEKE_ must use __long exponents__.
One typical exponentiation in _EKE_ or _SPEKE_ is equivalent
in cost 6-7 exponentiation in _J-PAKE_.
Hence, overall computational costs for _EKE_, _SPEKE_, and _J-PAKE_
are actually about the same.

## Why can J-PAKE use short exponents?

You must be curious about why _J-PAKE_ can use short exponents.
The basic pattern of the [_PAKE family_][pake] are exactly __same__.
They all choose a secret number \\( x \\) as a _private key_ and
generate a _public key_ \\( g^x \\) with the _group generator_ \\( g \\).

From the aspect of probability, the reason of
why _J-PAKE_ can achieve same security as _EKE_ and _SPEKE_ is that
it decomposes the probability of cracking one _private key_ into
several probabilities of cracking several _private keys_.

Suppose the _EKE_ or _SPEKE_ use a 4-bits group modulo \\( p \\),
then its used _private key_ must also be 4-bits.
Therefore, there are \\( 2^4 = 16 \\) possible choices for the _private key_.
To crack one _PAKE_ session channel,
the attacker needs to hit not only Alice's _private key_, but also Bob's one.
Thus, the probability of hitting the private keys of both sides is
\\( \frac{1}{16} \cdot \frac{1}{16} = \frac{1}{256} \\).
However, _J-PAKE_ can reach the same probability by
using only 2-bits group modulo \\( p \\).
_J-PAKE_ uses __2 exponents__ per session on each side.
Consequently, it will produce 2 _private keys_ on each side
in one protocol execution.
That is, Alice and Bob will have \\( 2^2 = 4 \\) choices
for one 2-bits _private key_.
To establish one _J-PAKE_ session,
both Alice and Bob will have \\( 4 \cdot 4 = 16 \\)
possible combinations for two random _private keys_.
Thus, there are \\( 16 \cdot 16 = 256 \\) possible combinations for
Alice and Bob's _private keys_.
Then the probability to compromise a _J-PAKE_ session is \\( \frac{1}{256} \\).
And that's why _J-PAKE_ can achieve the same security as _EKE_ and _SPEKE_.

Formally, assume that \\( u, v \\) are the probabilities
to crack one _private key_ of respectively _EKE_/_SPEKE_ and _J-PAKE_.
Then to find a \\( v \\) such that \\( u^2 = v^4 \\) can guarantee that
_J-PAKE_ has same security level as _EKE_ and _SPEKE_.
That is, if we use \\( i \\) bits _private key_ for _EKE_ or _SPEKE_,
To achieve same security level,
we must use \\( j \\) bits _private key_ for _J-PAKE_ such that

$$
\begin{aligned}
u &= \frac{1}{2^i} \\\\
v &= \frac{1}{2^j} \\\\
u^2 &= v^4 \\\\
\Rightarrow (\frac{1}{2^i})^2 &= (\frac{1}{2^j})^4 \\\\
\Rightarrow \frac{1}{2^{2i}} &= \frac{1}{2^{4j}} \\\\
\Rightarrow 2^{2i} &= 2^{4j} \\\\
\Rightarrow j &= \frac{i}{2}
\end{aligned}
$$

Thus, _J-PAKE_ can only use half bits of _EKE_ or _SPEKE_
to keep the channel secret.

[pake]: ../../pake.md "PAKE: Password Authenticated Key Exchange"
[eke]: ../dh-eke.md "Diffie-Hellman Encrypted Key Exchange"
[speke]: ../speke.md "Simple Password Exponential Key Exchange"
[jpake]: intro.md "J-PAKE: Password Authenticated Key Exchange by Juggling Without PKI"
