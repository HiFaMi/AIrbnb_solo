# Generated by Django 2.1 on 2018-08-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='room_image',
            field=models.ImageField(max_length=255, upload_to='room_profile_image', verbose_name='숙소 프로필 이미지를 업로드 해주세요'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='rooms_description',
            field=models.TextField(help_text='당신의 숙소를 소개하세요, 게스트의 흥미를 유발하는것이 중요합니다.', verbose_name='숙소 개요'),
        ),
    ]
