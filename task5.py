import os
import argparse
import logging
from collections import namedtuple

# Определяем структуру для хранения информации о файлах/папках
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir'])

def setup_logging(log_file='directory_info.log'):
    """Настройка логирования"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # Вывод также в консоль
        ]
    )

def get_directory_contents(directory_path):
    """
    Собирает информацию о содержимом директории
    """
    contents = []
    
    # Проверяем существование директории
    if not os.path.exists(directory_path):
        logging.error(f"Директория не существует: {directory_path}")
        return contents
    
    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        return contents
    
    try:
        # Получаем список элементов в директории
        with os.scandir(directory_path) as entries:
            for entry in entries:
                try:
                    # Получаем информацию об элементе
                    if entry.is_dir():
                        # Для директории
                        name = entry.name
                        extension = ''
                        is_directory = True
                    else:
                        # Для файла
                        filename, ext = os.path.splitext(entry.name)
                        name = filename
                        extension = ext.lstrip('.')  # Убираем точку в начале расширения
                        is_directory = False
                    
                    # Создаем объект FileInfo
                    file_info = FileInfo(
                        name=name,
                        extension=extension,
                        is_directory=is_directory,
                        parent_dir=os.path.basename(directory_path)
                    )
                    
                    contents.append(file_info)
                    logging.info(f"Обработан: {entry.name}")
                    
                except OSError as e:
                    logging.error(f"Ошибка при обработке {entry.name}: {e}")
                    
    except OSError as e:
        logging.error(f"Ошибка доступа к директории {directory_path}: {e}")
    
    return contents

def save_to_file(contents, output_file='directory_contents.txt'):
    """Сохраняет собранную информацию в текстовый файл"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Информация о содержимом директории:\n")
            f.write("=" * 50 + "\n")
            
            for item in contents:
                if item.is_directory:
                    f.write(f"📁 {item.name} | Папка | Родитель: {item.parent_dir}\n")
                else:
                    ext_info = f" | Расширение: {item.extension}" if item.extension else ""
                    f.write(f"📄 {item.name}{ext_info} | Файл | Родитель: {item.parent_dir}\n")
        
        logging.info(f"Данные сохранены в файл: {output_file}")
        
    except IOError as e:
        logging.error(f"Ошибка при записи в файл {output_file}: {e}")

def main():
    """Основная функция"""
    # Настройка парсера аргументов
    parser = argparse.ArgumentParser(description='Сбор информации о содержимом директории')
    parser.add_argument('directory', help='Путь к директории для анализа')
    parser.add_argument('--output', '-o', default='directory_contents.txt',
                       help='Имя файла для сохранения результатов (по умолчанию: directory_contents.txt)')
    
    args = parser.parse_args()
    
    # Настройка логирования
    setup_logging()
    
    logging.info(f"Начало обработки директории: {args.directory}")
    
    # Получаем информацию о содержимом
    contents = get_directory_contents(args.directory)
    
    if contents:
        # Сохраняем результаты
        save_to_file(contents, args.output)
        
        # Выводим статистику
        files_count = len([item for item in contents if not item.is_directory])
        dirs_count = len([item for item in contents if item.is_directory])
        
        print(f"\nОбработка завершена!")
        print(f"Найдено файлов: {files_count}")
        print(f"Найдено папок: {dirs_count}")
        print(f"Всего элементов: {len(contents)}")
        print(f"Результаты сохранены в: {args.output}")
        print(f"Логи сохранены в: directory_info.log")
        
        # Выводим примеры данных
        print(f"\nПримеры обработанных данных:")
        for item in contents[:5]:  # Показываем первые 5 элементов
            type_icon = "📁" if item.is_directory else "📄"
            ext_info = f", расширение: {item.extension}" if item.extension else ""
            print(f"  {type_icon} {item.name}{ext_info}")
            
        if len(contents) > 5:
            print(f"  ... и еще {len(contents) - 5} элементов")
    
    else:
        print("Не удалось собрать информацию о директории. Проверьте логи.")

if __name__ == "__main__":
    main()