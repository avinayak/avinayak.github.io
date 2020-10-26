---
title: Deobfuscating a Maze Program
date: 2020-10-25 15:00:00 +0000
categories:
- programming
layout: post

---
I was randomly wandering inside Wikipedia when I came across this interesting page [https://en.wikipedia.org/wiki/Obfuscation_](https://en.wikipedia.org/wiki/Obfuscation_ "https://en.wikipedia.org/wiki/Obfuscation_")(software), and this interesting piece of code. 

    char*M,A,Z,E=40,J[40],T[40];main(C){for(*J=A=scanf(M="%d",&C);
    --            E;             J[              E]             =T
    [E   ]=  E)   printf("._");  for(;(A-=Z=!Z)  ||  (printf("\n|"
    )    ,   A    =              39              ,C             --
    )    ;   Z    ||    printf   (M   ))M[Z]=Z[A-(E   =A[J-Z])&&!C
    &    A   ==             T[                                  A]
    |6<<27<rand()||!C&!Z?J[T[E]=T[A]]=E,J[T[A]=A-Z]=A,"_.":" |"];}

According to the article, this was a non winning entry for the 1988 [International Obfuscated C Code Contest](https://en.wikipedia.org/wiki/International_Obfuscated_C_Code_Contest). I really have no idea how anyone could've topped this. I serached around [http://www.de.ioccc.org/years.html#1988](http://www.de.ioccc.org/years.html#1988 "http://www.de.ioccc.org/years.html#1988"), but it looks like this entry is missing in this page. Wikipedia citation points me to a book, which I might check out later.

What's interesting about this piece of code is that

* It looks like a maze.
* It can generate mazes of any height (and width if you can tweak it a bit).
* The word MAZE is spelled with white-spaces if you look carefully. Here's it highlighted 

  ![](/uploads/screenshot-from-2020-10-26-21-26-24.png)

According to wikipedia, 

I'll attempt to de-obfuscate this code as much as I can and try to explain how it works, and maybe even re-implement this in a different language.