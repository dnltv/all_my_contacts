# Generated by Django 3.2.5 on 2021-07-21 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20210721_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(blank=True, help_text='Укажите номер или никнейм Telegram', max_length=30, null=True)),
                ('whatsapp', models.CharField(blank=True, help_text='Укажите номер или никнейм WhatsApp', max_length=30, null=True)),
                ('viber', models.CharField(blank=True, help_text='Укажите номер или никнейм Viber', max_length=30, null=True)),
                ('facebook_messenger', models.CharField(blank=True, help_text='Укажите номер или никнейм Facebook Messenger', max_length=30, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Messengers',
                'ordering': ['user'],
            },
        ),
    ]
