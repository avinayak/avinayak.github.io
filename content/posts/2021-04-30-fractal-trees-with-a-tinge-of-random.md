---
categories: art
title: Fractal Trees with a bit of random()
date: 2019-04-30T15:00:00.000Z
category: Programming
tags: fractals;p5js
---

![](/media/atul-vinayak-aU2Xvdhh-mQ-unsplash\(1\).jpg)I was trying to generate [Pythagoras Tree fractal](https://en.wikipedia.org/wiki/Pythagoras_tree_\(fractal\)) in p5js, when I decide to see what would happen If I add `random()` in the branch angle code. It turns out that with high amount of branching, this can give some cool photorealsitic dandelionesque flower images.

It started out really tame like this. These are really just circles with constant radii.

![](/media/EysQW6KUUAA9Km_.png)

With some tweaking of branch angles using random + radii of circle being a function of branch depth.

![](/media/EytMtstVIAYFtTk.png)

Other samples. Each with a some param being `random()`

![](/media/EyxflmqU4AI4FNp.png)![](/media/EyxfXrnVgAM9am_.png)![](/media/EyxfZEmVcAoxTaD.png)![](/media/EyxfcZAUYAEABIU.png)

This is all the code for this:

```javascript
setup = _ => {
  createCanvas(w=1080, h = 1080);
  background(0);
  r = random
  v = [
    [w / 2, h, 3 / 2, 9, 14]
  ]
  stroke(255)
}
x = b =>
  v.splice(b, 0, [([_,n,o,_,u] = v[b])[0], n,o + .5-r(), 9, u - 1])

draw = _ => {
  smooth()

  i = 0
  while (i < v.length &&(c = v[i])[4])
    if (c[3]--) {
      h = (c[4] + 6) / r(1, 5)
      circle(c[0] -= cos(c[2]) * h, c[1] -= sin(c[2]) * h, 0.001)
      i++
    } else {
      x(i++)
      x(i++)
      v.splice(i, 1)
    }
  for([k,l,_,_,e] of v)
    circle(k,l,.1)
}
```

Here's a recording of the whole process

<video loop autoplay muted src="/media/fractalrandom.mp4" />