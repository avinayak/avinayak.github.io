---
title: "[draft] Fast Palette overlay for WasmBoy using feColorMatrix "
date: 2022-04-10 00:00:00 +0000
categories:
- programming
- design
- math
layout: post

---
## The problem

Most GameBoy(classic) emulators tend to use the boring grayscale palette with no possibility of even having the option to choose a different set of colors. ie. They all look like this

![](/uploads/screenshot-from-2022-05-03-20-56-07.png)

This, when they could look like

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">SD Hiryuu no Ken Gaiden<br>by Culture Brain(1995) for GameBoy<a href="https://twitter.com/hashtag/pixelart?src=hash&ref_src=twsrc%5Etfw">#pixelart</a> <a href="https://twitter.com/hashtag/gameboy?src=hash&ref_src=twsrc%5Etfw">#gameboy</a> <a href="https://t.co/18PkLWsyXQ">pic.twitter.com/18PkLWsyXQ</a></p>— Pixel Snips (@pixelsnips) <a href="https://twitter.com/pixelsnips/status/1298047083874639872?ref_src=twsrc%5Etfw">August 24, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

By the way.. that was from a discontinued bot experiment (ie. rip youtube gameboy gameplay videos, upscale it and apply random palette) I ran in 2020.

Recently, I came across this cool wasm based GameBoy emulator called [WasmBoy](https://github.com/torch2424/wasmboy). It's actually possible to use WasmBoy as a library and create your own emulator front-end (like [https://vaporboy.net/](https://vaporboy.net/ "https://vaporboy.net/")). I wanted to make a cool minimal GameBoy emulator frontend, but with the additional feature of being able to select a palette. 

## How

I started out by poking internals of WasmBoy. Right now, the GB image buffer is mapped to a js `Uint8ClampedArray` called `imageDataArray` and 

```js
    this.canvasImageData.data.set(this.imageDataArray);
    this.canvasContext.clearRect(0, 0, this.canvasElement.width, this.canvasElement.height);
    this.canvasContext.putImageData(this.canvasImageData, 0, 0);
```

Width and height are same as that of number of pixels in a gameboy (160 x 144). For an rgba image therefore, we need to loop through an array of 160 * 144 * 4 = 92160 ints and replace each of the 4 grayscale levels with out custom palette colors. This might be possible, but I have a feeling this could be intractable. Can we do this with a fragment shader?

## CSS Shaders?

I knew that you could apply pixel level transformations 