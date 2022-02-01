# PAKE: Password Authenticated Key Exchange

_Password-Authenticated Key Exchange_ is a protocol for multiple parties
to establish a shared cryptographic keys
based on their same knowledge of a __password__.
All parties can compute the exactly same result
from the password and the public messages exchanged among them.
The unauthorized party who doesn't possess the password has no way
to get the password from the communication channel.
With the password, there is no need for a trusted third party
like _public key infrastructure_(PKI) for authentication.

_PAKE_ prevents attacks from an eavesdropper or man-in-middle.
The attackers are unable to guess the password
without interaction with engaging parties.
It can use weak __human-memorable__ passwords to generate
a high-entropy strong key to encrypt/decrypt,
so it's very convenient in use and widely deployed
in many commercial applications today.

## Applications

- __Mutual authentication by low-entropy passwords__:
_PAKE_ can generate a high-entropy cryptographically strong key from
low-entropy passwords for engaging parties to authenticate mutually.
- __Alternative for computationally expensive authentication__:
For low-end devices, it's computationally expensive to use asymmetric encryption
like _RSA_. It would be easy to use a simple symmetric encryption protocol
like _pake_ to do it.

## PAKE Family

There are so many _PAKE_ protocol had been proposed.
In our content, only two protocols will be mentioned.
One is _Balanced PAKE_, and the other is _Augmented PAKE_.

Overview of _PAKE_ family we will mention:

- Balanced PAKE
  - EKE: Encrypted Key Exchange
    - DH-EKE: Diffie-Hellman Encrypted Key Exchange
  - SPEKE: Simple Password Exponential Key Exchange
  - J-PAKE: Password Authenticated Key Exchange by Juggling
- Augmented PAKE
  - SRP: Secure Remote Password protocol

## Goal of PAKE

Establish a shared key among devices for encryption without PKI

## Diffie-Hellman Key Exchange

Many protocols of _PAKE_ are variant of [_Diffie-Hellman Key Exchange_][dh].
In order to understand the _balance PAKE_ such as _DH-EKE_, _SPEKE_,
or the _augmented PAKE_ such as _SRP_, the first thing you need to do is to
understand the underlying [_Diffie-Hellman Key Exchange_][dh].
For those who don't know it, please read [_Diffie-Hellman Key Exchange_][dh]
in appendix. If you are already familiar with it, just skip it
and keep on reading.

## References

- [Password-authenticated key agreement][pake]

[pake]: http://cryptowiki.net/index.php?title=Password-authenticated_key_agreement "Password-authenticated key agreement"
[dh]: ../appendix/dh/dh.md "Diffie-Hellman Key Exchange"
