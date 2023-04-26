import datetime
from models import con, cursor


# Initial addition of 15 elements
def init_add_values(date_time):
    insert_with_param = """INSERT INTO 'Cookie_Profile'
                          ('created_at')
                          VALUES (?);"""

    cursor.execute(insert_with_param, (date_time,))
    con.commit()


for _ in range(15):
    init_add_values(datetime.datetime.now())
