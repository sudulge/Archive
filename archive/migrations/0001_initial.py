# Generated by Django 4.1.7 on 2023-03-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
