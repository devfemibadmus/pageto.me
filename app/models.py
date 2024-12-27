from django.db import models
from django.contrib.auth.models import User

class Template(models.Model):
    name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to="templates/")

class TemplateRow(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name="rows")
    image = models.ImageField(upload_to="template_rows/", null=True, blank=True)
    title = models.CharField(max_length=100)
    link = models.URLField()
    position = models.PositiveIntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    selected_template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template_row = models.ForeignKey(TemplateRow, on_delete=models.CASCADE, related_name="links")
    url = models.URLField()
    title = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)

class LinkAnalytics(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="analytics")
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=100)
