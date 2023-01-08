
# importing module
import logging
from datetime import datetime

class GetLog:

	@staticmethod
	def get_log_details():
		now = datetime.now()
		dt_string = now.strftime("%d_%m_%Y_T%H_%M_%S")

		# Create and configure logger
		# logging.basicConfig(filename=f"""../new_file_{dt_string}.log""",
		# 					format='%(asctime)s %(message)s',
		# 					filemode='w')

		# Creating an object
		logger = logging.getLogger()

		# Setting the threshold of logger to DEBUG
		logger.setLevel(logging.DEBUG)

		# Test messages
		logger.error(f"""{dt_string}_Harmless debug Message""")	
		logger.debug(f"""{dt_string}Harmless debug Message""")
		logger.info(f"""{dt_string}Harmless debug Message""")

		# logger.info("Just an information")
		# logger.warning("Its a Warning")
		# logger.error("Did you try to divide by zero")
		# logger.critical("Internet is down")

grtlogobj = GetLog()
grtlogobj.get_log_details()