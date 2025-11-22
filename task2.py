from datetime import datetime

# Получаем текущее время и дату
now = datetime.now()

# Выводим в формате YYYY-MM-DD HH:MM:SS
formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(f"Текущая дата и время: {formatted_datetime}")

# Получаем день недели
day_of_week = now.strftime('%A')
print(f"День недели: {day_of_week}")

# Получаем номер недели в году
week_number = now.isocalendar()[1]
print(f"Номер недели в году: {week_number}")