# Generated by Django 3.2.5 on 2021-08-03 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_payment_usercourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]