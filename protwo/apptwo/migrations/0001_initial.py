# Generated by Django 2.2.5 on 2019-10-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=264)),
                ('Lname', models.CharField(max_length=264)),
                ('Email', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
