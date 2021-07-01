# Generated by Django 3.2.4 on 2021-07-01 06:38

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('agency_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('email_address', models.EmailField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Create_File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=108)),
                ('last_name', models.CharField(max_length=108)),
                ('guest_email', models.EmailField(max_length=300)),
                ('guest_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('no_of_adults', models.IntegerField()),
                ('no_of_children', models.IntegerField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('currency', models.CharField(choices=[('USD', '$'), ('EUR', '€'), ('GBP', '£'), ('RUP', 'Rs')], max_length=10)),
                ('tour_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accommodation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.add_accommodation')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_create_file_related', related_query_name='sales_create_files', to='sales.agent')),
                ('arrival_transfer_airport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.transfer_airport')),
                ('attraction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.add_attraction')),
                ('day_tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.add_day_tour')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_create_file_related', related_query_name='sales_create_files', to='core.employee')),
                ('meal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.add_meal')),
                ('misc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.add_misc')),
                ('return_transfer_train', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.return_transfer_train')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.add_ticket')),
                ('train_transfer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.transfer_train')),
                ('transfer_return_air', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_create_file_related', related_query_name='sales_create_files', to='operations.return_transfer_airport')),
            ],
        ),
    ]