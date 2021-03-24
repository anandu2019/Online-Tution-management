from django.contrib import admin
from .models import userdetails,marksheet,Note_updated

# Register your models here
admin.site.register(userdetails)
admin.site.register(marksheet)
admin.site.register(Note_updated)