# Generated by Django 3.2 on 2022-02-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='genus',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
