# Generated by Django 3.0.3 on 2020-02-15 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200215_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='alliance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Alliance'),
        ),
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Guild'),
        ),
    ]
