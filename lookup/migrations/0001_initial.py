# Generated by Django 3.2.6 on 2022-06-27 12:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animal_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='breed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='dominant_color',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='education_level',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='est_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='identity_doc_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='incident_level',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='incident_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='mode_of_transport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='nationality',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='next_of_kin_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='operation_status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='origin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='payment_channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='payment_mode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='quarantine_reason',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='quarantine_status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tag_status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='trans_fee_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='transfer_action_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='transfer_nature',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='transfer_purpose',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='transfer_status',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tribe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_make',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
