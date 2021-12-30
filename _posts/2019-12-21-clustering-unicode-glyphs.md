---
title: Clustering Unicode Glyphs
date: 2019-12-21 15:00:00 +0000
categories:
- programming
layout: post

---
I saw this image of Language families across the globe today, and decided I wanted to do something related. 

![](/uploads/language_families_map.png)

What would happen if I apply a clustering algorithm to all the Unicode characters? I wanted to this done really quickly, So no reinventing the wheel.. we get the latest SoTA clustering algorithm and swap the dataset with the Unicode character data. Ideally, I wanted to do this with the Noto font, but I had a feeling it might get complicated (ie. Noto requires you to swap in .ttf files depending on what codepoints your glyphs are in). In the name of quick and easy Sunday afternoon project, I decided to go with [unifont](https://unifoundry.com/unifont/ "unifont").

## Creating Dataset

I found this official [VAE MLP Clustering tutorial](https://blog.keras.io/building-autoencoders-in-keras.html) on MNIST dataset for the keras library. Perfect. I hacked up a python script that generates Unifont glyphs in the 28x28x65536 pixel numpy array using Pillow Image processing lib. This has the same cross sectional shape of MNIST, so it should just work.

The problem though was missing glyphs.

![](/uploads/captdure.PNG)

I found that a huge portion of unifont was tofu (White squares with hexadecimal codepoint). We have to de-tofu this dataset.

I could've done some cool pattern matching filtering or manually figuring out the tofu from unifont documentation, but I I decided to export each 28x28 pixel glyph image to files and delete the tofu manually.

![](/uploads/wwwture.PNG)

Now, I regenerated the dataset with the missing file indices removed.