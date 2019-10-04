from django.contrib import admin
from first_app.models import WebPage,AccessRecord,Topic
# Register your models here.
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(Topic)
