# Generated by Django 2.1.7 on 2019-03-05 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0003_auto_20190305_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationalstructurefunction',
            name='structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizational_area.OrganizationalStructure'),
        ),
    ]
