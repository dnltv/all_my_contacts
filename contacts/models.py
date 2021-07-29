from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom Model for Auth
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=20, help_text=_('Enter your name'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class DopeUser(models.Model):
    """
    Representation of Profile model
    """
    # Fields
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, verbose_name=_('user'))
    first_name = models.CharField(_('first name'), max_length=20, help_text=_('Enter your name'))
    last_name = models.CharField(_('last name'), max_length=20, help_text='Введите свою фамилию', null=True, blank=True)
    nickname = models.CharField(max_length=20, help_text='Введите свой никнейм', null=True, blank=True)
    date_of_birth = models.DateField(help_text='Введите дату своего рождения в формате YYYY-MM-DD', null=True,
                                     blank=True)
    description = models.TextField(help_text='Расскажите о себе', max_length=500, null=True, blank=True)
    photo = models.FileField(null=True, blank=True)

    # Видимость аккаунта по никнейму
    VISIBLE_STATUS = (
        ('v', 'Visible'),
        ('h', 'Hidden'),
    )
    status = models.CharField(max_length=1, choices=VISIBLE_STATUS, blank=True, default='v',
                              help_text='Видимость аккаунта')

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of UserModel.
        """
        return reverse('user', args=[str(self.id)])

    def __str__(self):
        """
        String representating the UserModel object (in Admin site etc.)
        """
        if self.last_name:
            return f'{self.first_name} {self.last_name}'  #(id: {self.id})
        else:
            return f'{self.first_name}'


class SocialMedia(models.Model):
    """
    Representation of User's Social Media references
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    instagram = models.CharField(max_length=50, help_text='Профиль Instagram', null=True, blank=True,
                                 verbose_name='Instagram')
    instagram2 = models.CharField(max_length=50, help_text='Профиль Instagram', null=True, blank=True,
                                  verbose_name='Instagram 2')
    tiktok = models.CharField(max_length=50, help_text='Профиль Tik-Tok', null=True, blank=True)
    vk = models.CharField(max_length=50, help_text='Профиль Вконтакте', null=True, blank=True)
    facebook = models.CharField(max_length=50, help_text='Профиль Facebook', null=True, blank=True)
    twitter = models.CharField(max_length=50, help_text='Профиль Twitter', null=True, blank=True)
    snapchat = models.CharField(max_length=50, help_text='Профиль Snapchat', null=True, blank=True)
    odnoklassniki = models.CharField(max_length=50, help_text='Профиль Одноклассники', null=True, blank=True)
    pinterest = models.CharField(max_length=50, help_text='Профиль Pinterest', null=True, blank=True)
    tumblr = models.CharField(max_length=50, help_text='Профиль Tumblr', null=True, blank=True)
    yandex_dzen = models.CharField(max_length=50, help_text='Профиль Яндекс.Дзен', null=True, blank=True)
    clubhouse = models.CharField(max_length=50, help_text='Профиль Clubhouse', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Social Media'
        # permissions

    #def get_absolute_url(self):
        #"""
        #Returns the url to access a particular Social Media refs of User.
        #"""
        #return reverse('user-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        Model representating a DopeUser's Social Media object(in Admin site etc.)
        """
        return self.user.__str__()

    # def display_user_social_media(self):
    # return ', '.join([field.name for field in self._meta.get_fields()])
    # display_user_social_media.short_description = 'SM'


class Messengers(models.Model):
    """
    Representation of User's Messengers
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    telegram = models.CharField(max_length=50, help_text='Укажите номер или никнейм Telegram', null=True, blank=True)
    whatsapp = models.CharField(max_length=50, help_text='Укажите номер или никнейм WhatsApp', null=True, blank=True)
    viber = models.CharField(max_length=50, help_text='Укажите номер или никнейм Viber', null=True, blank=True)
    facebook_messenger = models.CharField(max_length=50, help_text='Укажите номер или никнейм Facebook Messenger',
                                          null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Messengers'

    def __str__(self):
        return self.user.__str__()


class VideoCallServices(models.Model):
    """
    Representation of User's Video-calling services
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    facetime = models.CharField(max_length=50, help_text='Укажите номер телефона или логин FaceTime',
                                null=True, blank=True)
    skype = models.CharField(max_length=50, help_text='Укажите логин Skype', null=True, blank=True)
    zoom = models.CharField(max_length=50, help_text='Укажите логин Zoom', null=True, blank=True)
    discord = models.CharField(max_length=100, help_text='Профиль Discord', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Video Call Services'

    def __str__(self):
        return self.user.__str__()


class PersonalContacts(models.Model):
    """
    Representating User's personal contacts
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15, help_text='Введите номер телефона', null=True, blank=True)
    email = models.EmailField(max_length=100, help_text='Введите e-mail', null=True, blank=True)
    site = models.CharField(max_length=100, help_text='Укажите адрес сайта', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Personal Contacts'

    def __str__(self):
        return self.user.__str__()


class MusicPlatforms(models.Model):
    """
    Representation of User's accounts on Music Platforms
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    apple_music = models.CharField(max_length=50, help_text='Профиль Apple Music',
                                   null=True, blank=True)
    spotify = models.CharField(max_length=50, help_text='Профиль Spotify', null=True, blank=True)
    soundcloud = models.CharField(max_length=50, help_text='Профиль SoundCloud', null=True, blank=True)
    yandex_music = models.CharField(max_length=50, help_text='Профиль Яндекс.Музыка', null=True,
                                    blank=True)
    vk_boom = models.CharField(max_length=50, help_text='Профиль VK BOOM', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Music Platforms'

    def __str__(self):
        return self.user.__str__()


class VideoHostings(models.Model):
    """
    Representation of User's accounts on Video-hosting services
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    youtube = models.CharField(max_length=50, help_text='Профиль/канал Youtube', null=True, blank=True)
    vimeo = models.CharField(max_length=50, help_text='Профиль Vimeo', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Video Hostings'

    def __str__(self):
        return self.user.__str__()


class Wallets(models.Model):
    """
    Representation of User's accounts on MT services
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    sberbank = models.CharField(max_length=100, help_text='Укажите номер карты или номер телефона, к которому '
                                                          'привязана карта Сбербанк', null=True, blank=True)
    alfabank = models.CharField(max_length=100, help_text='Укажите номер карты или номер телефона, к которому '
                                                          'привязана карта Альфа-Банк', null=True, blank=True)
    tinkoff = models.CharField(max_length=100, help_text='Укажите номер карты или номер телефона, '
                                                         'к которому привязана карта Тинькофф Банк', null=True,
                               blank=True)
    yoomoney = models.CharField(verbose_name='YooMoney', max_length=100, help_text='Укажите номер кошелька YooMoney (Яндекс.Деньги)',
                                null=True, blank=True)
    vk_pay = models.CharField(max_length=100, help_text='Укажите номер кошелька VK Pay', null=True, blank=True)
    paypal = models.CharField(max_length=100, help_text='Укажите номер кошелька PayPal', null=True, blank=True)
    qiwi = models.CharField(max_length=100, help_text='Укажите номер кошелька QIWI', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Wallets'

    def __str__(self):
        return self.user.__str__()


class Portfolio(models.Model):
    """
    Representation of User's accounts on portfolio sites
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    behance = models.CharField(max_length=100, help_text='Укажите свой профиль Behance', null=True, blank=True)
    dribbble = models.CharField(max_length=100, help_text='Укажите свой профиль Dribbble', null=True, blank=True)
    five_hundred_px = models.CharField(name='500px', max_length=100, help_text='Укажите свой профиль 500px', null=True,
                                       blank=True)
    flickr = models.CharField(max_length=100, help_text='Укажите свой профиль Flickr', null=True, blank=True)
    linkedin = models.CharField(max_length=100, help_text='Укажите свой профиль LinkedIn', null=True, blank=True)
    github = models.CharField(max_length=100, help_text='Профиль GitHub', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.user.__str__()


class Gaming(models.Model):
    """
    Representation of User's accounts on Gaming Platforms
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    twitch = models.CharField(max_length=100, help_text='Профиль Twitch', null=True, blank=True)
    steam = models.CharField(max_length=100, help_text='Профиль Steam', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Gaming'

    def __str__(self):
        return self.user.__str__()


class Maps(models.Model):
    """
    Representation of User's address
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, help_text='Введите адрес', null=True, blank=True)
    yandex_maps = models.CharField(max_length=100, help_text='Введите координаты в Яндекс.Картах', null=True, blank=True, )
    google_maps = models.CharField(max_length=100, help_text='Введите координаты в Google Maps', null=True, blank=True, )
    two_gis_maps = models.CharField(name='2GIS', max_length=100, help_text='Введите координаты в 2ГИС', null=True, blank=True, )

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Maps'

    def __str__(self):
        return self.user.__str__()


class Other(models.Model):
    """
    Representation any other info about User
    """
    user = models.ForeignKey(DopeUser, on_delete=models.CASCADE, null=True)
    onlyfans = models.CharField(max_length=50, help_text='Профиль OnlyFans', null=True, blank=True)
    podcasts = models.CharField(max_length=50, help_text='Профиль Podcasts', null=True, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'Other'

    def __str__(self):
        return self.user.__str__()
