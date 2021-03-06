# Generated by Django 3.2.5 on 2021-07-30 12:18

import autoslug.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(help_text='Enter your name', max_length=20, verbose_name='first name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DopeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='?????????????? ???????? ??????', max_length=20, verbose_name='first name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='first_name')),
                ('last_name', models.CharField(blank=True, help_text='?????????????? ???????? ??????????????', max_length=20, null=True, verbose_name='last name')),
                ('nickname', models.CharField(blank=True, help_text='?????????????? ???????? ??????????????', max_length=20, null=True, verbose_name='nickname')),
                ('date_of_birth', models.DateField(blank=True, help_text='?????????????? ???????? ???????????? ????????????????', null=True, verbose_name='date of birth')),
                ('description', models.TextField(blank=True, help_text='???????????????????? ?? ????????', max_length=500, null=True, verbose_name='description')),
                ('photo', models.FileField(blank=True, null=True, upload_to='', verbose_name='photo')),
                ('status', models.CharField(blank=True, choices=[('v', 'Visible'), ('h', 'Hidden')], default='v', help_text='?????????????????? ????????????????', max_length=1)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Wallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sberbank', models.CharField(blank=True, help_text='?????????????? ?????????? ?????????? ?????? ?????????? ????????????????, ?? ???????????????? ?????????????????? ?????????? ????????????????', max_length=100, null=True)),
                ('alfabank', models.CharField(blank=True, help_text='?????????????? ?????????? ?????????? ?????? ?????????? ????????????????, ?? ???????????????? ?????????????????? ?????????? ??????????-????????', max_length=100, null=True)),
                ('tinkoff', models.CharField(blank=True, help_text='?????????????? ?????????? ?????????? ?????? ?????????? ????????????????, ?? ???????????????? ?????????????????? ?????????? ???????????????? ????????', max_length=100, null=True)),
                ('yoomoney', models.CharField(blank=True, help_text='?????????????? ?????????? ???????????????? YooMoney (????????????.????????????)', max_length=100, null=True, verbose_name='YooMoney')),
                ('vk_pay', models.CharField(blank=True, help_text='?????????????? ?????????? ???????????????? VK Pay', max_length=100, null=True)),
                ('paypal', models.CharField(blank=True, help_text='?????????????? ?????????? ???????????????? PayPal', max_length=100, null=True)),
                ('qiwi', models.CharField(blank=True, help_text='?????????????? ?????????? ???????????????? QIWI', max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Wallets',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='VideoHostings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.CharField(blank=True, help_text='??????????????/?????????? Youtube', max_length=50, null=True)),
                ('vimeo', models.CharField(blank=True, help_text='?????????????? Vimeo', max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Video Hostings',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='VideoCallServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facetime', models.CharField(blank=True, help_text='?????????????? ?????????? ???????????????? ?????? ?????????? FaceTime', max_length=50, null=True)),
                ('skype', models.CharField(blank=True, help_text='?????????????? ?????????? Skype', max_length=50, null=True)),
                ('zoom', models.CharField(blank=True, help_text='?????????????? ?????????? Zoom', max_length=50, null=True)),
                ('discord', models.CharField(blank=True, help_text='?????????????? Discord', max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Video Call Services',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(blank=True, help_text='?????????????? Instagram', max_length=50, null=True, verbose_name='Instagram')),
                ('instagram2', models.CharField(blank=True, help_text='?????????????? Instagram', max_length=50, null=True, verbose_name='Instagram 2')),
                ('tiktok', models.CharField(blank=True, help_text='?????????????? Tik-Tok', max_length=50, null=True)),
                ('vk', models.CharField(blank=True, help_text='?????????????? ??????????????????', max_length=50, null=True)),
                ('facebook', models.CharField(blank=True, help_text='?????????????? Facebook', max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, help_text='?????????????? Twitter', max_length=50, null=True)),
                ('snapchat', models.CharField(blank=True, help_text='?????????????? Snapchat', max_length=50, null=True)),
                ('odnoklassniki', models.CharField(blank=True, help_text='?????????????? ??????????????????????????', max_length=50, null=True)),
                ('pinterest', models.CharField(blank=True, help_text='?????????????? Pinterest', max_length=50, null=True)),
                ('tumblr', models.CharField(blank=True, help_text='?????????????? Tumblr', max_length=50, null=True)),
                ('yandex_dzen', models.CharField(blank=True, help_text='?????????????? ????????????.????????', max_length=50, null=True)),
                ('clubhouse', models.CharField(blank=True, help_text='?????????????? Clubhouse', max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Social Media',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behance', models.CharField(blank=True, help_text='?????????????? ???????? ?????????????? Behance', max_length=100, null=True)),
                ('dribbble', models.CharField(blank=True, help_text='?????????????? ???????? ?????????????? Dribbble', max_length=100, null=True)),
                ('500px', models.CharField(blank=True, help_text='?????????????? ???????? ?????????????? 500px', max_length=100, null=True)),
                ('flickr', models.CharField(blank=True, help_text='?????????????? ???????? ?????????????? Flickr', max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, help_text='?????????????? ???????? ?????????????? LinkedIn', max_length=100, null=True)),
                ('github', models.CharField(blank=True, help_text='?????????????? GitHub', max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='PersonalContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, help_text='?????????????? ?????????? ????????????????', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, help_text='?????????????? e-mail', max_length=100, null=True)),
                ('site', models.CharField(blank=True, help_text='?????????????? ?????????? ??????????', max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Personal Contacts',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onlyfans', models.CharField(blank=True, help_text='?????????????? OnlyFans', max_length=50, null=True)),
                ('podcasts', models.CharField(blank=True, help_text='?????????????? Podcasts', max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Other',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='MusicPlatforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple_music', models.CharField(blank=True, help_text='?????????????? Apple Music', max_length=50, null=True)),
                ('spotify', models.CharField(blank=True, help_text='?????????????? Spotify', max_length=50, null=True)),
                ('soundcloud', models.CharField(blank=True, help_text='?????????????? SoundCloud', max_length=50, null=True)),
                ('yandex_music', models.CharField(blank=True, help_text='?????????????? ????????????.????????????', max_length=50, null=True)),
                ('vk_boom', models.CharField(blank=True, help_text='?????????????? VK BOOM', max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Music Platforms',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Messengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(blank=True, help_text='?????????????? ?????????? ?????? ?????????????? Telegram', max_length=50, null=True)),
                ('whatsapp', models.CharField(blank=True, help_text='?????????????? ?????????? WhatsApp', max_length=50, null=True)),
                ('viber', models.CharField(blank=True, help_text='?????????????? ?????????? Viber', max_length=50, null=True)),
                ('facebook_messenger', models.CharField(blank=True, help_text='?????????????? ?????????????? Facebook Messenger', max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Messengers',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, help_text='?????????????? ??????????', max_length=200, null=True)),
                ('yandex_maps', models.CharField(blank=True, help_text='?????????????? ???????????????????? ?? ????????????.????????????', max_length=100, null=True)),
                ('google_maps', models.CharField(blank=True, help_text='?????????????? ???????????????????? ?? Google Maps', max_length=100, null=True)),
                ('2GIS', models.CharField(blank=True, help_text='?????????????? ???????????????????? ?? 2??????', max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Maps',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Gaming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitch', models.CharField(blank=True, help_text='?????????????? Twitch', max_length=100, null=True)),
                ('steam', models.CharField(blank=True, help_text='?????????????? Steam', max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.dopeuser')),
            ],
            options={
                'verbose_name_plural': 'Gaming',
                'ordering': ['user'],
            },
        ),
    ]
