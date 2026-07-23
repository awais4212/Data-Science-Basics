import logging

logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %Y:%M:%S',
    handlers=[
        logging.FileHandler('arithmaticApp.Log'),
        logging.StreamHandler()   
    ]
)

logger = logging.getLogger('arithmaticApp')

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a,b):
    result = a-b
    logger.debug(f"subtraccting {a} - {b} = {result}")
    return result

def mul(a,b):
    result = a*b
    logger.debug(f"multiplying {a} * {b} = {result}")
    return result


def div(a,b):
    result = a/b
    logger.debug(f"dividing {a} / {b} = {result}")
    return result

add(10,20)
sub(4,2)
mul(4,4)
div(10,2)