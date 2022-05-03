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

Most GameBoy(classic) emulators tend to use the boring grayscale palette with no possibility of even having the option to choose a different set of colors. ie. They all look like this..

<video loop="" autoplay="" muted=""> <source src="https://video.twimg.com/ext_tw_video/1297925940022931457/pu/vid/800x720/WrOfp_Ri6QvMC4jP.mp4" type="video/webm"> </video>

when they could look like..

<video loop="" autoplay="" muted=""> <source src="https://video.twimg.com/ext_tw_video/1298047067340673024/pu/vid/800x720/TzN9E11-NUJsJqpW.mp4" type="video/webm"> </video>

Recently, I came across this cool wasm based GameBoy emulator called [WasmBoy](https://github.com/torch2424/wasmboy). It's actually possible to use WasmBoy as a library and create your own emulator front-end (like [https://vaporboy.net/](https://vaporboy.net/ "https://vaporboy.net/")). I wanted to make a cool minimal electron/web based GameBoy emulator frontend, but with the additional feature of being able to select a palette.

## How

I started out by poking internals of WasmBoy. Right now, the GB image buffer is mapped to a js `Uint8ClampedArray` called `imageDataArray` and

```js
this.canvasImageData.data.set(this.imageDataArray);
this.canvasContext.clearRect(0, 0, this.canvasElement.width, this.canvasElement.height);
this.canvasContext.putImageData(this.canvasImageData, 0, 0);
```

Width and height are same as that of number of pixels in a gameboy (160 x 144). For an rgba image therefore, we need to loop through an array of 160 * 144 * 4 = 92160 ints and replace each of the 4 grayscale levels with out custom palette colors. This might be possible, but I have a feeling this could result in very low framerates.

## CSS Shaders?

I knew that you could apply pixel level transformations using css `filters`. For example `filter: hue-rotate(90deg);`. You could apply this filter to almost anything, even a  I knew for a fact that this is internally just a simple fragment shader. Can you add your own custom shaders? Googling around gave be this: [https://developer.chrome.com/blog/introduction-to-custom-filters-aka-css-shaders/]. I got excited only to be let down few minutes later..

![](/uploads/screenshot-from-2022-05-03-21-38-14.png)

Bummer :/

## SVG Filters

I started to research more on libraries like [https://github.com/PixelsCommander/HTML-GL], to apply a shader to any given DOM element. I saw svg filters on the way, but discarded them thinking they could never be applied to canvas elements, or that they would have any other filters than the ones css offered. I was wrong. SVG filters were more powerful tools and they could be referenced from css like

```css
filter: url("../../media/examples/shadow.svg#element-id");
```

Quick experimentation showed game me this..

![](/uploads/screenshot-from-2022-05-01-00-45-23.png)

While it may look terrible, this is the result of applying a random feColorMatrix on the grayscale canvas from WasmBoy. The question now is, how do I map each of the grayscale levels to a specific color in a palette? Is this even mathematically possible with the filters we have in SVG?