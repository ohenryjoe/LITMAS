# Generated by Django 3.2.6 on 2022-06-30 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='county',
            old_name='dictrict',
            new_name='district',
        ),
        migrations.AddField(
            model_name='county',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='county',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='county',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='county',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='district',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='district',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='createdby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='district',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='district',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='parish',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='parish',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parish',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='parish',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='region',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='region',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='region',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sub_region',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='sub_region',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub_region',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='sub_region',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcounty',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='village',
            name='created_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='village',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='village',
            name='updated_by',
            field=models.CharField(default='current_user', max_length=100),
        ),
        migrations.AddField(
            model_name='village',
            name='updated_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
