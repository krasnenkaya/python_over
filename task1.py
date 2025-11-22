import logging

# Настройка основного логгера
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Создаем форматтер
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для debug_info.log (только DEBUG и INFO)
debug_handler = logging.FileHandler('debug_info.log')
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

# Обработчик для warnings_errors.log (WARNING и выше)
warning_handler = logging.FileHandler('warnings_errors.log')
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_handler)
logger.addHandler(warning_handler)

# Тестируем логирование
logger.debug('Отладочное сообщение')
logger.info('Информационное сообщение')
logger.warning('Предупреждение')
logger.error('Ошибка')
logger.critical('Критическая ошибка')

print("Логи записаны в файлы debug_info.log и warnings_errors.log")