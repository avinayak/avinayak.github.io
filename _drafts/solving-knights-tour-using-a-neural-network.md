---
title: Solving Knights Tour using a Neural Network
date: 2013-04-11T00:00:00.000+00:00
categories:
- programming
- algorithm
layout: post

---
Recently came across this post by Dimitry Brant: [Knight’s Tours Using a Neural Network](https://dmitrybrant.com/knights-tour). A properly vectorized numpy re-implementation is long overdue, so I decided to give it a shot.  

A **knight's tour** is a sequence of moves of a [knight](https://en.wikipedia.org/wiki/Knight_(chess) "Knight (chess)") on a [chessboard](https://en.wikipedia.org/wiki/Chessboard "Chessboard") such that the knight visits every square exactly once. There are at-least 4 ways to solve this: Backtracking, Divide an Conquer, Warnsdorff's Heuristic and what most interesting of all, using a Neural Network. 

This is neither the most efficient nor practical algorithm to solve this problem, but it's definitely the most elegant way. Also, is it really a NN solution though? It feels more like a graph-theory problem to me.

Algorithm

1. Setup a Knight's Graph, A graph of all possible paths on a given chessboard. 
2. Initialize Vt, a vector the size of all the vertices of Knight's Graph, initialized randomly with 0/1. This vector is the Neural Network 
3. Initialize Ut, a zeros vector the size of all the vertices of Knight's Graph.
4. Until a solution is found repeat following
   1. 