import sqlite3

def alter_table(database_name, table_name, operation, ):
	pass

def create_table(database_name, table_name, table_headers):
	database_object = sqlite3.connect(database_name)
	database_cursor = database_object.cursor()

	sql_cmd = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ( '

	for th in table_headers:
		sql_cmd = sql_cmd + ' '.join(th)
		if table_headers[-1] != th:
			sql_cmd = sql_cmd + ', '

	sql_cmd = sql_cmd + ' );'
	
	database_cursor.execute(sql_cmd)
	database_object.commit()
	database_object.close()

def insert_data(database_name, table_name, format, data):
	database_object = sqlite3.connect(database_name)
	database_cursor = database_object.cursor()

	sql_cmd = 'INSERT INTO ' + table_name + ' VALUES ('

	for f in format:
		sql_cmd = sql_cmd + ':' + f[0]
		if format[-1] != f:
			sql_cmd = sql_cmd + ', '

	sql_cmd = sql_cmd + ')'

	database_cursor.execute(sql_cmd,data)

	database_object.commit()
	database_object.close()

def retrieve_table(database_name, table_name, columns, parameter_str):
	database_object = sqlite3.connect(database_name)
	database_cursor = database_object.cursor()

	if(len(columns)>1):
		col_list = ','.join(columns.split())
	else:
		col_list = columns

	sql_cmd = 'SELECT ' + col_list + ' FROM ' + table_name
	
	if parameter_str:
		sql_cmd = sql_cmd + ' WHERE ' + parameter_str

	database_cursor.execute(sql_cmd)
	#print(sql_cmd)	
	return database_cursor.fetchall()
	
def update_table(database_name, table_name, format, data, id_name, id_value):
	database_object = sqlite3.connect(database_name)
	database_cursor = database_object.cursor()

	sql_cmd = 'UPDATE ' + table_name + ' SET '

	index = 0;
	update_array = []
	for f in format:
		if f[0] != id_name:
			sql_cmd = sql_cmd + f[0] + ' = ?'# + data[index]
			update_array.append(data[index])
			if format[-1] != f:
				sql_cmd = sql_cmd + ', '
		index = index + 1

	sql_cmd = sql_cmd + ' WHERE ' + id_name + ' = ?'

	update_array.append(id_value)	
	print(sql_cmd)
	print(update_array)
	database_cursor.execute(sql_cmd, update_array)

	database_object.commit()
	database_object.close()



























