import re

from django.forms import ValidationError
from django.utils.translation import pgettext

FILENAME_CONTENT = re.compile(r"([a-zA-Z0-9]|\.|_|-)+")
FILENAME_TANGIBILITY = re.compile(r"[a-zA-Z0-9]")


def validate_css_name(filename):
    if not filename.lower().endswith(".css"):
        raise ValidationError(
            pgettext("admin css name validator", "Name is missing an .css extension.")
        )

    if filename.startswith("."):
        raise ValidationError(
            pgettext("admin css name validator", 'Name can\'t start with period (".").')
        )

    if not FILENAME_CONTENT.fullmatch(filename[:-4]):
        raise ValidationError(
            pgettext(
                "admin css name validator",
                "Name can contain only latin alphabet characters, digits, dots, underscores and dashes.",
            )
        )

    if not FILENAME_TANGIBILITY.match(filename[:-4]):
        raise ValidationError(
            pgettext(
                "admin css name validator",
                "Name has to contain at least one latin alphabet character or digit.",
            )
        )


def validate_css_name_is_available(instance, name):
    queryset = instance.theme.css.filter(name=name)
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)
    if queryset.exists():
        raise ValidationError(
            pgettext(
                "admin css name unique validator",
                "This name is already in use by other asset.",
            )
        )
