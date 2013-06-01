---
layout: default
---

<!-- Cuando sea necesario, lo voy a habilitar.
<div class="toc">
  <ul>
    <li><a href="#">ngResource</a></li>
  </ul>
</div>
-->

AngularJS
=========

En esta página he intentado de recopilar pequeños trozos de conocimiento que he
ido adquiriendo a medida utilizo más el framework.

ngResource
----------

La documentación oficial se encuentra en:

<p class="indent">
  <a href="http://docs.angularjs.org/api/ngResource.$resource" target="_blank">
    http://docs.angularjs.org/api/ngResource.$resource
  </a>
</p>

### Instanciar un resource a partir de un arreglo asociativo

Asumiendo que existe un `resource` ya definido (en este ejemplo se llama
`Pregunta`):

{% highlight javascript %}
var Pregunta = $resource('/pregunta/:preguntaId', { preguntaId: '@id' });
{% endhighlight %}

Si necesitás crear una nueva instancia de ese `resource` a partir de un arreglo
asociativo, podés hacer lo siguiente:

{% highlight javascript %}
var pregunta = new Pregunta({
  texto: '¿Cuántos años tienes?',
  tipo: 'número'
});
pregunta.$save();
{% endhighlight %}
