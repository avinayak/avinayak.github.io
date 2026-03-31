---
title: Mining for wikipedia gold with LLMs
date: 2026-03-28T07:00:00.000Z
category: Programming
tags: LLM, AI, Wikipedia
status: published
---

Wikipedia is awesome. One if the greatest things we have ever done as a civilization. If you know what you want, there's a good chance you can find it on wikipedia. But what if you don't know what you want? What if you just want to explore and discover new things?

Wikipedia has [Special:Random](https://en.wikipedia.org/wiki/Special:Random) which will take you to a random article. I thought these random articles would be a great way to explore wikipedia and discover new things, But because of the scale of wikipedia, most of the articles were not interesting reads. Bulk of wikipedia is just random [place pages with 1-2 lines of information](https://en.wikipedia.org/wiki/Moothakunnam).

My first attempt to kind of make wikipedia discoverable was wikidive.net, a platform that lets you rabbithole into wikipedia articles. You can start with a random topic or article and the app gives you two related articles to choose from. You can keep going down the rabbit hole until you find something interesting. The whole discovery portion is LLM assisted as in It asks a medium powered LLM a prompt like

> I am currently reading "No-cloning theorem". I got here from the rabbithole "Computer science -> Garbled circuit -> Secure multi-party computation -> Homomorphic encryption -> OpenFHE -> Post-quantum cryptography -> Quantum volume -> Quantum coin flipping -> Magic state distillation -> No-cloning theorem". Here are my related articles: ["Quantum teleportation", "Bell's theorem", "Spin", "Quantum key distribution", "Nitrogen Vacancy center" .... ]. Pick 2 articles that are most related to "No-cloning theorem". Just reply with the article names and nothing else.
