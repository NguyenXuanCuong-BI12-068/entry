# Generated by Django 4.2.11 on 2024-06-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcnqsd', '0002_remove_folderfilemodel_file_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='folderfilemodel',
            name='page',
            field=models.IntegerField(null=True),
        ),
    ]
