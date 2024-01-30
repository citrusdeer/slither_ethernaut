# Ethernaut Detectors

As I tried working through Ethernaut, it seemed like a good opportunity to
test and try some new (to me) tools! Slither, Echidna, etc

It seems logical to me that CTF challenges should easily flag on static analysis.
They are, after all, common and well known vulnerabilities, boiled down to their
most basic and easily-digestible-for-beginners form. So imagine my dismay as I
run slither on many of the contracts and get no findings, even on the simplest levels!
Vulnerabilities that I can see with the human eye, before even running it!
And yet slither cannot.

Lets fix that! As I work through ethernaut, lets multitask and make some new detectors.
Hopefully, the simplicity of the challenges doesn't over simplify my detectors too much,
and they remain useful in real world contexts!

WARNING: While I am an experienced software developer and Security Researcher, I am relatively new
to Solidity and the unique design decisions and vulnerabilities of the EVM and contract architecture.
I am using this repo to learn (and hopefully document that learning in a public way).
I hope others can get value from these detectors, but i make no guarentees about the quality, detection
rate, or anything else. I hope they bring you value, but use at your own risk, and do your own research.


