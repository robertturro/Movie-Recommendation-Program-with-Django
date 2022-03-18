# Generated by Django 4.0.2 on 2022-03-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_input', models.CharField(max_length=100)),
                ('release_year', models.FloatField()),
                ('result', models.CharField(max_length=100)),
                ('overview', models.CharField(default='None', max_length=3000)),
            ],
        ),
    ]
