# Generated by Django 4.0.5 on 2022-07-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_costcentr'),
    ]

    operations = [
        migrations.CreateModel(
            name='grp_alter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('nature', models.CharField(max_length=225)),
                ('grp', models.CharField(max_length=225)),
                ('nett', models.CharField(max_length=225)),
                ('used', models.CharField(max_length=225)),
                ('method', models.CharField(max_length=225)),
            ],
        ),
    ]
