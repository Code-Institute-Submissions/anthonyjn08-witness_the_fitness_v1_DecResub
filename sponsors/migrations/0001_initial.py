# Generated by Django 3.2 on 2022-12-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=100)),
                ('sponsor_bio', models.TextField()),
                ('sponsor_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('sponsor_website', models.TextField()),
            ],
            options={
                'verbose_name': 'Sponsor',
                'db_table': 'Sponsors',
            },
        ),
    ]
