# J-PAKE: Password Authenticated Key Exchange by Juggling Without PKI

__Password Authenticated Key Exchange by Juggling(J-PAKE)__
is a _password-authenticated key agreement(PAKE)_ protocol
without requiring __Public Key Infrastructure(PKI)__ for authentication.
_J-PAKE_ is able to establish a private and authenticated channel
on top of an insecure network solely based on a shared password.

## Why we need J-PAKE

- EKE may leak partial information about password to a passive attacker
- SPEKE allows an active attacker to test multiple password
in one protocol execution
- They are both patented

## Applications

- Firefox Sync ([removed after 2015](https://blog.mozilla.org/services/2014/04/30/firefox-syncs-new-security-model/))
- OpenSSH and OpenSSL ([removed after 2014](http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/Attic/jpake.c))
- [Thread][thread] (IoT wireless network protocol)
- Palemoon sync (forked from Firefox)

## Zero-Knowledge Proof

_J-PAKE_ use [_Zero-Knowledge Proof_][zkp] to produce valid knowledge proof
of a discrete logarithm without revealing it.
One example is to use [Schnorr digital signature][ss],
which is a non-interactive protocol.

## What is the group used in J-PAKE?

- [Multiplicative group of integers modulo n][int_group]
- [Elliptic Curve Group][ec]

## References

- [Password Authenticated Key Exchange by Juggling][jpake_wiki]
- [J-PAKE: Authenticated Key Exchange Without PKI][jpake_FHao_PRyan]

[thread]: http://threadgroup.org/ "Thread"
[zkp]: ../../../appendix/zkp/zkp.md "Zero-Knowledge Proof"
[ss]: ../../../appendix/zkp/schnorr_signature.md "Schnorr signature"
[int_group]: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n "Multiplicative group of integers modulo n"
[ec]: https://en.wikipedia.org/wiki/Elliptic_curve#The_group_law "Elliptic Curve Group Law"
[jpake_wiki]: https://en.wikipedia.org/wiki/Password_Authenticated_Key_Exchange_by_Juggling "Password Authenticated Key Exchange by Juggling"
[jpake_FHao_PRyan]: http://eprint.iacr.org/2010/190.pdf "J-PAKE: Authenticated Key Exchange Without PKI"
