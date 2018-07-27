# Generated by Django 2.0.4 on 2018-07-27 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(max_length=60, verbose_name='Slug')),
                ('type', models.CharField(choices=[('docker', 'DOCKER')], default='docker', max_length=20, verbose_name='Type')),
                ('server', models.CharField(max_length=200, verbose_name='Connection')),
                ('auth_data', models.TextField(verbose_name='Auth Data')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
        ),
        migrations.CreateModel(
            name='Host_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Host', verbose_name='Related host')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('failed', 'FAILED'), ('passed', 'PASSED'), ('daemon', 'DAEMON'), ('error', 'ERROR')], default='pending', max_length=20, verbose_name='Status')),
                ('last_status', models.CharField(choices=[('pending', 'PENDING'), ('failed', 'FAILED'), ('passed', 'PASSED'), ('daemon', 'DAEMON'), ('error', 'ERROR')], default='pending', max_length=20, verbose_name='Last Status')),
                ('locked', models.BooleanField(default=False, verbose_name='Locked')),
                ('executor', models.CharField(max_length=200, verbose_name='Executor')),
                ('parameters', models.TextField(max_length=30, verbose_name='Parameters')),
                ('interval', models.CharField(max_length=200, verbose_name='Interval')),
                ('retry_count', models.PositiveSmallIntegerField(default=0, verbose_name='Retry Count')),
                ('trials', models.PositiveSmallIntegerField(default=5, verbose_name='Trials')),
                ('priority', models.PositiveSmallIntegerField(verbose_name='Priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('run_at', models.DateTimeField(null=True, verbose_name='Run at')),
                ('last_run', models.DateTimeField(null=True, verbose_name='Last Run')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('autoload', models.BooleanField(default=False, verbose_name='Autoload')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('github_url', models.CharField(max_length=100, verbose_name='Github URL')),
                ('facebook_url', models.CharField(max_length=100, verbose_name='Facebook URL')),
                ('twitter_url', models.CharField(max_length=100, verbose_name='Twitter URL')),
                ('access_token', models.CharField(max_length=200, verbose_name='Access token')),
                ('refresh_token', models.CharField(max_length=200, verbose_name='Refresh token')),
                ('access_token_updated_at', models.DateTimeField(null=True, verbose_name='Access token last update')),
                ('refresh_token_updated_at', models.DateTimeField(null=True, verbose_name='Refresh token last update')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
        ),
        migrations.CreateModel(
            name='Reset_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=100, verbose_name='Email')),
                ('token', models.CharField(db_index=True, max_length=200, verbose_name='Token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('expire_at', models.DateTimeField(verbose_name='Expire at')),
                ('messages_count', models.PositiveSmallIntegerField(verbose_name='Messages Count')),
            ],
        ),
        migrations.CreateModel(
            name='User_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related User')),
            ],
        ),
    ]
