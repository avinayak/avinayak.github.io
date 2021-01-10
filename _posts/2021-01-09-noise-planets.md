---
title: Noise Planets
date: 2021-01-09 03:00:00 +0000
categories:
- art
layout: post

---
![](/uploads/erporydxmaarwcd.png)

This piece called LINES 2A (2017) by [Tyler Hobbs](https://twitter.com/tylerxhobbs) kinda looked very hand drawn, but it's completely generative. Something about this drawing kind of resonated with me, so I wanted to try to study and replicate (or make something inspired by this work) using p5. 

I started out by plotting a bunch of random points within a circle like so.

    w = 1000
    function setup() {
      createCanvas(w, w);
      background('#F9F8F4');
    }
    
    function draw() {
      x = random(w)
      y = random(w)
      if (pow(w/2 - x, 2) + pow(w/2 - y, 2) < 7e4) {
        point(x,y)
      }
    }

![](/uploads/download-25.png)