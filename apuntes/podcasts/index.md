---
layout: page
title: Podcasts
categories: [apuntes, podcasts]
---

Compilación de apuntes personales que he tomado al escuchar algunos podcasts. No
son una traducción exacta de lo que se dice. Los publico para utilizarlos como
referencia en el futuro, y por si a alguien le parece útil.

## Scott Shaw: Are You Infected By Microservice Envy?

<iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/206283659&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false"></iframe>

1. Para empezar a utilizar microservicios ([*microservices*][1]) es recomendado
   primero ser practicante de [*continuous delivery*][2], haber automatizado la
   infraestructura, entender REST y la integración de sistemas.

2. Ley de Postel o [El Principio de Robustez][3]: se conservador en lo que
   envías, se liberal en lo que aceptas.

3. Los microservicios son una inversión a largo plazo: un equipo tardó seis meses
   en desarrollar los primeros dos servicios, pero en los seis meses siguientes
   llegaron a tener alrededor de cincuenta servicios.

4. Si no practicas [*Domain-driven design*][4] en tu sistema monolítico,
   probablemente no vas a ser exitoso descomponiéndolo en microservicios.

5. Una buena forma de empezar a utilizar microservicios es refactorizando tu
   sistema monolítico para que exista una clara separación de [*bounded
   contexts*][5], y un entendimiento de cómo cada uno de ellos expone su
   información a los otros.

6. Utilizar [*Domain-driven design* para descomponer un sistema monolítico en
   microservicios][6].

7. Es más fácil [empezar con un sistema monolítico y descomponerlo en
   microservicios][7], ya que hay un mejor entendimiento del dominio.

8. Si estás gastando demasiado tiempo corrigiendo el proceso de *deployment* o
   tus entornos de desarrollo, talvez no estás preparado para usar
   microservicios.

9. La idea de microservicios es antigua y [se remonta a SOA (*Service-oriented
   architecture*)][8], la diferencia es que ahora tenemos más herramientas y un
   mejor conocimiento de cómo construir sistemas distribuidos a gran escala.

[1]: http://martinfowler.com/microservices
[2]: http://martinfowler.com/bliki/ContinuousDelivery.html
[3]: https://en.wikipedia.org/wiki/Robustness_principle
[4]: https://domainlanguage.com/ddd/
[5]: http://martinfowler.com/bliki/BoundedContext.html
[6]: https://www.thoughtworks.com/insights/blog/domain-driven-design-services-architecture
[7]: http://martinfowler.com/bliki/MonolithFirst.html
[8]: http://martinfowler.com/articles/microservices.html#MicroservicesAndSoa
