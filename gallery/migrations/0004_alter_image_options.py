# Generated by Django 3.2 on 2022-05-28 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date']},
        ),
    ]