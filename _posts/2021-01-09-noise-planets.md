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

This is a painfully slow process to generate random points in a circle. I found a better way to do this later. What I wanted to do next was to generate flow fields, but restricted to the circular region. 

It's super easy to generate flow field patterns using perlin noise.

1. Choose a random point <x,y>
2. Plot <x,y>
3. Calculate n = noise(x,y)
4. Do x+=cos(n * 2 * PI) and y+=sin(n * 2 * PI)
5. Repeat 2.

In this situation, we're going to plot flow fields inside the circle. Let's try this.

    const is_in_circle = (x, y) => 
      (pow(w / 2 - x, 2) + pow(w / 2 - y, 2) < 7e4)
    
    function draw() {
      if (is_in_circle(x = random(w), y = random(w)))
        while (is_in_circle(x, y)) {
          n = noise(x, y)
          x += sin(n * TAU)
          y += cos(n * TAU)
          circle(x, y, .3)
        }
    }

![](/uploads/download-28.png)

OK, not very good. The noise at this level is pretty rough. we're going to zoom in to the nose function (by dividing the x,y inputs) and probably use circle(x ,y ,0.3) to plot points instead if point function, because I feel it looks way smoother. Also, I'm adding a random() > 0.01 condition in the loop so that we get short lines that are not trimmed away by the edge of the circle.