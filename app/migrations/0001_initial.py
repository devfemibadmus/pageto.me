# Generated by Django 5.1.4 on 2025-01-11 09:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('preview_image', models.ImageField(upload_to='templates/')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('views', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LinkAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=100)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='app.link')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='template_rows/')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('position', models.PositiveIntegerField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='app.template')),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='template_row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='app.templaterow'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.template')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]