# Generated by Django 4.0.4 on 2022-04-12 16:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userattempt',
            unique_together={('user', 'question', 'answer')},
        ),
    ]
