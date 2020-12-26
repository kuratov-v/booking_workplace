from django.db import models
from django.contrib.auth import get_user_model


class Room(models.Model):
    number = models.CharField(max_length=10)
    floor = models.SmallIntegerField()
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.pk} Number: {self.number}"

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Workplace(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.pk} Number: {self.number}"

    class Meta:
        unique_together = ('room', 'number')
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"


class Booking(models.Model):
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ['-datetime_to', ]
        verbose_name = "Забронированное место"
        verbose_name_plural = "Забронированные места"
