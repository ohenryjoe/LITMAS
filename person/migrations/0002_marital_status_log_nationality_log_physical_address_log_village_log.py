# Generated by Django 3.2.6 on 2022-06-27 12:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='village_log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_village', models.CharField(blank=True, max_length=200, null=True)),
                ('to_village', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='physical_address_log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_address', models.CharField(blank=True, max_length=200, null=True)),
                ('to_address', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='nationality_log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('to_nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='marital_status_log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_is_married', models.CharField(blank=True, max_length=200, null=True)),
                ('to_is_married', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(default='current_user', max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default='current_user', max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
        ),
    ]
