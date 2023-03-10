# Generated by Django 4.1.7 on 2023-02-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depertment',
            fields=[
                ('DepertmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepertmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Depertment', models.CharField(max_length=500)),
                ('DataOfJoining', models.DateField()),
                ('photoFileName', models.CharField(max_length=400)),
            ],
        ),
    ]
