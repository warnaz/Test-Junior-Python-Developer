import datetime
import json
from models import con, cursor


def update_cookie_profile(id: int, cookies: list):
    update_sql = '''UPDATE Cookie_Profile 
                        SET cookie=?, launch_date=?, launch_count=launch_count+1
                    WHERE id=?'''

    json_cookie = json.dumps(cookies)
    cursor.execute(update_sql, [json_cookie, datetime.datetime.now(), id])
    con.commit()


def get_saved_cookie(id: int) -> str or None:
    select_sql = '''SELECT cookie FROM Cookie_Profile WHERE id=?'''

    json_cookie = cursor.execute(select_sql, [id]).fetchall()[0][0]

    if json_cookie:
        return json.loads(json_cookie)
    else:
        return None


def get_all_profiles():
    select_sql = '''SELECT id, cookie FROM Cookie_Profile'''
    result = cursor.execute(select_sql).fetchall()

    return result
