# Generated by Django 3.2.12 on 2022-02-10 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220210_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='i_list',
            new_name='industry_list',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='phnum',
            new_name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='company',
            name='body',
        ),
    ]