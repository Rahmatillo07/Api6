# Generated by Django 5.0.6 on 2024-07-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_amenity_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('star', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=20)),
                ('telegram', models.CharField(max_length=20)),
                ('you_tube', models.CharField(max_length=20)),
                ('facebook', models.CharField(max_length=20)),
                ('tok_tok', models.CharField(max_length=20)),
            ],
        ),
    ]
