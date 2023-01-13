# Django
# Utilities
from apps.core.models import TimesModelMixin, UUIDModelMixin
from django.db import models


class SiteAlert(TimesModelMixin, UUIDModelMixin):
    """Model for register of url."""

    url_site = models.URLField(
        null=True,
        blank=True,
        unique=True
    )

    message_type = models.ForeignKey(
        "logs_page.MessageType",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    enable = models.BooleanField(
        default=True
    )

    def __str__(self):  # noqa
        return str(self.url_site)
