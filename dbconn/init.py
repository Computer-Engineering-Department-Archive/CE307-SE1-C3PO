from tables import *


def init_category():
    category()
    print("CATEGORY_ELEMENT TABLE CREATED.")
    category_default()
    print("CATEGORY_ELEMENT DEFAULT VALUES INSERTED.")


def init_url():
    url()
    print("URL TABLE CREATED.")
    url_init()
    print("URL VALUES INSERTED")


if __name__ == "__main__":
    print('DATABASE INITIALIZATION')
    # init_category()
    # init_url()
