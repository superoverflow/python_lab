#!/usr/bin/python
import logging

FORMAT = '%(asctime)-15s [%(levelname)s] %(filename)s %(lineno)d: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logging.debug("Hello World")
