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

[Avoiding Microservice Megadisasters](https://www.youtube.com/watch?v=gfh-VCTwMw8) by [Jimmy Bogard](https://jimmybogard.com)
talks about how on a Microservice Architecture, when you do a service call, the service should be able to answer your request
without the need of an additional service call of its own.

It also talks about the assumption that replicating data is wrong. It gives an example on how data replication allowed to get
rid of service calls inside a service meant to provide search functionalities.

<hr class="small" />

[Choosing The Right Deployment Strategy](https://fosdem.org/2020/schedule/event/choosing_the_right_deployment_strategy) by
[Viktor Farcic](https://technologyconversations.com) concludes with:

  * Choose the "Recreate" strategy when working with legacy applications that are stateful without replication.
  * Choose the "Rolling update" strategy with cloud-native applications which cannot use canary deployments.
  * Choose the "Canary" strategy when you need the additional control when to roll forward and when to roll back.
  * Choose the "Serverless" strategy when you need excellent scaling capabilities or when the application is not in constant use.