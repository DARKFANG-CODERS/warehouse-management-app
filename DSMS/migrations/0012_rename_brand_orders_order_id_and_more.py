# Generated by Django 4.0.6 on 2022-09-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSMS', '0011_approvals_approved_orders_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='brand',
            new_name='order_id',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='category',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='orders',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
