# Generated by Django 5.1.1 on 2024-09-26 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_fruit_id_alter_fruit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Tên nhóm')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên nhà sản xuất')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Mô hình xe')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.manufacturer', verbose_name='Nhà sản xuất')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(verbose_name='Ngày tham gia')),
                ('invite_reason', models.CharField(max_length=64, verbose_name='Lý do mời')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.group', verbose_name='Nhóm')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.person', verbose_name='Người tham gia')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='newapp.Membership', to='newapp.person', verbose_name='Danh sách thành viên'),
        ),
    ]
