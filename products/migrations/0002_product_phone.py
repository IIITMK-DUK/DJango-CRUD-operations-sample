# Generated by Django 3.2 on 2021-07-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.DecimalField(blank=True, decimal_places=0, default=9459281202, max_digits=10, verbose_name='Phone'),
            preserve_default=False,
        ),
    ]
