# Generated by Django 4.0.5 on 2022-07-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_costcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costcentr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('emply', models.CharField(max_length=225)),
            ],
        ),
    ]
