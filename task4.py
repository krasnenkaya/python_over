import argparse

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description='Скрипт для работы с числом и строкой')
    
    # Обязательные аргументы
    parser.add_argument('number', type=int, help='Целое число')
    parser.add_argument('text', type=str, help='Текстовая строка')
    
    # Опции (флаги)
    parser.add_argument('--verbose', action='store_true', 
                       help='Выводить дополнительную информацию')
    parser.add_argument('--repeat', type=int, default=1,
                       help='Количество повторений строки (по умолчанию: 1)')
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Режим verbose
    if args.verbose:
        print("=== РЕЖИМ VERBOSE ===")
        print(f"Получено число: {args.number}")
        print(f"Получен текст: {args.text}")
        print(f"Количество повторений: {args.repeat}")
        print("---")
    
    # Основная логика
    result = args.number * 2
    print(f"Результат умножения числа на 2: {result}")
    
    # Повторение строки
    for i in range(args.repeat):
        print(f"Текст: {args.text}")
    
    # Дополнительная информация в verbose режиме
    if args.verbose:
        print("---")
        print("Обработка завершена!")

if __name__ == "__main__":
    main()