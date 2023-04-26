import multiprocessing
import random
import time
from selenium_logic import create_session
from update_profile import get_all_profiles

list_profiles = get_all_profiles()

if __name__ == '__main__':
    with multiprocessing.Pool(5) as p:
        p.map(create_session, list_profiles)
