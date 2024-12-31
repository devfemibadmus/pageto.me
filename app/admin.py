from django.contrib import admin
from .models import Template, TemplateRow, UserProfile, Link, LinkAnalytics


admin.site.register(Link)
admin.site.register(Template)
admin.site.register(TemplateRow)
admin.site.register(UserProfile)
admin.site.register(LinkAnalytics)

# Register your models here.
