from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
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


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name')
    ordering = ('email', 'first_name')


#admin.site.register(CustomUser, CustomUserAdmin)


# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomUser
    # list_display = ('email', 'first_name', 'is_staff', 'is_active')
    # list_filter = ('email', 'first_name', 'is_staff', 'is_active')
    # search_fields = ('email', 'first_name', 'is_staff', 'is_active')
    # fieldsets = (
        #(None, {'fields': ('email', 'first_name', 'password')}),
        #('Permissions', {'fields': ('is_staff', 'is_active')}),
    #)
    #add_fieldsets = (
        #(None, {
            #'classes': ('wide',),
            #'fields': ('email', 'password1', 'password2', 'first_name', 'is_staff', 'is_active')
        #}),
    #)
    #search_fields = ('email', 'first_name')
    #ordering = ('email', 'first_name',)


# admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(DopeUser)
class DopeUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'id', 'date_of_birth')
    list_filter = ('user', 'first_name', 'last_name', 'id', 'date_of_birth')
    search_fields = ('user', 'first_name__startswith', 'id')
    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name',)
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


# admin.site.register(SocialMedia)
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