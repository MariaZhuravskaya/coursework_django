# Generated by Django 4.2.5 on 2023-09-18 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_logi_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesettings',
            name='last_dispatch_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 18, 20, 2, 26, 289635), verbose_name='дата последней отправки'),
        ),
    ]
