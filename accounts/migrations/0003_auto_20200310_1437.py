# Generated by Django 2.2.10 on 2020-03-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191205_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='web_page',
            field=models.URLField(null=True),
        ),
    ]
