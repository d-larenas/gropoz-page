from django.contrib import admin

from apps.logs_page.models import MessageType, SiteRegister, SiteAlert


class MessageTypeAdmin(admin.ModelAdmin):
    """Project model admin."""
    list_display = ('uuid', 'email', 'type_alert', 'created')


class SiteRegisterAdminView(admin.ModelAdmin):
    """Project model admin view."""
    list_display = ('uuid', 'status_code', 'page', 'created')


class SiteAlertView(admin.ModelAdmin):
    """Project model admin view."""
    list_display = ('uuid', 'url_site', 'message_type', 'created')


admin.site.register(MessageType, MessageTypeAdmin)
admin.site.register(SiteRegister, SiteRegisterAdminView)
admin.site.register(SiteAlert, SiteAlertView)
