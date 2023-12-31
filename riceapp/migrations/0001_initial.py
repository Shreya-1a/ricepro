# Generated by Django 5.0 on 2023-12-08 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Godown',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('sell_id', models.AutoField(primary_key=True, serialize=False)),
                ('sell_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('purchase_cost', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.category')),
                ('godown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.godown')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riceapp.product')),
            ],
        ),
    ]
