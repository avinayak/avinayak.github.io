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
3. Invert a single cell at a random location. 
4. Create a copy of this matrix.
5. Run N generations of Game of Life on the matrix
6. Compute a score of how close the matrix is with the target.
   1. If the score is less than best_score
      1. Set it as best score and set the copy from step 4 as best-result.
   2.  else
      1. Copy best result to current matrix.
7. Repeat 3

Here's the important bits of code I used. Complete version of this POC is available here.

    while best_score>0.23:
        states = np.tile(np.copy(best_seed), (batch_size, 1, 1))
        rms_errors = []
        for i in range(len(states)):
            states[i] = perturbate(states[i], (m,n))
            rms = rmse(target, nth_generation(np.copy(states[i])))
            rms_errors.append(rms)
        lowest = min(rms_errors)
        if lowest < best_score:
            best_score = lowest
            best = rms_errors.index(lowest)
            best_state = states[best]
            clear_output(wait=True)
            print("lowest score: ", best_score)