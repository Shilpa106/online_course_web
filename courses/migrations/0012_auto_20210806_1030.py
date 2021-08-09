# Generated by Django 3.2.5 on 2021-08-06 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.usercourse'),
        ),
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('discount', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='courses.course')),
            ],
        ),
    ]
