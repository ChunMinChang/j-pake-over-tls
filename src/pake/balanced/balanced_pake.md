# Balanced PAKE

_Balanced PAKE_ satisfy all the [security requirements][sec] and
allow parties to negotiate with each other to get a same shared key
for encryption by some magic mathematical computation based on
their common knowledge of a same __password__.
It prevents messages from being eavesdropped and tampered,
so we can keep the secrecy and integrity of the transmitted data.

We will next introduce two of most well-known protocol of _Balanced PAKE_,
_EKE_ and _SPEKE_.

## EKE: Encrypted Key Exchange

[_Encrypted Key Exchange_][steven_michael], often abbreviated to _EKE_,
is invented by _Steven M. Bellovin_ and _Michael Merritt_ in 1992,
when they worked in AT&T Bell Laboratories.

In general forms of _Encrypted Key Exchange_,
at least one engaging parties will use the common password with a random number
to generate a ephemeral (one-time) public key, and sends it to another party,
who can use this received ephemeral public key to generate another public key
to send to the next party or send it back to the first one.
After one or more rounds of the exchange of the one-time public keys,
the engaging parties can use them with the common password
to generate a shared key for encryption.

## SPEKE: Simple Password Exponential Key Exchange

[_Simple Password Exponential Key Exchange_][D_Jablon],
often abbreviated to _SPEKE_
is proposed by _David P. Jablon_ in 1996.
The protocol is almost same as [_Diffie-Hellman Key Exchange_][dh],
except the group generate is derived from the password.

## References

- [CryptoWiki: Encrypted Key Exchange][eke]
- [Wiki: Encrypted key exchange][eke_wiki]
- [Authenticated Key Exchange with SPEKE or DH-EKE][dheke_speke]
- [Encrypted Key Exchange: Password-based Protocols Secure Against Dictionary Attacks][steven_michael]
- [Strong Password-Only Authenticated Key Exchange][D_Jablon]

[sec]: ../security_requirements.md "Security Requirements"
[pake]: http://cryptowiki.net/index.php?title=Password-authenticated_key_agreement "Password-authenticated key agreement"
[eke]: http://cryptowiki.net/index.php?title=Encrypted_Key_Exchange "CryptoWiki: Encrypted Key Exchange"
[eke_wiki]: https://en.wikipedia.org/wiki/Encrypted_key_exchange "Wiki: Encrypted key exchange"
[dheke_speke]: http://www.themccallums.org/nathaniel/2014/10/27/authenticated-key-exchange-with-speke-or-dh-eke/ "Authenticated Key Exchange with SPEKE or DH-EKE By Nathaniel McCallum"
[steven_michael]: https://www.cs.columbia.edu/~smb/papers/neke.pdf "Encrypted Key Exchange: Password-based Protocols Secure Against Dictionary Attacks"
[D_Jablon]: http://www.jablon.org/jab96.pdf "Strong Password-Only Authenticated Key Exchange"
[dh]: ../../appendix/dh/dh.md "Diffie-Hellman Key Exchange"
