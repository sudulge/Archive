# Generated by Django 4.1.7 on 2023-03-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]