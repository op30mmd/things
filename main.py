def my_function(x):
  logger.info("Starting my_function with x={}".format(x))

  # Define the result variable before using it
  result = x * 2

  logger.debug("Returning {}".format(result))
  return result
