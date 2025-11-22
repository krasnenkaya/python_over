from datetime import datetime, timedelta

def get_future_date(days):
    """
    Принимает количество дней и возвращает дату через указанное количество дней
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date

# Получаем количество дней от пользователя
try:
    days = int(input("Введите количество дней: "))
    
    # Получаем будущую дату
    result_date = get_future_date(days)
    
    # Выводим результат
    print(f"Через {days} дней будет: {result_date.strftime('%Y-%m-%d')}")
    
except ValueError:
    print("Ошибка: Введите целое число!")