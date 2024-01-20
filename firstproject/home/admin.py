from django.contrib import admin

# Register your models here.
from .models import Gallery
from .models import Category
from .models import Header
from .models import Banner


admin.site.register(Gallery)

admin.site.register(Category)

admin.site.register(Header)

admin.site.register(Banner)

