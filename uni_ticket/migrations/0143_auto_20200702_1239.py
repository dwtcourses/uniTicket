# Generated by Django 3.0.7 on 2020-07-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0142_auto_20200702_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalstructurewsarchipro',
            name='protocollo_email',
            field=models.EmailField(blank=True, help_text='Se vuoto: amministrazione@pec.unical.it', max_length=255, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='ticketcategorywsarchipro',
            name='protocollo_fascicolo_numero',
            field=models.IntegerField(verbose_name='Fascicolo numero'),
        ),
    ]
