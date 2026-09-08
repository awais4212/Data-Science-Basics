import logging
logging.basicConfig(
    filemode='w',
    filename='app.log',
    level = logging.DEBUG,
    format= '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)