# Generated by Django 5.0.3 on 2024-03-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataentry',
            name='pendente',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
