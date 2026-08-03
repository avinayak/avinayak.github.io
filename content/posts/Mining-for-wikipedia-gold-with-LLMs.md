---
title: Mining for wikipedia gold with LLMs
date: 2026-03-28T07:00:00.000Z
category: Programming
tags: LLM, AI, Wikipedia
status: published
---

Wikipedia has [Special:Random](https://en.wikipedia.org/wiki/Special:Random) which will take you to a random article. I thought these random articles would be a great way to explore wikipedia and discover new things, But because of the scale of wikipedia, most of the articles were not interesting reads. Bulk of wikipedia is just random [place pages with 1-2 lines of information](https://en.wikipedia.org/wiki/Moothakunnam).

My first attempt to kind of make wikipedia discoverable was wikidive.net, a platform that lets you rabbithole into wikipedia articles. You can start with a random topic or article and the app gives you two related articles to choose from. You can keep going down the rabbit hole until you find something interesting. The whole discovery portion is LLM assisted as in It asks a medium powered LLM a prompt like.

> I am currently reading "No-cloning theorem". I got here from the rabbithole "Computer science -> Garbled circuit -> Secure multi-party computation -> Homomorphic encryption -> OpenFHE -> Post-quantum cryptography -> Quantum volume -> Quantum coin flipping -> Magic state distillation -> No-cloning theorem". Here are my related articles: ["Quantum teleportation", "Bell's theorem", "Spin", "Quantum key distribution", "Nitrogen Vacancy center" .... ]. Pick 2 articles that are most related to "No-cloning theorem". Just reply with the article names and nothing else.

This worked pretty well, but it still failed to surface niche and articles that are really not well linked to anything else, but still are interesting to read.

So, for the next round, I wanted to go for something different. Back in February I came across this list called the [Archive](https://endwalker.com/archive.html). It's a list of some interesting and weird(ish) wikipedia articles. I thought it would be fun to see if I can use an LLM to find more articles like these. Also during this time I saw this [video by PrallelPipes](https://youtu.be/6lQ1V5yg9sE). These two contained common wiki gold like

- [Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo](https://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo)
- [Blue peacock](https://en.wikipedia.org/wiki/Blue_peacock)
- [Dord](https://en.wikipedia.org/wiki/Dord)
