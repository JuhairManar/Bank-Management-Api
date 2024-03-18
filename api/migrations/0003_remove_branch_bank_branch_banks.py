# Generated by Django 5.0 on 2024-03-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_bank_branch_branch_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='bank',
        ),
        migrations.AddField(
            model_name='branch',
            name='banks',
            field=models.ManyToManyField(related_name='branches', to='api.bank'),
        ),
    ]
