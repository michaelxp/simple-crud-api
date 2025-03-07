# Generated by Django 5.0.4 on 2024-04-05 17:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id_game', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=1024)),
                ('release_year', models.IntegerField()),
                ('developer', models.CharField(max_length=32)),
            ],
        ),
    ]
