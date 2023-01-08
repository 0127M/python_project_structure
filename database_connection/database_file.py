# Importing module
import mysql.connector

class DatabaseConnection:

	@staticmethod
	def dc():
		# Creating connection object
		mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "root",
			database = "test"
		)
		cursor = mydb.cursor()
		return cursor
		# cursor.execute("select * from customers")
		# customer_table = cursor.fetchall()
		# print(customer_table)
		# print(dir(cursor))


# gs', '_handle_eof', '_handle_result', '_handle_resultset', '_handle_warnings', 
# '_last_insert_id', '_nextrow', '_raw', '_raw_as_string', '_rowcount', '_stored_results', 
# '_warning_count', '_warnings', 'add_attribute', 'arraysize', 'callproc', 'clear_attributes',
#  'close', 'column_names', 'description', 'execute', 'executemany', 'fetchall', 'fetchmany', 
#  'fetchone', 'fetchwarnings', 'get_attributes', 'lastrowid', 'nextset', 'reset', 'rowcount', 
#  'setinputsizes', 'setoutputsize', 'statement', 'stored_results', 'warning_count', 'warnings', 'with_rows'