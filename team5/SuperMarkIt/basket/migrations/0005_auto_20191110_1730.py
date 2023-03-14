# Generated by Django 2.2.6 on 2019-11-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_auto_20191110_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='items',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='products',
        ),
        migrations.AddField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, to='basket.Basket'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='product_total',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
