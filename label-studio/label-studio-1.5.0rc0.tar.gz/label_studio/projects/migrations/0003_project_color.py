# Generated by Django 3.1.4 on 2021-03-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210304_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.CharField(blank=True, default='#FFFFFF', max_length=16, null=True, verbose_name='color'),
        ),
    ]
