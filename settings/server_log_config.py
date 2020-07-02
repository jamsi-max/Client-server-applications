import logging
from datetime import datetime

logger = logging.getLogger('app.main_server')
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s - %(message)s "
    )
log_file = logging.FileHandler(f'log/{datetime.now()}_serverg .log', encoding='utf-8')
log_file.setLevel(logging.DEBUG)
log_file.setFormatter(formatter)

logger.addHandler(log_file)
logger.setLevel(logging.DEBUG)
