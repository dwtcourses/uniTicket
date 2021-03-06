# Generated by Django 3.0.3 on 2020-03-03 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessagemodel',
            options={'ordering': ('-created',), 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
        migrations.RemoveField(
            model_name='chatmessagemodel',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='chatmessagemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatmessagemodel',
            name='room',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
