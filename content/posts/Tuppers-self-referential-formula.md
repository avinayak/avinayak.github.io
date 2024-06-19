---
title: Tupper's self-referential formula
date: 2024-06-19T07:00:00.000Z
category: Programming
tags: math
status: published
---

I saw this old tweet today\
\
\<blockquote class="twitter-tweet">\<p lang="en" dir="ltr">Tupper\&#39;s self-referential formula is a formula that visually represents itself when graphed at a specific location in the (x, y) plane. \<a href="https\://t.co/R0L3ZjqcyP">pic.twitter.com/R0L3ZjqcyP\</a>\</p>\&mdash; Fermat\&#39;s Library (@fermatslibrary) \<a href="https\://twitter.com/fermatslibrary/status/1470392579288145931?ref\_src=twsrc%5Etfw">December 13, 2021\</a>\</blockquote> \<script async src="https\://platform.twitter.com/widgets.js" charset="utf-8">\</script> \
\
This blew my mind. The "data" used to render this is contained within the constant `k` as seen in the plot. The whole plot is 106x17. Someday I'll figure out how to reverse engineer this number, but right now I wanted to plot this using matplotlib. To get started, 
