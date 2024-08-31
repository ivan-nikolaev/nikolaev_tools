from logging import getLogger, Logger, Formatter, StreamHandler
from logging.handlers import TimedRotatingFileHandler
 
def add_file_handler(logger: Logger, file_name: str, level: str):
    fmt = "[%(asctime)s] %(message)s (%(levelname)s)"
    date_fmt = "%d.%m.%y %H:%M:%S"
    file_formatter = Formatter(fmt=fmt, datefmt=date_fmt)
    file_handler = TimedRotatingFileHandler(filename=file_name,
                                            when="d",
                                            interval=1,
                                            backupCount=7,
                                            encoding="UTF-8")
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
 
 
def add_console_handler(logger: Logger, level: str):
    console_handler = StreamHandler()
    fmt = "[%(asctime)s] %(message)s (%(levelname)s)"
    date_fmt = "%d.%m.%y %H:%M:%S"
    console_formatter = Formatter(fmt=fmt, datefmt=date_fmt)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)
    
def main():
    logger = getLogger()
    logger.setLevel("DEBUG")
    add_console_handler(logger, level="DEBUG")
    add_file_handler(logger, file_name='log.txt', level="DEBUG")
 
    logger.info('Привет мир!')
 
 
if __name__ == '__main__':
    main()