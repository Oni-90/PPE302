# Generated by Django 4.0.10 on 2024-06-25 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('censusApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='censusApp.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='AgentToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='censusApp.agent')),
            ],
        ),
    ]
