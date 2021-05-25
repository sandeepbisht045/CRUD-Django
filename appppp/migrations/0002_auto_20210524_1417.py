# Generated by Django 3.2.2 on 2021-05-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appppp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=33)),
                ('singer', models.CharField(max_length=23)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
