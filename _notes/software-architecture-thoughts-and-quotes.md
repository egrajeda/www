---
layout: post
title: "Software Architecture: Thoughts and quotes"
tags: [architecture]
updated: 2020-04-11
language: en
---

<p class="lead">
  Collection of interesting thoughts and quotes about Software Architecture, collected from videos or articles.
</p>

----

[Avoiding Microservice Megadisasters](https://www.youtube.com/watch?v=gfh-VCTwMw8) by [Jimmy
Bogard](https://jimmybogard.com) talks about how on a Microservice Architecture, when you do a service call, the service
should be able to answer your request without the need of an additional service call of its own.

It also talks about the assumption that replicating data is wrong. It gives an example on how data replication allowed
to get rid of service calls inside a service meant to provide search functionalities.

----

[Choosing The Right Deployment Strategy](https://fosdem.org/2020/schedule/event/choosing_the_right_deployment_strategy)
by [Viktor Farcic](https://technologyconversations.com) concludes with the following recommendations:

* Choose the "Recreate" strategy when working with legacy applications that are stateful without replication.
* Choose the "Rolling update" strategy with cloud-native applications which cannot use canary deployments.
* Choose the "Canary" strategy when you need the additional control when to roll forward and when to roll back.
* Choose the "Serverless" strategy when you need excellent scaling capabilities or when the application is not in
  constant use.

----

[Cultivating Production Excellence](https://www.youtube.com/watch?v=HiDqrqa34Ls) by [Liz
Fong-Jones](https://www.lizthegrey.com/) talks about key elements to achieve production excellence:

1. Know when our systems are too broken: systems are always failing, we need to define what's acceptable through good
   SLOs.
2. Be able to debug our systems: support debugging our systems in production through good observability.
3. Cross-team collaboration: work with other teams, rotate the on-call, share knowledge through documentation.
4. Eliminate (unnecessary) complexity: address risks that threathen the SLO.

A nice quote around observability I liked was: *"Our services must be observable. Our systems have to be able to explain
themselves to us and answer our questions using the telemetry they're already exporting, rather than us having to create
new code in order to understand our services"*.
