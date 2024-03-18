# Generated by Django 5.0 on 2024-03-15 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_branch_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='bank',
        ),
        migrations.AddField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='api.bank'),
            preserve_default=False,
        ),
    ]
