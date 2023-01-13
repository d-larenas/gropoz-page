from apps.core.models import TimesModelMixin, UUIDModelMixin
from django.db import models


class SiteRegister(TimesModelMixin, UUIDModelMixin):
    """Model for register of error."""

    status_code = models.CharField(null=False, blank=False, max_length=3)

    message_error = models.TextField(null=False, blank=False)

    page = models.ForeignKey(
        "logs_page.SiteAlert",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):  # noqa
        return f"{self.status_code} - {self.page}"
