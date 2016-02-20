---
layout: post
title: Configuración de un entorno de prueba de ELK con Filebeat
---

En este documento detallo, tanto para referencia personal como para cualquier
otra persona que le pueda servir, los primeros pasos que seguí al experimentar
con Elasticsearch, Logstash, Kibana y Filebeat. La meta será instalar ELK y
Filebeat, enviar datos de uno a otro, y configurar Kibana para verificar que los
datos han sido enviados exitosamente.

## Instalación de Elasticsearch, Logstash y Kibana

La sigla ELK corresponde a Elasticsearch, Logstash y Kibana, tres herramientas
desarrolladas por una compañía llamada [Elastic][11]. Al ser utilizadas en
conjunto, son una de las opciones disponibles para consolidar archivos de logs
generados en múltiples servidores.

[Elasticsearch][8] es una *search engine*, y en nuestro caso es donde se
almacenarán los datos que enviaremos a través de Logstash. [Logstash][9] es un
servicio intermediario que recibirá nuestros logs, extraerá la información
importante y la almacenará en Elasticsearch. [Kibana][10] es la herramienta que
nos permite visualizar la información que hemos enviado a Elasticsearch a través
de Logstash.

Para crear un entorno de prueba con ELK vamos a utilizar [Docker][1] y la imagen
[sebp/elk][2]. Primero descargamos la imagen:

```
egrajeda@host:~$ docker pull sebp/elk
```

<div class="info">
  <p>Para descargar exactamente la misma imagen que se utilizó al escribir este
  documento utiliza:</p>

  <div class="highlight">
    <pre><code class="language-text" data-lang="text">egrajeda@host:~$ docker pull sebp/elk@sha256:919c9e3e9ac95f4860fe2c8d3ec480ce1e1d9b39939adb76649b4257586a53d8</code></pre>
  </div>
</div>

Después creamos el contenedor a partir de la imagen que descargamos:

```
egrajeda@host:~$ docker run -d --name elk sebp/elk
```

Para este tipo de pruebas yo no acostumbro exponer los puertos del contenedor a
través de `localhost` (p. ej.: `docker run -p 5044:5044 ...`) sino que accedo al
contenedor a través de la IP que el sistema le asigna:

```
egrajeda@host:~$ docker exec elk ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
11: eth0@if12: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 11:11:11:11:11:11 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 2222::22:2222:2222:2/64 scope link
       valid_lft forever preferred_lft forever
```

En este caso la IP es `172.17.0.2`. Verificamos que el puerto de Logstash
utilizado por Filebeat esté funcionando:

```
egrajeda@host:~$ nc -vv 172.17.0.2 5044
Warning: Inverse name lookup failed for `172.17.0.2'
172.17.0.2 5044 (lxi-evntsvc) open
```

## Instalación de Filebeat

[Filebeat][12] es la herramienta (también desarrollada por [Elastic][11]) que se
utiliza en los servidores clientes para constantemente enviar sus archivos de
logs al servidor ELK.

[Descarga e instala Filebeat][3] de acuerdo a tu sistema operativo. Una vez
hecho esto, crearemos una carpeta para hacer las pruebas y dentro de ella
creamos el archivo de configuración vacío:

```
egrajeda@host:~$ mkdir -p labs/elk-filebeat
egrajeda@host:~$ cd labs/elk-filebeat
egrajeda@host:~/labs/elk-filebeat$ touch filebeat.yml
egrajeda@host:~/labs/elk-filebeat$ ls
filebeat.yml
```

La configuración de Filebeat consiste principalmente en dos partes: entradas y
salidas. Las entradas son nuestros archivos de logs, y la salida en nuestro caso
es el servidor de Logstash. Cuando Filebeat envíe el contenido de los archivos a
Logstash, se creará un índice en Elasticsearch con el patrón `filebeat-*`.

Antes de empezar a configurar Filebeat, consultemos en Elasticsearch qué
información existe asociada al índice `filebeat-*`:

```
egrajeda@host:~/labs/elk-filebeat$ curl -XGET 'http://172.17.0.2:9200/filebeat-*/_search?pretty'
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 0,
    "successful" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 0,
    "max_score" : 0.0,
    "hits" : [ ]
  }
}
```

Como todavía no hemos enviado nada de información a Logstash, es de esperar que
el índice `filebeat-*` no tenga nada de contenido.

## Configuración del *index template* en Elasticsearch

Antes de enviar información a Logstash deberás configurar el *index template*
para Filebeat en Elasticsearch. Para ello, [tu instalación de Filebeat][7]
incluye un archivo llamado `filebeat.template.json`, cuyo contenido deberás
enviar a Elasticsearch a través de su API:

```
egrajeda@host:~/labs/elk-filebeat$ curl -XPUT 'http://172.17.0.2:9200/_template/filebeat?pretty' -d@/etc/filebeat/filebeat.template.json
{
  "acknowledged" : true
}
```

## Configuración de Filebeat

Para nuestras pruebas empezaremos con la siguiente configuración mínima:

```yaml
filebeat:
    prospectors:
        -
            paths:
                - "access_log"
            input_type: log

output:
    logstash:
        hosts: ["172.17.0.2:5044"]
```

La documentación de Filebeat tiene la explicación completa de las [opciones de
entrada][4] y las [opciones de salida][5], por lo que solamente explicaré dos de
ellas:

1. `paths`: Los archivos cuyo contenido Filebeat enviará a Logstash. Se pueden
   especificar múltiples archivos: uno por línea y deben empezar con `-`.
2. `hosts`: Los servidores Logstash a los cuales conectarse.

{{ site.baseurl }}
<div class="info">
  <p>Para estas pruebas utilicé una versión anonimizada de un subconjunto (3000
  líneas) de <a href="http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html">access
  logs publicados por la NASA</a>. Si deseas usar el mismo archivo,
  <a href="{{ site.baseurl }}/downloads/access_log">descárgalo</a> y guárdalo
  en la carpeta <code>~/labs/elk-filebeat</code>.
</div>

Probemos la configuración ejecutando Filebeat de la siguiente manera:

```
egrajeda@host:~/labs/elk-filebeat$ filebeat -e -c filebeat.yml -d "*"
```

Lo siguiente es lo que significa cada una de las opciones de línea de comando:

1. `-e`: Mostrar la información de depuración en consola (`stderr` para ser
   específico) en lugar de guardarla en un archivo.
2. `-c filebeat.yml`: El archivo de configuración a utilizar.
3. `-d "*"`: Mostrar toda la información de depuración, muy útil cuando se
   están haciendo pruebas.

Después de un momento verás que el siguiente error aparecerá repetidamente en la
consola:

```
single.go:76: INFO Error publishing events (retrying): EOF
single.go:152: INFO send fail
single.go:159: INFO backoff retry: 4s
```

El problema es que nuestro contenedor Docker está configurado para que la
comunicación con Logstash se haga de forma encriptada, pero Filebeat no puede
validar los certificados. Como estamos configurando un entorno de prueba (<u>no
hagas esto en producción</u>), actualizaremos la configuración para ignorar la
validez de los certificados:

```
output:
    logstash:
        hosts: ["172.17.0.2:5044"]
        tls:
            insecure: true
```

<div class="info">
  <p>Si prefieres configurar Filebeat para que reconozca los certificados
  utilizados por nuestro contenedor Docker, puedes seguir
  <a href="http://elk-docker.readthedocs.org/#notes-on-certificates">
    los pasos detallados en su documentación.
  </a></p>
</div>

Tratamos de ejecutar Filebeat de nuevo, y esta vez no debería haber ningún
error:

```
egrajeda@host:~/labs/elk-filebeat$ filebeat -e -c filebeat.yml -d "*"
```

Después de un momento y para verificar que los datos se han cargado
exitosamente, ejecuta de nuevo el siguiente comando:

```
egrajeda@host:~/labs/elk-filebeat$ curl -XGET 'http://172.17.0.2:9200/filebeat-*/_search?pretty'
{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 3000,
    "max_score" : 1.0,
    "hits" : [ {
      "_index" : "filebeat-2016.02.20",
...
```

## Primeros pasos en Kibana

Kibana es la herramienta que nos permite visualizar la información que hemos
enviado a Elasticsearch a través de Logstash. Para abrir Kibana entra a
`https://172.17.0.2:5601`.

La primera vez que entres serás redireccionado a la página de configuración, en
donde deberás especificar el patrón que siguen los índices que deseas analizar.
Como lo vimos anteriormente, Filebeat crea índices bajo el patrón `filebeat-*`.
En la página de configuración aparecerá por defecto el patrón `logstash-*`,
reemplázalo por `filebeat-*`, no modifiques ninguno de los otros campos y haz
clic en **Create**:

![Kibana settings page]({{ site.baseurl }}/images/kibana-settings.png)

Haz ahora clic en **Discover** en la barra superior. Serás redireccionado a una
página desde la cual podrás analizar la información que has enviado:

![Kibana discover page]({{ site.baseurl }}/images/kibana-discover.png)

Si en tus pruebas no logras ver nada, asegúrate que la fecha en la parte superior
derecha (donde en la captura de pantalla dice "*February 19th 2016...*")
corresponda a la fecha en que enviaste la información a Logstash (en la mayoría
de los casos deberá ser **Today**).

Un par de observaciones:

1. Los logs utilizados en estas pruebas son de 1995, pero notarás que en Kibana
   aparecen como que han sido generados ahora. Esto se debe a que todavía no
   hemos configurado Logstash para que sepa qué parte del mensaje corresponde al
   `@timestamp`.
2. A este punto todavía no podrás filtrar por la información contenida en el
   mensaje, como el verbo HTTP o la URL. Para lograr hacer esto, así como en el
   punto anterior, debemos de configurar Logstash para que sepa cómo extraer la
   información del mensaje.

En un futuro documento comentaré mis experiencias al tratar de extraer
información de los mensajes enviados a Logstash.

## Notas adicionales

Los siguientes comandos me resultaron muy útiles durante mi experimentación con
ELK y Filebeat. Si los deseas utilizar en un entorno de producción, <u>asegurate
de leer toda la documentación oficial</u>, ya que la mayoría de ellos podría
corromper (o eliminar) la información que ya tienes almacenada.

### Eliminar todos los datos

Para eliminar todos los datos cargados por Filebeat, pídele a Elasticsearch a
través de su API que elimine toda la información asociada a los índices con el
patrón `filebeat-*`:

```
egrajeda@host:~$ curl -XDELETE 'http://172.17.0.2:9200/filebeat-*'
```

### Reenviar un archivo

Filebeat almacena información de los archivos que ha enviado previamente en un
archivo llamado `.filebeat`. Este archivo contiene información en formato JSON,
y se encuentra en el directorio donde ha sido ejecutado Filebeat (p. ej.:
`~/labs/elk-filebeat`).

Si quieres volver a enviar un archivo que Filebeat ya ha enviado previamente,
la opción más fácil es eliminar el archivo `.filebeat`. Opcionalmente puedes
editar el archivo y eliminar únicamente los registros que desees.

### Filebeat ignora algunos archivos

Si al ejecutar Filebeat ves un mensaje como el siguiente:

```
prospector.go:306: DBG  Skipping file (older than ignore older of 24h0m0s, 106h4m40.808875202s): ...
```

Es porque por defecto Filebeat está configurado para ignorar archivos cuya
última fecha de modificación es más de un día. Para solucionar este problema
puedes utilizar `touch` para actualizar la fecha de modificación:

```
egrajeda@host:~/labs/elk-filebeat$ touch access_log
```

O puedes [configurar la opción de entrada `ignore_older`][13].

[1]: https://www.docker.com
[2]: https://hub.docker.com/r/sebp/elk
[3]: https://www.elastic.co/downloads/beats/filebeat
[4]: https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html
[5]: https://www.elastic.co/guide/en/beats/filebeat/current/logstash-output.html
[6]: http://elk-docker.readthedocs.org/#notes-on-certificates
[7]: https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-template.html
[8]: https://www.elastic.co/products/elasticsearch
[9]: https://www.elastic.co/products/logstash
[10]: https://www.elastic.co/products/kibana
[11]: https://www.elastic.co
[12]: https://www.elastic.co/products/beats
[13]: https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html#_ignore_older
