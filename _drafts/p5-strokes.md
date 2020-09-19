---
title: Procedurally generated handwriting in a tweet
date: 2020-04-30 15:00:00 Z
categories:
- programming
- art
layout: post
---

I made a tweet go viral last week in the [#つぶやきProcessing](https://twitter.com/hashtag/%E3%81%A4%E3%81%B6%E3%82%84%E3%81%8DProcessing?src=hashtag_click) circles.

<blockquote class="twitter-tweet"><p lang="cy" dir="ltr">j=24,m=0,draw=(a=>{for(v=(i=>w/3*(n=noise)(i)-k),createCanvas(w=1e3,w),noFill(),background('<a href="https://twitter.com/hashtag/fd7?src=hash&ref_src=twsrc%5Etfw">#fd7</a>'),translate(0,m--),i=0,y=0;y<w-m;y+=j)for(x=k=90;x<w-k;x+=9)if(y+k>-m?curve(v(i++)+x,v(i++)+y,x,j+y,x+9,j+y,v(i++)+x,v(i++)+y):i+=4,x+=v(i++)%9,n(x*y)<.13)y+=j});//<a href="https://twitter.com/hashtag/%E3%81%A4%E3%81%B6%E3%82%84%E3%81%8DProcessing?src=hash&ref_src=twsrc%5Etfw">#つぶやきProcessing</a> <a href="https://t.co/WNIwAAAXjQ">pic.twitter.com/WNIwAAAXjQ</a></p>— atulvinayak (@atulvinayak) <a href="https://twitter.com/atulvinayak/status/1305116417419653120?ref_src=twsrc%5Etfw">September 13, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I'll try to explain how this script worked and how I was able to fit the whole thing into 280 characters. 
This all started when last week when I was experimenting with the p5js 