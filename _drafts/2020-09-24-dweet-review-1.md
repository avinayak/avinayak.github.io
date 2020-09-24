---
title: 'Dweet Review #1 - Pixel Spaceships'
date: 2020-09-24T00:00:00.000+00:00
categories:
- programming
- procedural_generation
layout: post

---
<iframe width=500 height=570 frameBorder="0" src="https://www.dwitter.net/e/3078" allowFullScreen="true"></iframe>

Hello!  
I've decided to review/analyze some really cool dweets in this new series of posts. For those who do not know, a dweet is a short js program of 140 characters or less designed to run in [dwitter](https://www.dwitter.net/). For the first dweet study, I've picked procedural pixel spaceship generation.

First up, u/FireFly's 1-bit spaceships.

![](/uploads/screenshot-from-2020-09-24-12-53-31.png)

    for(i=2e3;!t&&i--;Math.random()>(X**2+(Y-4)**2)**.5/6&&f(7)+f(-7))X=i&
    3,Y=i>>2&7,f=m=>x.fillRect(240*(i>>5&7)+120-X*m,180*(i>>8)+50+Y*7,7,7)

Prettifying this js script gives us

    for(i=2e3;!t&&i--;Math.random()>(X**2+(Y-4)**2)**.5/6&&f(7)+f(-7))
    {
        X=i&3;
        Y=i>>2&7,
        f=m=>x.fillRect(240*(i>>5&7)+120-X*m,180*(i>>8)+50+Y*7,7,7)
    }