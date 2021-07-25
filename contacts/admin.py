from django.contrib import admin
from .models import *


class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    extra = 0


class MessengersInline(admin.StackedInline):
    model = Messengers
    extra = 0


class VideoCallServicesInline(admin.StackedInline):
    model = VideoCallServices
    extra = 0


class PersonalContactsInline(admin.StackedInline):
    model = PersonalContacts
    extra = 0


class MusicPlatformsInline(admin.StackedInline):
    model = MusicPlatforms
    extra = 0


class VideoHostingsInline(admin.StackedInline):
    model = VideoHostings
    extra = 0


class WalletsInline(admin.StackedInline):
    model = Wallets
    extra = 0


class PortfolioInline(admin.StackedInline):
    model = Portfolio
    extra = 0


class GamingInline(admin.StackedInline):
    model = Gaming
    extra = 0


class MapsInline(admin.StackedInline):
    model = Maps
    extra = 0


class OtherInline(admin.StackedInline):
    model = Other
    extra = 0


@admin.register(DopeUser)
class DopeUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id', 'date_of_birth')
    list_filter = ('first_name', 'last_name', 'id', 'date_of_birth')
    search_fields = ('first_name__startswith', 'id')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name',)
        }),
        ('About', {
            'fields': ('photo', 'description', 'nickname', 'date_of_birth',)
        }),
        ('Account Visibility', {
            'fields': ('status',)
        }),
    )
    inlines = [SocialMediaInline, MessengersInline, VideoCallServicesInline, PersonalContactsInline,
               MusicPlatformsInline, VideoHostingsInline, WalletsInline, PortfolioInline, GamingInline, MapsInline,
               OtherInline]


# admin.site.register(UserSocialMedia)
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('user', 'instagram', 'instagram2', 'vk', 'facebook', 'twitter')
    search_fields = ('user__startswith', 'instagram__startswith', 'instagram2', 'vk', 'facebook', 'twitter')
    fields = ('user', ('instagram', 'instagram2'), 'tiktok', 'vk', 'facebook', 'twitter', 'snapchat', 'odnoklassniki',
              'pinterest', 'tumblr', 'yandex_dzen', 'clubhouse')


@admin.register(Messengers)
class MessengersAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram', 'whatsapp', 'viber', 'facebook_messenger')


@admin.register(VideoCallServices)
class VideoCallServicesAdmin(admin.ModelAdmin):
    list_display = ('user', 'facetime', 'skype', 'zoom', 'discord')


@admin.register(PersonalContacts)
class PersonalContactsAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'email', 'site')
    fields = ('user', ('phone_number', 'email'), 'site')

@admin.register(MusicPlatforms)
class MusicPlatformsAdmin(admin.ModelAdmin):
    list_display = ('user', 'apple_music', 'spotify', 'soundcloud', 'yandex_music', 'vk_boom')


@admin.register(VideoHostings)
class VideoHostingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'youtube', 'vimeo')


@admin.register(Wallets)
class WalletsAdmin(admin.ModelAdmin):
    list_display = ('user', 'sberbank', 'alfabank','tinkoff', 'yoomoney', 'vk_pay', 'paypal', 'qiwi')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'behance', 'dribbble', '500px', 'flickr', 'linkedin', 'github')


@admin.register(Gaming)
class GamingAdmin(admin.ModelAdmin):
    list_display = ('user', 'twitch', 'steam')


@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'yandex_maps', 'google_maps', '2GIS')


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = ('user', 'onlyfans', 'podcasts')