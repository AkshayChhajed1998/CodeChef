# Generated by Django 2.0.8 on 2019-02-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('question_is_active', models.BooleanField(default=True)),
                ('language_option', models.BooleanField(default=True)),
            ],
        ),
    ]
