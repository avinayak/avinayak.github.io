---
title: A Music player that can uplift your mood
date: 2013-10-20T00:00:00.000+00:00
categories:
- programming
layout: post
subtitle: SVM Failure

---
This is the beginning of a big project I’m undertaking as a part of my Blackberry 10 Internship. It is a music player, which can analyze mood of a given track, and also guess our mood from the songs played. It uses support vector machine based regression to locate a song’s mood.

It had lots of cool (*planned*) features like an ‘Uplift Me’, which plays a sad song at first, but slowly plays happy songs!


![My helpful screenshot](/assets/images/mood.png)

The screenshot below is my webapp for training the algorithm. Kind of like a *crowdsourcing* platform.

![My helpful screenshot](/assets/images/ut.png)

Anyone can go to the page, and click the play button and play a song(randomly) and guess the song’s mood. The Webapp written in flask, saved all this information to an sqlite table in my laptop. I placed this in our college’s network for everyone to consume, and at the end of the day I had ~15% of my music collection of 4400 songs “moodated”. Hopefully, I’ll train the algorithm completely in a few weeks time.

## Edit

This project failed miserably :(

I underestimated the kind of effort & feature extraction involved in music. Most songs won’t have a single mood throughout. The next step after getting the songs tagged with mood information is to extract ~ 60 parameters for individual tracks, such as pitch, frequency, timber etc. and train the SVM with this.

Unfortunately, the model never converged well, and I got sidetracked by other projects.