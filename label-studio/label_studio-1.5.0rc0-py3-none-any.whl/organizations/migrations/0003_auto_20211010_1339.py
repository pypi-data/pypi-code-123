# Generated by Django 3.1.13 on 2021-10-10 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20210310_2044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationmember',
            options={'ordering': ['pk']},
        ),
    ]
