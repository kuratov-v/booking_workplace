from rest_framework.exceptions import ValidationError

from django.db.models import Q
from django.db.models.query import QuerySet

from workplace.models import Workplace


def filter_booking_workplace(datetime_from: str, datetime_to: str) -> 'QuerySet[Workplace]':
    """
    Возвращает рабочие места на которые есть бронь в данный промежуток времени.
    """
    return Workplace.objects.filter(
        Q(Q(bookings__datetime_from__range=[datetime_from, datetime_to]) |
          Q(bookings__datetime_to__range=[datetime_from, datetime_to])) |
        Q(Q(bookings__datetime_from__lte=datetime_from), Q(bookings__datetime_to__gte=datetime_to))
    )


def get_free_workplaces(datetime_from: str, datetime_to: str) -> 'QuerySet[Workplace]':
    """
    Возвращает свободные в указанный промежуток времени рабочие места.
    """
    workplace_list = filter_booking_workplace(datetime_from, datetime_to).values_list('id', flat=True)
    return Workplace.objects.exclude(id__in=workplace_list)


def booking_create_verification(workplace: Workplace, datetime_from: str, datetime_to: str) -> None:
    """
    Вызывает ошибку, если для рабочего места в указанное время уже есть бронь.
    """
    workplace_filter = filter_booking_workplace(datetime_from, datetime_to)

    if workplace_filter.filter(pk=workplace.pk).exists():
        raise ValidationError({'error': 'The selected time intersects with the already booked'})
