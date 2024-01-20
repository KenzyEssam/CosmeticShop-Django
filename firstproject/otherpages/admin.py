from django.contrib import admin

# Register your models here.
from .models import Blog,Blog_slider
from .models import Team
from .models import about_header
from .models import AboutUs,Card,Messagee




admin.site.register(Blog)
admin.site.register(Messagee)
admin.site.register(Blog_slider)
admin.site.register(AboutUs)
admin.site.register(Card)
admin.site.register(Team)
admin.site.register(about_header)


