# Generated by Django 2.1 on 2018-08-03 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilities', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms_description', models.CharField(max_length=200)),
                ('rooms_amount', models.PositiveSmallIntegerField()),
                ('rooms_bed', models.PositiveSmallIntegerField()),
                ('rooms_personnel', models.PositiveSmallIntegerField()),
                ('rooms_bathroom', models.PositiveSmallIntegerField()),
                ('rooms_type', models.CharField(choices=[('AP', '아파트'), ('HO', '주택'), ('OR', '원룸'), ('GH', '게스트하우스')], default='OR', max_length=2)),
                ('check_in_minimum', models.PositiveSmallIntegerField(default=1)),
                ('check_in_maximum', models.PositiveSmallIntegerField(default=3)),
                ('days_price', models.PositiveIntegerField()),
                ('refund', models.TextField()),
                ('address_country', models.CharField(max_length=100)),
                ('address_city', models.CharField(max_length=50)),
                ('address_district01', models.CharField(max_length=100)),
                ('address_district02', models.CharField(max_length=100)),
                ('address_detail', models.CharField(max_length=100)),
                ('address_latitude', models.DecimalField(decimal_places=14, max_digits=16)),
                ('address_longitude', models.DecimalField(decimal_places=14, max_digits=17)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_cover', models.ImageField(blank=True, upload_to='room_image_cover')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='rooms.RoomDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms_name', models.CharField(max_length=50)),
                ('tag', models.CharField(blank=True, max_length=50)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='with_host', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='roomdetail',
            name='rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='with_rooms', to='rooms.Rooms'),
        ),
        migrations.AddField(
            model_name='roomdetail',
            name='rooms_facilities',
            field=models.ManyToManyField(blank=True, related_name='rooms_facilities', to='rooms.Facilities'),
        ),
    ]
