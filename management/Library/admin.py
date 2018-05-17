from __future__ import unicode_literals
from django.contrib import admin
from Library.models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Issue_Books)
admin.site.register(Return_Books)
