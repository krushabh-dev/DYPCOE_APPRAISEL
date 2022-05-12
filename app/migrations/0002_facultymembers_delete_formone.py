# Generated by Django 4.0.3 on 2022-03-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('claimedscore', models.IntegerField()),
                ('givenscore', models.IntegerField()),
                ('performace', models.CharField(max_length=20)),
                ('formstatus', models.IntegerField()),
                ('lastupdated', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='FormOne',
        ),
    ]
