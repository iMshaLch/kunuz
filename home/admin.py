from django.contrib import admin
from .models import Post, Types, Locations, Tag

admin.site.register(Tag)
admin.site.register(Types)
admin.site.register(Post)
admin.site.register(Locations)
