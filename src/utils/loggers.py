import logging
import os

def get_logger(name : str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        if not os.path.exists('src\logs'):
            os.mkdirs('src\logs')
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler('src/logs/app.log')
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandle(file_handler)
    return logger 



