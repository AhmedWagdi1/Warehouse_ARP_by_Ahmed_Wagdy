# Generated by Django 2.2 on 2019-04-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0082_auto_20190430_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellinvoice',
            name='paid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sellinvoice',
            name='unpaid',
            field=models.IntegerField(),
        ),
    ]
