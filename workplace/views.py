from rest_framework import mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from workplace import services
from workplace.models import Workplace, Booking
from workplace.serializers import (
    WorkplaceListSerializer,
    WorkplaceDetailSerializer,
    BookingSerializer,
    BookingEditSerializer
)


class WorkplaceView(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """
    Вывод всех рабочих мест list и detail.
    При указанных датах вывыодит свободные рабочие места в этот промежуток времени.
    """
    queryset = Workplace.objects.all().prefetch_related('bookings')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return WorkplaceDetailSerializer
        return WorkplaceListSerializer

    def list(self, request, *args, **kwargs):
        params = request.query_params
        workplaces = Workplace.objects.all()
        if params:
            try:
                workplaces = services.get_free_workplaces(
                    params['datetime_from'],
                    params['datetime_to']
                )
            except KeyError as e:
                return Response({"error": f'Missing data: {e.args}'})
        serializer = self.get_serializer(workplaces, many=True)
        return Response(serializer.data)


class BookingView(ModelViewSet):
    """
    Бронирование для текущего пользователя
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookingSerializer
        return BookingEditSerializer

    def get_serializer_context(self):
        context = super(BookingView, self).get_serializer_context()
        context.update({"user": self.request.user})
        return context

    def perform_create(self, serializer):
        services.booking_create_verification(**serializer.validated_data)
        serializer.save()

    def perform_update(self, serializer):
        services.booking_create_verification(**serializer.validated_data)
        serializer.save()
