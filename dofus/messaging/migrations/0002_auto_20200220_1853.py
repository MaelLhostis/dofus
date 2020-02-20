# Generated by Django 3.0.3 on 2020-02-20 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messaging',
            name='recever',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='recever', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messaging',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
