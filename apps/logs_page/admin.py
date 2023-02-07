from django.contrib import admin

from apps.logs_page.models import MessageType, SiteRegister, SiteAlert


class MessageTypeAdmin(admin.ModelAdmin):
    """Project model admin."""
    list_display = ('uuid', 'email', 'type_alert', 'created')


class SiteRegisterAdminView(admin.ModelAdmin):
    """Project model admin view."""
    list_display = ('uuid', 'page', 'status_code', 'created', 'is_alerted',)
    list_display_links = ('uuid', 'page')
    list_filter = ('page', 'status_code', 'is_alerted',)
    search_fields = (
        "status_code",
        "page__url_site",

    )


class SiteAlertView(admin.ModelAdmin):
    """Project model admin view."""
    list_display = ('uuid', 'url_site', 'message_type', 'created', 'enable')


admin.site.register(MessageType, MessageTypeAdmin)
admin.site.register(SiteRegister, SiteRegisterAdminView)
admin.site.register(SiteAlert, SiteAlertView)
