# Generated by Django 4.0.5 on 2022-07-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_groupmodel_does_it_affect_groupmodel_nature_of_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('revenue', models.CharField(max_length=225)),
                ('nonrevenue', models.CharField(max_length=225)),
            ],
        ),
    ]