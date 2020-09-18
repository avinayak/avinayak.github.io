---
title: Particle Collision Experiments
date: 2013-12-19 00:00:00 Z
categories:
- programming
layout: post
---

OK, So I saw this in [reddit](https://www.reddit.com/r/gaming/comments/bdar7/colourful_5min_breakout_style_game_seriously_play).

<video controls="" muted="" src="https://i.imgur.com/T0EaN6u.mp4">
</video>

And I wanted to do something like that. I had plans to mess around with Box2D for a long time but didn’t get the opportunity. After a day’s worth of research,
I found out that Blender does a much better job in Physics simulation, and it has a Python interpreter. I couldn’t ask for more. and I made this!

<video controls="" muted="" loop="" src="http://i.imgur.com/RQXqIPT.mp4">
</video>

As you can see, the particles are not really particles here. They’re more like blocks. This is actually a 3D simulation.
The camera faces the Z-axis orthogonally in isometric view. In the beginning, there were no colors and the blocks were arranged into a huge rectangle. 
But I knew it looks much more satisfying if I did something similar to this (I was waiting for a real life application for this Programing 101 snippet) 😉

{% highlight c %}
for(int i=0;i<5;i++){
    for(int j=0;j<i;j++){
        printf("* ");
    }
    printf("\n");
}

/* Outputs 

* 
* * 
* * * 
* * * * 

*/

{% endhighlight %}

Also, I(Me being the idiot that I am), didn’t know the existence of the HSV/HSL functions, which would’ve made my life much easier. Instead, I had to implement this.

![My helpful screenshot](/assets/images/hsv.png)

With HSV(), I smoothly mapped the X locations of blocks with an H value, keeping S and V fixed.

In the end, I wanted to reduce the block size so that they’re more like particles, but my potato computer took ~ 30 Hrs to render this 😕.