# Generated by Django 2.2.4 on 2019-08-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0041_auto_20190806_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketcategory',
            old_name='allow_utente',
            new_name='allow_user',
        ),
    ]
