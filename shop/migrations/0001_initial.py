# Generated by Django 3.2.4 on 2021-06-15 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Rasmi')),
                ('description', models.TextField(blank=True, verbose_name='Tovar haqida')),
                ('price', models.PositiveIntegerField(default=0, null=True, verbose_name='Narxi')),
                ('old_price', models.PositiveIntegerField(blank=True, default=0, verbose_name='Avvalgi Narxi')),
                ('colors', models.CharField(choices=[('white', 'WHITE'), ('black', 'BLACK'), ('blue', 'BLUE'), ('green', 'GREEN'), ('yellow', 'YELLOW'), ('red', 'RED'), ('tomato', 'TOMATO'), ('pink', 'PINK'), ('teal', 'TEAL'), ('brown', 'BROWN')], max_length=50, verbose_name='Ranglari')),
                ('instock', models.BooleanField(default=True, verbose_name="Omborda bor yoki yo'q")),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Soni')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'Tovar',
                'verbose_name_plural': 'Tovarlar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Tovar alohida rasmlari')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name': 'Tovar rasmlari',
                'verbose_name_plural': 'Tovar rasmlari',
            },
        ),
    ]
