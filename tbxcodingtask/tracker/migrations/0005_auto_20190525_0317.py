# Generated by Django 2.1.7 on 2019-05-25 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20190525_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tracker.Project'),
            preserve_default=False,
        ),
    ]
