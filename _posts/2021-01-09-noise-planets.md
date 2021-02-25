---
title: Noise Planets
date: 2021-01-09T03:00:00.000+00:00
categories:
- art
layout: post

---
![](/uploads/erporydxmaarwcd.png)
<cap>Thank you Tyler Hobbs for the inspiration</cap>

I recently found this piece of art (LINES 2A (2017)) created by [Tyler Hobbs](https://twitter.com/tylerxhobbs). This picture kinda looked very hand drawn, but it's completely generative. Something about this drawing and it's texture kind of resonated with me, so I wanted to try to study and replicate (or make something inspired by this work) using p5js.

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

1. Choose a random point `<x,y>`
2. Plot `<x,y>`
3. Calculate `n = noise(x,y)`
4. Do `x+=cos(n * 2 * PI)` and `y+=sin(n * 2 * PI)`
5. Repeat 2.

We're going to plot flow fields inside the circle. Let's try this.

    const is_in_circle = (x, y) => 
      (pow(w / 2 - x, 2) + pow(w / 2 - y, 2) < 7e4)
    
    function draw() {
      if (is_in_circle(x = random(w), y = random(w)))
        while (is_in_circle(x, y)) {
          n = noise(x, y)
          x += sin(n * TAU)
          y += cos(n * TAU)
          point(x, y)
        }
    }

![](/uploads/download-28.png)

OK, not very good. The noise at this level is pretty rough. we're going to zoom in to the noise function (by dividing the `x,y` inputs by some constant value) and probably use `circle(x ,y ,0.3)` to plot points instead if point function, because I feel it looks way smoother. Also, I'm adding a `random() > 0.01` condition in the loop so that we also get short lines that are not trimmed away by the edge of the circle.

    function draw() {
      if (is_in_circle(x = random(w), y = random(w)))
        while (is_in_circle(x, y) && random() > 0.01) {
          n = noise(x / 500, y / 500)
          x += sin(n * TAU)
          y += cos(n * TAU)
          circle(x, y, .3)
        }
    }

![](/uploads/download-27.png)

Actually.. not bad. I think we manage almost replicate the original texture. The inverted version also looks pretty good.

![](/uploads/download-19.png)

![](/uploads/ppanets.png)

I went ahead and made a つぶやきProcessing version of this.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">function setup(){createCanvas(w=1e3,w),background("<a href="https://twitter.com/hashtag/%E3%81%A4%E3%81%B6%E3%82%84%E3%81%8DProcessing?src=hash&ref_src=twsrc%5Etfw">#つぶやきProcessing</a>")}function draw(){if(g(x=random(w),y=random(w)))for(;g(x,y)&&random()>.01;)n=noise(x/500,y/500),x+=sin(n_TAU),y+=cos(n_TAU),circle(x,y,.3)}g=((n,o)=>pow(w/2-n,2)+pow(w/2-o,2)<w*w/16); <a href="https://t.co/iVZTMtCn3i">pic.twitter.com/iVZTMtCn3i</a></p>— yakinavault (@yakinavault) <a href="https://twitter.com/yakinavault/status/1347903013042622467?ref_src=twsrc%5Etfw">January 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Going Further: Animations

The code we wrote right now technically is animated. The animation however is not very smooth.

<video loop autoplay muted> <source src="https://avinayak.github.io/uploads/simplescreenrecorder-2021-01-10_03-52-31.mp4" type="video/mp4" /> </video>

To make smooth animations, we need to generate new points in the circle, keep track of these points outside the `draw()` function. I found this neat [technique](https://stackoverflow.com/a/50746409), to find random points in a circle where a random radius `r` and angle `theta` are chosen and the `x,y` points are obtained as `x = centerX + r * cos(theta)` and `y = centerY + r * sin(theta)`

Let's try that first.

    function random_point() {
      r = random(w / 4)
      t = random(TAU)
      return [
        w/2 + cos(t) * r, 
        w/2 + sin(t) * r
      ]
    }
    
    function setup() {
      createCanvas((w = 1e3), w);
      background(255)
      k = w / 2
      m = (Array(w).fill(0)).map(random_point)
    }
    
    function draw() {
      for (i = k; --i;) {
        [x, y] = m[i]
        circle(x, y, .3);
      }
    }

![](/uploads/screenshot-from-2021-01-10-04-51-20.png)

and now we apply flow fields and try to move these points.

    function random_point() {
      r = random(w / 4)
      t = random(TAU)
      return [
        w/2 + cos(t) * r, 
        w/2 + sin(t) * r
      ]
    }
    
    const w = 1000
    function setup() {
      createCanvas(w, w);
      background('#F9F8F4')
      k = w / 2
      points = (Array(k).fill(0)).map(random_point)
    }
    
    function draw() {
      for (i = k; --i;) {
        [x, y] = m[i]
        x += sin(n = noise(x / 400, y / 400) * TAU) * h
        y += cos(n) * h
        stroke(i%255)
        circle(x, y,.3)
        if (pow(k - x, 2) + pow(k - y, 2) < 7e4)  // if point is in circle
          points[i] = [x, y, t]
        else points[i] = random_point() // replace with new point if not
      }
    }

<video loop autoplay muted> <source src="/uploads/simplescreenrecorder-2021-01-10_04-56-11.mp4" type="video/mp4" /> </video>

And a つぶやきProcessing version of course..

<blockquote class="twitter-tweet"><p lang="cy" dir="ltr">t=0,p=i=>\[k+(r=random(w/4))_cos(t+=.1),k+r_sin(t)\],setup=i=>{createCanvas(w=1e3,w),m=Array(k=w/2).fill(0).map(p)},draw=r=>{for(i=k;--i;)\[x,y\]=m\[i\],x+=sin(n=noise(x/k,y/k)_TAU),y+=cos(n),stroke(i%4_85),point(x,y),k_w+x_x+y_y-w_(x+y)<7e4?m\[i\]=\[x,y\]:m\[i\]=p()};//<a href="https://twitter.com/hashtag/%E3%81%A4%E3%81%B6%E3%82%84%E3%81%8DProcessing?src=hash&ref_src=twsrc%5Etfw">#つぶやきProcessing</a> <a href="https://t.co/xVhCBNUltL">pic.twitter.com/xVhCBNUltL</a></p>— yakinavault (@yakinavault) <a href="https://twitter.com/yakinavault/status/1347930637227855874?ref_src=twsrc%5Etfw">January 9, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Adding Colors

There are many strategies to colorizing this sketch. One is by just giving each particle a random initial color.

![](/uploads/download-21.png)

However, I found that maintaining the initial x or y position in the particle array and using that to derive the hue information gives us some nice Jupiter/gaseous planet vibes.

<video loop autoplay muted> <source src="https://avinayak.github.io/uploads/simplescreenrecorder-2021-01-10_05-18-19.mp4" type="video/mp4" /> </video>

The fringing at the sides can be avoided by moving 50% of the points in the reverse direction.

<video loop autoplay muted> <source src="https://avinayak.github.io/uploads/simplescreenrecorder-2021-01-10_05-28-03.mp4" type="video/mp4" /> </video>

<video loop autoplay muted> <source src="https://avinayak.github.io/uploads/simplescreenrecorder-2021-01-10_08-43-25.mp4" type="video/mp4" /> </video>

More color variations

![](/uploads/untitled.png)

And that's it. Hope this was educational!