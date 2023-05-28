from django.contrib import admin
from .models import Post

@admin.register(Post) #! estefade az in dastor bejaye = admin.site.register(Post, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', ) #! namayeshe ajza dar panele admin
    ordering = ('status', ) #! moratab kardane khodkar,,,,( '-status' = baraxs sort mikone)

# admin.site.register(Post, PostAdmin)

# Register your models here.
