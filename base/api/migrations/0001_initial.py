# Generated by Django 4.1.7 on 2023-03-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='samples')),
            ],
        ),
    ]
