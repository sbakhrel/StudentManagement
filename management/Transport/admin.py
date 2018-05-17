from __future__ import unicode_literals
from django.contrib import admin
from Transport.models import *
# Register your models here.


admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(Driver)
admin.site.register(Transport_Allocation)
