# Generated by Django 5.1.1 on 2024-09-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_group_manufacturer_car_membership_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='name',
            field=models.CharField(help_text='Nhập tên của loại trái cây', max_length=100, unique=True, verbose_name='Tên loại trái cây'),
        ),
    ]
