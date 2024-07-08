import psycopg2
from psycopg2 import sql

# PostgreSQL connection parameters
remote_host = 'vehicaltracking.c3isgu44krjo.ap-south-1.rds.amazonaws.com'
remote_port = '5432'  # replace with your remote port
remote_dbname = 'VehicalTracking'
remote_user = 'postgres'
remote_password = 'PmAyaIhGmVVUtW22TNgh'

local_host = 'localhost'
local_port = '5432'  # replace with your local port
local_dbname = 'your_local_db_name'
local_user = 'your_local_username'
local_password = 'your_local_password'

table_name = 'your_table_name_to_backup'

try:
    # Connect to remote PostgreSQL
    remote_conn = psycopg2.connect(
        host=remote_host,
        port=remote_port,
        dbname=remote_dbname,
        user=remote_user,
        password=remote_password
    )
    remote_cursor = remote_conn.cursor()

    # Connect to local PostgreSQL
    local_conn = psycopg2.connect(
        host=local_host,
        port=local_port,
        dbname=local_dbname,
        user=local_user,
        password=local_password
    )
    local_cursor = local_conn.cursor()

    # Query to select data from remote table
    query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    remote_cursor.execute(query)

    # Fetch all rows
    rows = remote_cursor.fetchall()

    # Dump data into local table
    for row in rows:
        insert_query = sql.SQL("INSERT INTO {} VALUES ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(sql.Literal(cell) for cell in row)
        )
        local_cursor.execute(insert_query)

    # Commit changes
    local_conn.commit()
    print(f"Data from table '{table_name}' backed up and dumped successfully to local database.")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Closing database connections
    if remote_conn:
        remote_cursor.close()
        remote_conn.close()
    if local_conn:
        local_cursor.close()
        local_conn.close()
