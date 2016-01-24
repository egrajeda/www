---
layout: default
---

i3
==

### 1. Configurar las teclas multimedia

El siguiente snippet asume que no tenemos PulseAudio instalado:

{% highlight %}
bindsym XF86AudioMute        exec --no-startup-id amixer set Master toggle
bindsym XF86AudioLowerVolume exec --no-startup-id amixer set Master 5%-
bindsym XF86AudioRaiseVolume exec --no-startup-id amixer set Master 5%+
bindsym XF86AudioMicMute     exec --no-startup-id amixer set Capture toggle
{% endhighlight %}

### 2. Configurar las teclas de brillo del monitor

Para que el siguiente snippet funcione tenemos que tener instalado los drivers
de nuestra tarjeta de video, que en mi caso es `xf86-video-intel`:

<pre>
  <code>
bindsym XF86MonBrightnessUp   exec xbacklight -inc 20
bindsym XF86MonBrightnessDown exec xbacklight -dec 20
  </code>
</pre>
