---
title: Finding Mona Lisa in the Game of Life
date: 2021-02-19 15:00:00 +0000
categories:
- algorithms
- programming
layout: post

---
There was this rough idea I've been thinking about in [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) for a really long time.

<blockquote class="twitter-tweet" data-conversation="none"><p lang="en" dir="ltr">I wonder if it's possible to use some kind of stochastic algorithm that gives you an initial state which forms legible text after many cycles.</p>— yakinavault (@yakinavault) <a href="https://twitter.com/yakinavault/status/1291586306489761792?ref_src=twsrc%5Etfw">August 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

I came across [an article](https://kevingal.com/blog/mona-lisa-gol.html) of the same title by Kevin Galligan recently and I thought I could do something similar using a different approach. What if instead of using SAT Solvers, I use some kind of heuristic algorithm that could somehow "program" a large world of Game of Life to display an image after a few generations?

## Proof of Concept

I began working on a proof of concept version using the hill climbing technique. The idea was very simple.

1. Initialize variable best-score = infinity and an empty matrix as best-result
2. Start with a random matrix of 1s and 0s representing live and dead cells in Life.
3. Invert a single cell at a random location (modify).
4. Create a copy of this matrix.
5. Run N generations of Game of Life on the matrix
6. Compute a score of how close the matrix is with the target.
   1. If the score is less than best_score
      1. Set it as best score and set the copy from step 4 as best-result.
   2. else
   3. Copy best result to current matrix.
7. Repeat 3

Here's the important bit of code I used. Complete version of this POC is available here.

    def modify(state, shape):
        x,y = shape
        px = int(np.random.uniform(x+1))-1
        py = int(np.random.uniform(y+1))-1
        state[px][py] = not state[px][py]
        return state
    
    def rmse(predictions,targets):
        return np.sqrt(np.mean((predictions-targets)**2))
    
    while best_score>0.23:
        states = np.tile(np.copy(best_seed), (batch_size, 1, 1))
        rms_errors = []
        for state in range(len(states)):
            states[state] = modify(states[state], (m,n))
            rmse_val = rmse(target, nth_generation(np.copy(states[state])))
            rms_errors.append(rmse_val)
        lowest = min(rms_errors)
        if lowest < best_score:
            best_score = lowest
            best = rms_errors.index(lowest)
            best_state = states[best]

Hill Climbing works on finding the closest neighboring state to the state we have that has the least  difference from. The way I find the closest neighbor in every step is to create a copy of the best solution we have so far and invert a random cell. This change is small enough that we don't risk stepping over some local minima so much. Also we use root mean square error metric to compare the best state and the target. Other error metrics can be experimented with, but for this problem, I found that RMSE was sufficient.

After a few days of CPU time(!), I was able to obtain something that resembled Mona Lisa after running 4 generations of life.

<video loop autoplay muted> <source src="/uploads/simplescreenrecorder-2021-02-23_18-21-21.mp4" type="video/mp4" /> </video>

This was reassuring that my algorithm did indeed work, but I realize I made a bunch of mistakes and of course it's not really scalable.

## Dithering

Target Mona Lisa against which our random state was compared with was the medium resolution version taken from Wikipedia. 

![](/uploads/screenshot-from-2021-02-23-18-38-08.png)

or rather

![](/uploads/screenshot-from-2021-02-23-18-38-08-copy.png)

I think when you're comparing against boolean variables, It's better that we have something in two colors, than the whole gray scale range. Simply rounding (which is what I did) these gray scale values to either be black or while seems to remove a lot of details.

![](/uploads/screenshot-from-2021-02-23-18-39-11.png)

We could just not round at all, and compare against the grayscale version. However, I found that the best results are obtained when we use a rasterized version.

![](/uploads/screenshot-from-2021-02-23-19-04-26.png)

This image is a perfect array of 0s and 1s and should give us a better fitting life state. At highest resolutions, it looks a lot better. We need to scale of algorithm to operate at this level too.

![](/uploads/screenshot-from-2021-02-23-18-54-34.png)

### Garden of Eden

Not every random matrix of 0s and 1s are a valid Game of Life state. States that can never be an nth generation of any cellular automata are called Garden of Edens. It is almost impossible that our dithered Mona Lisa is a valid Game of Life generation. We can only hope to have a solution that's approximately close to the target. 

This is a zoomed portion of the 4th generation of the state we just prepared.

![](/uploads/screenshot-from-2021-02-23-19-08-47.png)

As you can see, it's impossible to get a continuous array of white cells because they will be killed off by the overpopulation rule. Completely dark areas are stable in life. The end result will be a higher contrast, but slightly darkened version of Mona Lisa. At higher resolutions, this effect is not as apparent.

### Scaling Up - Parallelization with JAX

The single core unvectorized version is extremely slow. I tried running this in both my 8th gen Core i7 and the Google Colab CPU machines, but you need to wait for hours/days (depending on target resolution) to get something that resembles the original.

Fortunately, This problem is well suited for parallelization. JAX is a python library that lets you use a version of numpy and compile it to highly vectorized code that can be run on a GPU/TPU. We need to rework this algorithm for a GPU.

GPUs generally suited to high-throughput type computations that exhibit data-parallelism to exploit the wide vector width SIMD (Single Instruction Multiple Data) architecture.

We extrude the `target`(Mona Lisa) and `canvas`(initial random state) to 3rd dimension with 3rd dimension being `batch_size` long.

![](/uploads/untssitled-another-copy.png)

![](/uploads/untssitled-copy.png)

The initial canvas will be completely random(unlike the figure). We set `best_canvas` to the inital canvas before our hill climbing loop.

Also, for every loop iteration, we need to produce a random 3D array called modifier with this property: Each slice across the 3rd dimension will be a field of zeros with a single one place at a random location.

![](/uploads/untssitled-3rd-copy.png)

Something like (with shape 5, 3, 2. batch_size being 5)

    array([[[1, 0],
            [0, 0],
            [0, 0]],
    
           [[1, 0],
            [0, 0],
            [0, 0]],
    
           [[0, 0],
            [0, 1],
            [0, 0]],
    
           [[0, 1],
            [0, 0],
            [0, 0]],
    
           [[1, 0],
            [0, 0],
            [0, 0]]])

The idea is that in every loop, we use the random modifier to calculate the next set of neihbours from our best matched like this `canvas = (best_canvas + modifier)%2`.

We compute n generations of game of life across every slice of this modified canvas. Then, we do a 3D RMSE (mean being calculated for the slice only) vs the nth generation canvas vs Mona Lisa , and find the one with the canvas slice with the lowest error. This is then set to best_canvas and the loop repeats till a finite number of iterations pass.

