# Discussion

## Why we need to use TLS here? Why don't we just use J-PAKE with AES or DES over TCP?

Imagine that we are no TLS here.
You need to establish a network protocol to transfer data.
you might use TCP or UDP.
After building channel, you need to perform J-PAKE protocol
and then encrypt/decrypt messages with the symmetric key
computed from J-PAKE.
Before encrypting, you need check the two parties have
at least one same cryptographic encryption module like AES or DES by your own.
In summary, you need to build TCP or UDP channel,
and then negotiate a encryption module for further usage.

This sounds like the __handshake__ step of TLS.

Why don't you use the built-in TLS if you already have one?

That is, TLS = (AES/DES/..) + TCP,
so, J-PAKE + (AES/DES/..) + TCP = J-PAKE + TLS

Thus, we can use the built-in TLS to establish a TCP channel
and reach an agreement on encryption module(AES/DES/...)
to transfer the encrypted messages or decrypt the received messages.
You can save the effort to do the same job as TLS handshake by your own.
TLS is well-deployed protocal. Just call it!

## Instead of PAKE, Why do we directly use shared password to authenticate each side?

The password is human-memorable weak secret.
Its bits is too short, so it will be easily cracked.

Suppose that we use the password to generate the session key directly.
If the password is fixed, it means that
all the session will use the same session key.
This is very dangerous.
If the password is leaked out, then all the sessions will be compromised.

If the password is random generated each time,
so every session will use different session key.
This indeed can avoid affecting other session
when the password is later disclosed.
However, the session whose password is disclosed is still cracked.

On the other hand, _PAKE_ protocol can generate different session keys
even if the password is fixed.
What's more, if the password is leaked out,
the established sessions and their session keys will still be safe.
The most important thing is that the session key is high-entropy,
so it's very hard to be cracked.

## When should we use J-PAKE instead of other PAKE?

If some devices are unable to operate large exponent,
the J-PAKE may be helpful.
The required bits of the used exponent in J-PAKE
is smaller than _EKE_, _SPEKE_.

However, _J-PAKE_ needs 2 rounds rather then _EKE_ and _SPEKE_
who only need one round.
Hence, if network latency is long,
then _J-PAKE_ might not be a good approach.
Otherwise, you can consider it.

## Can J-PAKE prevent all the known attacks for EKE and SPEKE?

## Can J-PAKE prevent DOS(Denial of Service) attack?

## Random Pattern Attack

Random function is pseudo, so the pattern is probably predictable.
How do it affect _EKE_, _SPEKE_, _J-PAKE_ ....

## EKE v.s. SPEKE

When to use? Which should you choose?
