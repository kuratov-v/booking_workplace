# booking_workplace

#### Регистрация  
```
[POST] http://194.58.98.101/api/auth/users/
  - username
  - password
```

#### Авторизация
```
[POST] http://194.58.98.101/api/auth/token/login/
  - username
  - password
  
Response:
  - token 
```

#### Список рабочих мест
```
[GET] http://194.58.98.101/api/workplace/
```

#### Список свободных рабочих мест в указанное время
```
[GET] http://194.58.98.101/api/workplace/?datetime_from=2020-12-13 15:30&datetime_to=2020-12-13 20:00
```

#### Список забронированных мест для текущего пользователя
```
[GET] http://194.58.98.101/api/booking/
[GET] http://194.58.98.101/api/booking/<id>/
Headers: Authorization - Token 668b4bda49bcfa92d2842100babbc9ff576c8a8b
```

#### Бронирование рабочего места
```
[POST] http://194.58.98.101/api/booking/
Headers: Authorization - Token 668b4bda49bcfa92d2842100babbc9ff576c8a8b
Data: 
  workplace - id рабочего места
  datetime_from - время в iso формате "Бронировать с ..."
  datetime_to - время в iso формате "Бронировать по ..."
```

#### Редактирование брони
```
[PUT, PATCH] http://194.58.98.101/api/booking/<id>/
Headers: Authorization - Token 668b4bda49bcfa92d2842100babbc9ff576c8a8b
Data: 
  workplace - id рабочего места
  datetime_from - время в iso формате "Бронировать с ..."
  datetime_to - время в iso формате "Бронировать по ..."
```

#### Удаление брони
```
[DELETE] http://194.58.98.101/api/booking/<id>/
Headers: Authorization - Token 668b4bda49bcfa92d2842100babbc9ff576c8a8b
```

# Развернуть dev версию
```
git clone https://github.com/kuratov-v/booking_workplace.git
cd booking_workplace
docker-compose build
docker-compose up -d 
```
