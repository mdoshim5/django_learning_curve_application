# Generated by Django 3.2.9 on 2022-01-25 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('publish_date', models.DateTimeField()),
                ('votes_total', models.IntegerField(default=1)),
                ('body', models.TextField()),
                ('icon', models.ImageField(upload_to='images/')),
                ('image', models.ImageField(upload_to='images/')),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
