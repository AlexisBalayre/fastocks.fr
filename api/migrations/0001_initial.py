# Generated by Django 3.1.5 on 2021-03-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_user', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id user')),
                ('gender', models.CharField(default=None, max_length=1, null=True, verbose_name='gender')),
                ('birth_date', models.DateField(default=None, null=True, verbose_name='birth date')),
                ('first_name', models.CharField(default=None, max_length=60, null=True, verbose_name='first name')),
                ('last_name', models.CharField(default=None, max_length=60, null=True, verbose_name='last name')),
                ('phone', models.CharField(default=None, max_length=20, null=True, unique=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('alert_stock_email', models.BooleanField(default=True)),
                ('alert_price_email', models.BooleanField(default=True)),
                ('alert_stock_sms', models.BooleanField(default=False)),
                ('alert_price_sms', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(default=None, max_length=255, null=True, unique=True, verbose_name='token')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'db_table': 'fastocks_users',
            },
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id_monitoring', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id monitoring')),
                ('id_user', models.IntegerField(verbose_name='id user')),
                ('sku', models.IntegerField(verbose_name='sku')),
                ('stock', models.BooleanField(default=True, verbose_name='stock')),
                ('price', models.BooleanField(default=True, verbose_name='price')),
                ('limit', models.DecimalField(decimal_places=6, max_digits=16, verbose_name='limit')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'db_table': 'fastocks_monitoring',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('sku', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='sku')),
                ('market_place', models.CharField(max_length=200, verbose_name='market place')),
                ('brand', models.CharField(max_length=200, verbose_name='brand')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('categorie', models.CharField(max_length=200, verbose_name='categorie')),
                ('size', models.CharField(max_length=200, null=True, verbose_name='size')),
                ('color', models.CharField(max_length=200, verbose_name='color')),
                ('request', models.CharField(max_length=200, verbose_name='request')),
                ('stock', models.BooleanField(default=False, verbose_name='stock')),
                ('price', models.DecimalField(decimal_places=6, max_digits=16, verbose_name='price')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'db_table': 'fastocks_products',
            },
        ),
    ]
