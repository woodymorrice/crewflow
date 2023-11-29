# Generated by Django 4.2.6 on 2023-11-29 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='payroll_status',
            field=models.CharField(choices=[('PENDING', 'Pending Approval'), ('APPROVED', 'Approved'), ('DECLINED', 'Declined')], default='PENDING', max_length=24),
        ),
    ]
