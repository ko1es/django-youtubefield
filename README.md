django-youtubefield
===================

Django youtube url field

Installation
============

::

    pip install git+git://github.com/ko1es/django-youtubefield.git


Basic usage
===========

Use it like any regular model field:

    from youtubeurl_field.modelfields import YoutubeUrlField
    class Item(models.Model):
        name = models.CharField(max_length=255)
        video = YoutubeUrlField(blank=True, null=True)


Template usage
===========

Use .embed_url in your templates to insert it in <iframe src >

		{% if item.video %}
		<div class="flex-video widescreen">
			<iframe width="500" height="281" src="{{ item.video.embed_url }}" frameborder="0" allowfullscreen></iframe>
		</div>
		{% else %}

