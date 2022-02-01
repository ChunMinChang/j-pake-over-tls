
# J-PAKE over TLS

This is a short introduction of building a secure channel between devices.

## Motivation

The motivation to write this is to note:
How to build secure channels between devices?

We encounter this problem when doing work for Firefox OS:
> How to build a secure channel between Firefox Android and Firefox OS TV?

To make Firefox Android as a remote controller of Firefox OS TV,
building a secure channel is definitely the first step to do.
However, the Firefox Android and Firefox OS TV are all in local network,
which has no any __Public Key Infrastructure(PKI)__ there,
so it's impossible to use standard __TLS__ and __https__
to build our connection.

To overcome this problem, we introduce a method, __J-PAKE over TLS__,
as our solution.

In brief, we want to use [TLS](tls/tls.md),
but we don't have a PKI in local network.
The solution we propose here is:

1. Build a confidential connection without authentication
2. Use __PAKE__ to authenticate the devices

### Demo

[![FxOS Remote Control][RemoteControlImg]][RemoteControlURL]

## J-PAKE: Password Authenticated Key Exchange by Juggling

__Password Authenticated Key Exchange by Juggling(J-PAKE)__
is a __password-authenticated key agreement__ protocol
with __Zero-Knowledge Proof(ZKP)__ mechanism.
By authenticating the preestablished password on both side,
there is no longer need _PKI_ for authentication.

## TLS: Transport Layer Security

_TLS_ is a cryptographic protocol to provide secure communication
over network.
Nowadays, _TLS_ is a well-established crypto module
in widespread use on major web sites and browsers
for web-browsing, email, messaging applications
to provide __privacy__ and __integrity__
of secure communication between devices.

## Structure of This Book

First, we will talk how _TLS_ works, including its requirements and limits.
Next, we need to figure out what is __Password authenticated Key Exchange(PAKE)__
and its properties. It is base of _J-PAKE_.
Then, to overcome the drawbacks of _TLS_ and _PAKE_, _J-PAKE_ is introduced.
Therefore, we have sequential chapters for  _TLS_, _PAKE_, and _J-PAKE_.

## Feel Free to Correct Me

Well, I study this topic only about one month,
it's hard to make sure that there is no anything wrong.
In addition, some sentences might be weird
or the grammar needs to be revised
since English is not my native language.
Please feel free to correct me
if you see anything that can enhance this book :)

## Talk slides

The Magic behind Remotecontrol
Service of Firefox OS TV: [slides here][slides]

[RemoteControlImg]: http://img.youtube.com/vi/Hqv_EnqQ86Y/0.jpg "FxOS Remote Control"
[RemoteControlURL]: https://www.youtube.com/watch?v=nVu4rxjqtOM&list=PLSVOWZrQzZlY07b3gR6ONDECSsh-83w9N "FxOS Remote Control"
[slides]: https://docs.google.com/presentation/d/15iXd4ZXy9Y1uKdXkuFsdoqXAzw7Y4pUFKlDaNiAFkb0/edit?usp=sharing "The Magic behind Remote-control Service of Firefox OS TV"
<!-- [RemoteControlURL]: https://www.youtube.com/playlist?list=PLSVOWZrQzZlY07b3gR6ONDECSsh-83w9N "FxOS Remote Control" -->