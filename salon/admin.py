from django.contrib import admin
from .models import Branch, Services, Master, Customer, Record

admin.site.register(Branch)
admin.site.register(Services)
admin.site.register(Master)
admin.site.register(Customer)
admin.site.register(Record)

