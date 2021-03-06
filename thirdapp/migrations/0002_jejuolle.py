# Generated by Django 3.2.5 on 2022-05-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JejuOlle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=20)),
                ('distance', models.FloatField()),
                ('time_info', models.CharField(max_length=10)),
                ('start_end_info', models.CharField(max_length=30)),
                ('cre_date', models.DateField()),
            ],
            options={
                'db_table': 'shop',
                'managed': False,
            },
        ),
    ]
