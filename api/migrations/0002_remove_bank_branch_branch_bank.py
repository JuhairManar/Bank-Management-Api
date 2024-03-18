# Generated by Django 5.0 on 2024-03-15 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='branch',
        ),
        migrations.AddField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='bank', to='api.bank'),
            preserve_default=False,
        ),
    ]
