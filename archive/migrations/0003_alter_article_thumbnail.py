# Generated by Django 4.1.7 on 2023-03-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='archive'),
        ),
    ]
