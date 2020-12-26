from rest_framework import serializers

from workplace.models import Workplace, Booking, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'floor', 'description']


class BookingSerializer(serializers.ModelSerializer):
    datetime_from = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    datetime_to = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Booking
        fields = ['id', 'workplace', 'datetime_from', 'datetime_to']


class WorkplaceListSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Workplace
        fields = ['id', 'number', 'description', 'room']


class BookingListSerializer(serializers.ModelSerializer):
    datetime_from = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    datetime_to = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    workplace = WorkplaceListSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'workplace', 'datetime_from', 'datetime_to']


class WorkplaceDetailSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(source='bookings', many=True)
    room = RoomSerializer()

    class Meta:
        model = Workplace
        fields = ['id', 'number', 'room', 'description', 'booking']


class BookingEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'workplace', 'datetime_from', 'datetime_to']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('user')
        return super(BookingEditSerializer, self).create(validated_data)
