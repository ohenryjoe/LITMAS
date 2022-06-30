# Generated by Django 3.2.6 on 2022-06-27 12:18

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0001_initial'),
        ('person', '0001_initial'),
        ('lookup', '0001_initial'),
        ('location', '0001_initial'),
        ('animal', '0001_initial'),
        ('service_provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transfer_date', models.DateField()),
                ('expected_arrival_date', models.DateField()),
                ('permit_number', models.CharField(default='000000000', max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.animal_type')),
                ('mode_of_transport', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.mode_of_transport')),
                ('org_ben', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='organisation.organisation')),
                ('person_ben', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='beneficiary', to='person.person')),
                ('transfer_initiated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='initiated_by', to='person.person')),
                ('transfer_nature', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.transfer_nature')),
                ('transfer_purpose', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.transfer_purpose')),
                ('transfer_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.transfer_status')),
                ('village', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='location.village')),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('driver_permit_number', models.CharField(default='000000000', max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
                ('transfer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.transfer')),
                ('vehicle', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='service_provider.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='transfer_route_readerpoint',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('readerpoint_order', models.PositiveIntegerField(unique=True)),
                ('readerpoint_name', models.CharField(default='xxx', max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('readerpoint_location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='location.village')),
                ('transfer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.transfer')),
            ],
        ),
        migrations.CreateModel(
            name='transfer_route_checkpoint',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checkpoint_order', models.PositiveIntegerField(unique=True)),
                ('checkpoint_name', models.CharField(default='xxx', max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('checkpoint_location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='location.village')),
                ('transfer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.transfer')),
            ],
        ),
        migrations.CreateModel(
            name='quarantine_notice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('expected_end_date', models.DateField()),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('reason', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.quarantine_reason')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.quarantine_status')),
            ],
        ),
        migrations.CreateModel(
            name='quarantine_animal_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('expected_end_date', models.DateField()),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.animal_type')),
                ('quarantine_notice', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.quarantine_notice')),
            ],
        ),
        migrations.CreateModel(
            name='animal_transfer_fee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fee_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('payment_date', models.DateField()),
                ('invoice_number', models.CharField(default='current_user', max_length=60)),
                ('invoice_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('fee_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.trans_fee_type')),
                ('payment_channel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.payment_channel')),
                ('payment_mode', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.payment_mode')),
                ('transfer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.transfer')),
            ],
        ),
        migrations.CreateModel(
            name='animal_transfer_action',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('action_date', models.DateField()),
                ('action_reason', models.CharField(default='current_user', max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('action_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.transfer_action_type')),
                ('transfer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.transfer')),
            ],
        ),
        migrations.CreateModel(
            name='animal_transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='animal.animal')),
                ('transfer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='movement.transfer')),
            ],
        ),
    ]
