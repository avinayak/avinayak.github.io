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

After a few days or so(!), I was able to obtain something that resembled monalisa after running 4 generations of life.

<video loop autoplay muted> <source src="/uploads/simplescreenrecorder-2021-02-23_18-21-21.mp4" type="video/mp4" /> </video>

This was reassuring that my algorithm did indeed work, but I realize I made a buch of mistakes.

### Dithering

Target monalisa against which our random state was compared with was the medium resolution version taken from wikipedia. 

![](/uploads/screenshot-from-2021-02-23-18-38-08.png)

or rather

![](/uploads/screenshot-from-2021-02-23-18-38-08-copy.png)

I think when you're comparing against boolean variables, It's better that we have something in two colors, than the whole grayscale range. Simply rounding (which is what I did) these grayscale values to either be black or while seems to remove a lot of details.

![](/uploads/screenshot-from-2021-02-23-18-39-11.png)

We could just not round at all, and compare against the grayscale version. However, I found that the best results are obtained when we use a rasterized version.

![](/uploads/screenshot-from-2021-02-23-18-54-34.png)

This image is a perfect array of 0s and 1s and should give us a better fitting life state.