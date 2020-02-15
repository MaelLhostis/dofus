# Generated by Django 3.0.3 on 2020-02-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200215_1407'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DofusClass',
        ),
        migrations.AlterField(
            model_name='alliance',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='alliance',
            name='server',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='guild',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='guild',
            name='server',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='player',
            name='DofusClasse',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='player',
            name='dbook',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='player',
            name='pvpm',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='player',
            name='server',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
