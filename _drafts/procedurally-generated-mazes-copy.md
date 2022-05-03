---
title: Fast Palette overlay for WasmBoy using feColorMatrix
date: 2022-04-10 00:00:00 +0000
categories:
- programming
- design
- math
layout: post

---
The problem: Most Gameboy(classic) emulators tend to use the Grayscale palette with no possibility of even having the option to choose a different set of colors. ie. They all look like 

![](/uploads/screenshot-from-2022-05-03-20-56-07.png)

This, when they could look like

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">SD Hiryuu no Ken Gaiden<br>by Culture Brain(1995) for GameBoy<a href="https://twitter.com/hashtag/pixelart?src=hash&amp;ref_src=twsrc%5Etfw">#pixelart</a> <a href="https://twitter.com/hashtag/gameboy?src=hash&amp;ref_src=twsrc%5Etfw">#gameboy</a> <a href="https://t.co/18PkLWsyXQ">pic.twitter.com/18PkLWsyXQ</a></p>&mdash; Pixel Snips (@pixelsnips) <a href="https://twitter.com/pixelsnips/status/1298047083874639872?ref_src=twsrc%5Etfw">August 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

By the way.. that was from a discontinued bot experiment(ie. rip youtube gameboy gameplay videos, upscale it and apply random palette) I ran in 2020.

Recently, I came across this cool wasm based gameboy emulator called [WasmBoy](https://github.com/torch2424/wasmboy). 