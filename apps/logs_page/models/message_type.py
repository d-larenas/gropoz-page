# Django
# Utilities
from apps.core.models import TimesModelMixin, UUIDModelMixin
from django.db import models

EMAIL = 1
OTHER = 2

ALERT_TYPE = (
    (EMAIL, "EMAIL"),
    (OTHER, "OTHER"),

)


class MessageType(TimesModelMixin, UUIDModelMixin):
    """model for sent alert."""

    email = models.EmailField(null=False, blank=False, unique=True, error_messages={
        'unique': 'A user with that email already exists.'
    })

    type_alert = models.SmallIntegerField(
        choices=ALERT_TYPE,
        default=EMAIL
    )

    def __str__(self):  # noqa
        return str(self.email)
