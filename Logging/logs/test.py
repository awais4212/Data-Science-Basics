from logger import logging

def add(x,y):
    logging.debug("The addition Opearation statring")
    return x+y

logging.debug('It took place')
add(2,4)