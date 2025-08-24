import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import colorlog

# Корень проекта (где лежит папка utils)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
# Папка, в которой будут лежать лог-файлы
LOG_DIR = PROJECT_ROOT / 'utils' / 'logger' / 'logs'
# Создаём директорию, если её нет
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Настраиваем логгер
logger = logging.getLogger('api_logger')  # Имя логгера
logger.setLevel(logging.DEBUG)  # Уровень логирования

# Хендлер для ротации логов
file_handler = RotatingFileHandler(
    LOG_DIR / 'api_requests.log',  # Имя файла
    maxBytes=5*1024*1024,  # Максимальный размер файла в байтах (5 МБ)
    backupCount=5,  # Количество резервных копий
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)

# Формат логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Хендлер для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# # Формат для консоли (только сообщение)
console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)
# Цветной формат
console_formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s',  # Уровень + сообщение
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
console_handler.setFormatter(console_formatter)

# Добавляем хендлеры к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)
