# Generated by Django 2.2.9 on 2020-10-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date__date_published']},
        ),
    ]