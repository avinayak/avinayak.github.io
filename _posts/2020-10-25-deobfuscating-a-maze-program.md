---
title: Deobfuscating a Maze Program
date: 2020-10-25 15:00:00 +0000
categories:
- programming
layout: post

---
I was wandering in Wikipedia when I came across this interesting page [https://en.wikipedia.org/wiki/Obfuscation_](https://en.wikipedia.org/wiki/Obfuscation_ "https://en.wikipedia.org/wiki/Obfuscation_")(software), and this interesting piece of code. 

    char*M,A,Z,E=40,J[40],T[40];main(C){for(*J=A=scanf(M="%d",&C);
    --            E;             J[              E]             =T
    [E   ]=  E)   printf("._");  for(;(A-=Z=!Z)  ||  (printf("\n|"
    )    ,   A    =              39              ,C             --
    )    ;   Z    ||    printf   (M   ))M[Z]=Z[A-(E   =A[J-Z])&&!C
    &    A   ==             T[                                  A]
    |6<<27<rand()||!C&!Z?J[T[E]=T[A]]=E,J[T[A]=A-Z]=A,"_.":" |"];}

According to the article, this was a non winning entry for the 1988 [International Obfuscated C Code Contest](https://en.wikipedia.org/wiki/International_Obfuscated_C_Code_Contest). I really have no idea how anyone could've topped this. I searched around [http://www.de.ioccc.org/years.html#1988](http://www.de.ioccc.org/years.html#1988 "http://www.de.ioccc.org/years.html#1988"), but it looks like this entry is missing in this page. Wikipedia citation points me to a book, which I might check out later.

The interesting part is..

* It looks like a maze.
* It can generate mazes of any height.
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

running this yields a 60x20 maze as expected

    ._._._._._._._._._._._._._._._._._._._._._._._._._._._._._
    |_._. ._| |_. ._._. . . | . ._| |_. ._._._|_._. | |_. |_. |
    | | |_. | | | ._|_. |_|_._|_._|_. ._._| |_. ._| |_._._._. |
    |_._. |_. |_._._| | . |_. | ._|_._._. | | | ._| | . . . . |
    |_._._. | | . |_._. |_| | . . ._| ._|_. |_._. |_. |_|_|_|_|
    | ._._._._._|_._| . . . . | |_| |_. ._._|_. ._. |_. |_. ._|
    | | ._._. |_. . ._|_|_| |_| |_. | | |_. . . | . ._|_._. | |
    |_._._. |_._|_|_. ._|_._. |_| ._._. | . | | |_|_._. ._. . |
    | | | . | |_. ._. ._. ._|_. ._|_. | ._| |_| ._| ._. ._|_| |
    | | ._| . |_._. |_._| ._| ._._._| |_| | ._| | ._. |_|_. | |
    | | ._|_| . . ._._| |_. | ._._._._| |_._._|_|_|_. | | ._._|
    | | | |_. | |_. . ._|_._|_|_._. ._._._._._._._|_._._|_| ._|
    |_._._._|_|_| |_|_. ._._|_. . . ._._._. ._| ._|_._._._. ._|
    | |_._. ._._._| ._._._| |_. |_| . |_._._| . | |_._. ._._._|
    | | | ._. . ._._. | | | . | . | |_. . ._._| |_. | |_. . ._|
    | |_._| . |_._._|_| | ._| | | |_| |_| ._. | ._._._. . |_. |
    | ._| ._|_._| | | . ._._|_|_| . |_._._._| | | | | ._|_._| |
    | |_. | | |_. |_. |_. ._._._|_| | | . ._|_|_| ._._._| | |_|
    | | ._._| ._. |_._| | | . . ._._. . | . ._._|_._._._| | ._|
    |_._._._._._| ._. | |_._| | ._| |_| | |_| ._. ._|_. |_._. |
    |_._._._._._._._|_._._._._|_._._._|_|_._._|_._._._._._._._|
    

## Analysis

let's start by looking at line 5: `for ( * J = A = 1; --E; J[E] = T[E] = E)printf("._");`

`printf("._")` is responsible for the first line of wall. but the loop it's part of is doing something else.

* It initializes first value of array J and char A as 1. 
* evaluates `--E`, so runs 29 times
* does `J[E] = T[E] = E` and `printf("._")`.

So, It looks like at the end of the loop

* E will be zero
* Array J will have values 1,1,2,3,..29 (1 at zeroth position set in the loop init)
* Array T will have values 0,1,2,3,..29

setting a breakpoint at line 6 and running this with gdb shows you what happened:

    (gdb) x/100b J
    0x555555558040 <J>: 	1	1	2	3	4	5	6	7
    0x555555558048 <J+8>:	8	9	10	11	12	13	14	15
    0x555555558050 <J+16>:	16	17	18	19	20	21	22	23
    0x555555558058 <J+24>:	24	25	26	27	28	29	0	0
    0x555555558060 <J+32>:	0	0	0	0	0	0	0	0
    0x555555558068 <J+40>:	0	0	0	0	0	0	0	0
    0x555555558070 <J+48>:	0	0	0	0	0	0	0	0
    0x555555558078 <J+56>:	0	0	0	0	0	0	0	0
    0x555555558080 <J+64>:	0	0	0	0	0	0	0	0
    0x555555558088 <J+72>:	0	0	0	0	0	0	0	0
    0x555555558090 <J+80>:	0	0	0	0	0	0	0	0
    0x555555558098 <J+88>:	0	0	0	0	0	0	0	0
    0x5555555580a0 <J+96>:	0	0	0	0
    (gdb) x/100b T
    0x5555555580c0 <T>: 	0	1	2	3	4	5	6	7
    0x5555555580c8 <T+8>:	8	9	10	11	12	13	14	15
    0x5555555580d0 <T+16>:	16	17	18	19	20	21	22	23
    0x5555555580d8 <T+24>:	24	25	26	27	28	29	0	0
    0x5555555580e0 <T+32>:	0	0	0	0	0	0	0	0
    0x5555555580e8 <T+40>:	0	0	0	0	0	0	0	0
    0x5555555580f0 <T+48>:	0	0	0	0	0	0	0	0
    0x5555555580f8 <T+56>:	0	0	0	0	0	0	0	0
    0x555555558100 <T+64>:	0	0	0	0	0	0	0	0
    0x555555558108 <T+72>:	0	0	0	0	0	0	0	0
    0x555555558110 <T+80>:	0	0	0	0	0	0	0	0
    0x555555558118 <T+88>:	0	0	0	0	0	0	0	0
    0x555555558120 <T+96>:	0	0	0	0
    (gdb) print E
    $9 = 0 '\000'
    (gdb) print A
    $11 = 1 '\001'
    

Line 6, starts with a loop condition `(A -= Z = !Z) || (printf("\n|"), A = W-1, H--)` . The printf in this condition also does, from what it looks like, draws the left side wall.

Quick refresher on conditional execution using `||` and `&&`

    #include <stdio.h>
    
    int main()
    {
        0 || printf("test 1\n");
        1 || printf("test 2\n"); // any nonzero
        0 && printf("test 3\n");
        1 && printf("test 4\n"); // any nonzero
        return 0;
    }
    /* prints:
    test 1                                                                                                                                                                             
    test 4
    */

So, the loop test expression executes nothing when `A -= Z = !Z` evaluates to non-zero and `(printf("\n|"), A = W-1, H--)` when `A -= Z = !Z` evaluates to zero. We can also guess that `(printf("\n|"), A = W-1, H--)` is executed once per row, since it has the left wall printf. 

In the whole program, Z, with initial value 0 is assigned a value only in this loop condition and it's simply !Z. This means, it can only take either 0 or 1 as a value. 

Also, this give us a clue about A. A is set to W-1 in as soon as the loop starts and is decremented in every alternate loop when Z == 1. A is not modified anywhere in the loop. So, A's value should go like 29,29,28,28,...1. when the final A-=Z happens, the condition evaluates to 0, triggering the side-wall expression which resets value of A to W-1.

The update statement is just `Z || printf(M)`. Seeing as this is the only other printf, we can be sure that this is the point where the maze gets rendered.

The body of the loop is something like `M[Z] = Z[..stuff..];`. This is bizarre. Z is used both as an array and an index. 

Since Z=0 or 1, we can guess the structure of M from the rest of the code. it'll always be of the form `< X, Y, '\0' >`, where X or Y can be one of the characters used to render the maze ('.' , '|' , ' ' or '_'). 

Let's looks at the "stuff" inside Z\[\] now. I added parenthesis for clarity on operator precedence, but I don't think it's much help for a line as long as this 

    ((A - (E = A[J - Z])) && ((!H & A == T[A] | 6 << 27 < rand()) || (!H & !Z))) ? (J[T[E] = T[A]] = E, J[T[A] = A - Z] = A, "_.") : (" |")

This is roughly in the form of `(s1 && (s2 || s3)) ? (s4, s5, "-."): " |"`. It's just a ternary operator that returns " |" or "-.".

we can replace the ternary operator with and if-else and the loop now looks like 

    for (; (A -= Z = !Z) || (printf("\n|"), A = W - 1, H--); Z || printf(M))
    	{
    		if (((A - (E = A[J - Z])) && ((!H & A == T[A] | 6 << 27 < rand()) || (!H & !Z))))
    		{
    			J[T[E] = T[A]] = E;
    			J[T[A] = A - Z] = A;
    			M[Z] = Z["_."];
    		}
    		else
    		{
    			M[Z] = Z[" |"];
    		}
    	}

much cleaner! one step further to clear up the condition.

    	for (; (A -= Z = !Z) || (printf("\n|"), A = W - 1, H--); Z || printf(M))
    	{
    		char s1 = A - (E = A[J - Z]);
    		char s2 = !H & A == T[A] | 6 << 27 < rand();
    		char s3 = !H & !Z;
    		if (s1 && (s2 || s3))
    		{
    			J[T[E] = T[A]] = E;
    			J[T[A] = A - Z] = A;
    			M[Z] = Z["_."];
    		}
    		else
    		{
    			M[Z] = Z[" |"];
    		}
    	}

It's starting to be readable now.

lets look at condition s1. the inner `A[J - Z]` is equivalent to `J[A - Z]`. why? it's just pointer math. think about it..

for condition s2, I added more paranthesis

    (!H & (A == T[A])) | (6 << 27) < rand()

and 6 << 27 is just 805306368 so

    (!H & (A == T[A])) | (805306368) < rand()

why this number? I think the whole point was to get a random boolean. We could try just replacing this with rand()%2. 

as for condition s3, it's very clear what this does. This is just a way to draw the bottom wall. we can confirm this by removing this condition.