import logging

logging.basicConfig(filename="myapp.log", level=logging.DEBUG)

logger = logging.getLogger(__name__)

def my_function(x):
  logger.info("Starting my_function with x={}".format(x))
  # ...
  logger.debug("Returning {}".format(result))
  return result

result = my_function(10)
