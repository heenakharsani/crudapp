# Generated by Django 3.1.4 on 2020-12-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254, unique=True)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
