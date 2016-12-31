# Blasto
A Python implementation of Hill-Climbing for cracking classic ciphers.

Blasto currently supports following ciphers :

-	Substitution cipher (includes Caesar Shift, Affine, etc...)
-	Turning Grille cipher

It also supports following languages used for plaintext scoring :

-	English
-	German
-	Spanish

*Quadgram statistics for the above languages are generated from <a href="http://practicalcryptography.com/">practicalcryptography.com</a><br>.

# Installation

To install Blasto, clone this repository and run `python setup.py install`

# Usage

```
usage: blasto [options]

optional arguments:
  -h, --help           show this help message and exit
  -i FILE              Input ciphertext from file. If not defined, ciphertext
                       will be inputed manually
  -o FILE              Save output result to file
  --cipher CIPHERTYPE  Set cipher type. If not defined, it will be prompted to
                       select manually. Available: (subs, grille)
  -s SEC, --sleep SEC  Set interval time between iterations to avoid max CPU
                       usage (0 to none). (Default=0.0001)
  -c NUM, --count NUM  Set iterations. (Default=1000)
  -l LANGUAGE          Set Plaintext language for Quadgram statistic.
                       Available: (en, es, de). (Default=en)
```                       

Example
----------------------

Running with default options.
```bash
~$ blasto

1. Substitution Cipher
2. Turning Grille Cipher

Select Cipher Type : 1
Enter ciphertext : HSJFHSJCNSKAFKAFJLAGKAL
```

Running with ciphertext from a file, use specified cipher and save final plaintext to a file.
```bash
~$ blasto --cipher=subs -i cipher.txt -o plain.txt
```

Running with 10000 `count` per iterations and using German language based plaintext.
```bash
~$ blasto --count=10000 -l de
```

# About Hill-Climbing

In computer science, hill climbing is a mathematical optimization technique which belongs to the family of local search. It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by incrementally changing a single element of the solution. If the change produces a better solution, an incremental change is made to the new solution, repeating until no further improvements can be found...

(<a href="https://en.wikipedia.org/wiki/Hill_climbing">https://en.wikipedia.org/wiki/Hill_climbing</a>)