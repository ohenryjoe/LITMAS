# Generated by Django 3.2.6 on 2022-06-27 19:09

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
        ('person', '0002_marital_status_log_nationality_log_physical_address_log_village_log'),
        ('lookup', '0001_initial'),
        ('location', '0001_initial'),
        ('service_provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='animal_type_slaughter_house',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.animal_type')),
            ],
        ),
        migrations.CreateModel(
            name='slaughterhouse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('license_issue_date', models.DateField()),
                ('date_est', models.DateField()),
                ('gps_lat', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('gps_long', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal_type', models.ManyToManyField(through='service_provider.animal_type_slaughter_house', to='lookup.animal_type')),
                ('operation_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.operation_status')),
                ('org', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='organisation.organisation')),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
                ('village', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='location.village')),
            ],
        ),
        migrations.AddField(
            model_name='animal_type_slaughter_house',
            name='slaughterhouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='service_provider.slaughterhouse'),
        ),
    ]
