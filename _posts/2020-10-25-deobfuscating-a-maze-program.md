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

Also, as the wiki points out, ANSI-compliant C compilers don't allow constant strings to be overwritten, which can be avoided by changing "*M" to "M\[3\]" and omitting "M=". I did this and tried to compile + run it, and sure enough,

    ~ $ gcc m.c && ./a.out 
    m.c:14:32: warning: return type defaults to ‘int’ [-Wimplicit-int]
       14 | char M[3],A,Z,E=40,J[40],T[40];main(C){for(*J=A=scanf("%d",&C);
          |                                ^~~~
    m.c: In function ‘main’:
    m.c:14:32: warning: type of ‘C’ defaults to ‘int’ [-Wimplicit-int]
    m.c:14:49: warning: implicit declaration of function ‘scanf’ [-Wimplicit-function-declaration]
       14 | char M[3],A,Z,E=40,J[40],T[40];main(C){for(*J=A=scanf("%d",&C);
          |                                                 ^~~~~
    m.c:14:49: warning: incompatible implicit declaration of built-in function ‘scanf’
    m.c:1:1: note: include ‘<stdio.h>’ or provide a declaration of ‘scanf’
      +++ |+#include <stdio.h>
        1 | // #define W 40
    m.c:16:15: warning: implicit declaration of function ‘printf’ [-Wimplicit-function-declaration]
       16 | [E   ]=  E)   printf("._");  for(;(A-=Z=!Z)  ||  (printf("\n|"
          |               ^~~~~~
    m.c:16:15: warning: incompatible implicit declaration of built-in function ‘printf’
    m.c:16:15: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
    m.c:16:51: warning: incompatible implicit declaration of built-in function ‘printf’
       16 | [E   ]=  E)   printf("._");  for(;(A-=Z=!Z)  ||  (printf("\n|"
          |                                                   ^~~~~~
    m.c:16:51: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
    m.c:18:31: warning: format not a string literal and no format arguments [-Wformat-security]
       18 | )    ;   Z    ||    printf   (M   ))M[Z]=Z[A-(E   =A[J-Z])&&!C
          |                               ^
    m.c:20:8: warning: implicit declaration of function ‘rand’ [-Wimplicit-function-declaration]
       20 | |6<<27<rand()||!C&!Z?J[T[E]=T[A]]=E,J[T[A]=A-Z]=A,"_.":" |"];}
          |        ^~~~
    24
    ._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._
    |_._. ._| |_. ._._. . . | . ._| |_. ._._._|_._. | |_. |_. | |_. | | | ._|_. | |
    |_._._. |_._._| . ._|_| . | ._._._._._._._| ._._._| | . |_. | ._|_._._. | | | |
    | ._| | . . . . |_._._|_| |_| | | |_._. | | . . . ._|_| | |_. ._._._| ._._. ._|
    |_._._._|_|_|_|_| . . . . | | ._. ._._|_. ._|_| |_| ._. . . ._._. |_. . ._|_. |
    | ._| . |_. . . |_| |_| |_|_._. |_._._._| ._._|_. |_._|_|_| |_. |_._. |_| | | |
    | |_._|_. ._|_| . |_| | | | |_. ._. ._. ._._. |_. . . ._. |_._|_. |_. | ._. | |
    |_._. |_._. |_. |_._._| | | . . . | ._| ._|_. | |_| |_._|_| | ._._| |_._| |_| |
    |_._. . ._._._| ._. . | ._._| | | |_| ._|_. | ._|_. ._._._._|_._._._._. ._._._|
    | ._. |_._._._|_. |_|_|_. ._|_| |_._| . . ._|_._._| ._| ._|_._._._. . ._._. ._|
    |_._|_| ._._._| |_. |_. | |_._._| . | |_|_._._|_._. | ._. . ._._. | |_| | |_| |
    | | | |_. . ._. ._| ._|_._| | ._. |_. |_._. . . . . | | ._| ._. | ._._._. ._| |
    | . ._| ._|_. | ._| | ._. ._. . |_|_._._. | | | | | ._|_._| |_. | |_. |_._|_. |
    | |_._._| . |_|_| | |_. |_. |_|_. . ._| |_| |_|_| |_._| ._| ._| |_| | . ._._._|
    | | | . ._|_._._._._| | ._|_._._|_|_._._. |_. | |_. . ._| | . |_| ._._| |_. ._|
    |_._. |_._. | . |_. ._| ._. . . ._._._. | | ._|_. |_| | | |_|_|_. |_. | ._._._|
    |_. . . . |_._|_. . |_._| | |_| . |_._. | |_|_._. | ._._| | ._._._. | |_._| | |
    | |_|_| |_._._. |_| ._. ._._| ._| ._._| | | . . . ._._._._|_| | | ._| ._._| | |
    | ._. . . ._|_._._|_. | | |_._|_._._|_._|_| |_|_|_. | | . | | ._. | |_. ._|_. |
    |_|_. |_|_. . |_. |_._|_._._. ._._. . . ._|_._._| | ._._| ._|_. | | | |_. |_. |
    |_. . ._| ._| ._._._. . | | | |_._. |_|_| |_. . . |_| | |_| . ._|_._. . | ._._|
    |_. |_. | ._| . | | | |_|_. ._._._|_._| . . |_| | . | ._| ._|_| |_._. |_|_._. |
    |_._._|_| ._|_| ._._| |_. | . ._._._|_._|_| |_._|_| | ._|_._._. ._. |_| | |_. |
    |_._._. |_| |_._._._| . | | |_|_._. | . . ._| | ._| . ._._|_._. | |_. . ._| ._|
    |_._._._._._._._._._._|_|_._._._._._._|_|_._._._._._|_._._._._._|_._._|_._._._|
    | ~ $
    

It works! 

This code tries to read the value for height (which I entered as 24). The width is locked to 80 characters, probably because that was the default number of characters per line in 1988?? 

I'll attempt to de-obfuscate this code as much as I can and try to explain how it works, and maybe even re-implement it's logic in a different language.

## Cleanup

I started out by removing unwanted white-spaces and line breaks, which gave me

    char M[3],A,Z,E=40,J[40],T[40];main(C){for(*J=A=scanf("%d",&C);--E;J[E]=T[E]=E)printf("._");for(;(A-=Z=!Z)||(printf("\n|"),A=39,C--);Z||printf(M))M[Z]=Z[A-(E=A[J-Z])&&!C&A==T[A]|6<<27<rand()||!C&!Z?J[T[E]=T[A]]=E,J[T[A]=A-Z]=A,"_.":" |"];}

the whole program is only 239 bytes!. Running it through code beautify gave me:

    char M[3], A, Z, E = 40, J[40], T[40];
    main(C) {
      for ( * J = A = scanf("%d", & C); --E; J[E] = T[E] = E) printf("._");
      for (;(A -= Z = !Z) || (printf("\n|"), A = 39, C--); Z || printf(M)) 
        M[Z] = Z[A - (E = A[J - Z]) 
          && !C & A == T[A] | 6 << 27 < rand() 
          || !C & !Z ? J[T[E] = T[A]] = E, J[T[A] = A - Z] = A, "_." : " |"];
    }

Lets try removing the scanf call and replacing 40 (I'm guessing the width of the maze divided by 2) so we can experiment with arbitrary widths and heights.

    #define W 30
    char M[3], A, Z, E = W, J[W], T[W];
    main() {
      int H=20;	
      for ( * J = A = 1; --E; J[E] = T[E] = E)printf("._");
      for (;(A -= Z = !Z) || (printf("\n|"), A = W-1, H--); Z || printf(M)) 
      	M[Z] = Z[A - (E = A[J - Z]) 
    	  && !H & A == T[A] | 6 << 27 < rand() 
    	  || !H & !Z ? J[T[E] = T[A]] = E, J[T[A] = A - Z] = A, "_." : " |"];
    }