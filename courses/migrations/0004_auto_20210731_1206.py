# Generated by Django 3.2.5 on 2021-07-31 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prequisite',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100),
        ),
    ]
