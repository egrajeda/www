---
layout: post
title: "Software Architecture: Thoughts and quotes"
tags: [architecture]
updated: 2020-04-06
language: en
---

<p class="lead">
  Collection of interesting thoughts and quotes about Software Architecture, collected from videos or articles.
</p>

<hr />

[Avoiding Microservice Megadisasters](https://www.youtube.com/watch?v=gfh-VCTwMw8) by [Jimmy Bogard](https://jimmybogard.com/)
talks about how on a Microservice Architecture, when you do a service call, the service should be able to answer your request
without the need of an additional service call of its own.

It also talks about the assumption that replicating data is wrong. It gives an example on how data replication allowed to get
rid of service calls inside a service meant to provide search functionalities.
