---
layout: page
title: Podcasts
---

Compilación de apuntes personales que he tomado al escuchar algunos podcasts. No
son una traducción exacta de lo que se dice. Los publico para utilizarlos como
referencia en el futuro, y por si a alguien le parece útil.

<br />

<a href="https://www.thoughtworks.com/insights/blog/podcast-are-you-infected-microservice-envy" id="microservice-envy" class="podcast">
  <img src="//i2.sndcdn.com/artworks-000117444986-ewbn0i-t200x200.jpg" />
  <span class="title">Are You Infected by Microservice Envy?</span>
  <span class="author">Director of Technology, Australia at Thoughtworks</span>
</a>

* Para empezar a utilizar microservicios ([*microservices*][1]) es recomendado
  primero ser practicante de [*continuous delivery*][2], haber automatizado la
  infraestructura, entender REST y la integración de sistemas.

* Ley de Postel o [El Principio de Robustez][3]: se conservador en lo que
  envías, se liberal en lo que aceptas.

* Los microservicios son una inversión a largo plazo: un equipo tardó seis meses
  en desarrollar los primeros dos servicios, pero en los seis meses siguientes
  llegaron a tener alrededor de cincuenta servicios.

* Si no practicas [*Domain-driven design*][4] en tu sistema monolítico,
  probablemente no vas a ser exitoso descomponiéndolo en microservicios.

* Una buena forma de empezar a utilizar microservicios es refactorizando tu
  sistema monolítico para que exista una clara separación de [*bounded
  contexts*][5], y un entendimiento de cómo cada uno de ellos expone su
  información a los otros.

* Utilizar [*Domain-driven design* para descomponer un sistema monolítico en
  microservicios][6].

* Es más fácil [empezar con un sistema monolítico y descomponerlo en
  microservicios][7], ya que hay un mejor entendimiento del dominio.

* Si estás gastando demasiado tiempo corrigiendo el proceso de *deployment* o
  tus entornos de desarrollo, talvez no estás preparado para usar
  microservicios.

* La idea de microservicios es antigua y [se remonta a SOA (*Service-oriented
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
