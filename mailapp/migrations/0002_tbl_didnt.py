# Generated by Django 5.0 on 2024-02-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_didnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=50)),
                ('regDte', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_didnt',
            },
        ),
    ]
