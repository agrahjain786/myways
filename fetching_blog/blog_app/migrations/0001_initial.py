# Generated by Django 4.2.8 on 2024-03-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostTable',
            fields=[
                ('userId', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
    ]
