from tables import *


def init_category():
    category()
    print("CATEGORY_ELEMENT TABLE CREATED.")
    category_default()
    print("CATEGORY_ELEMENT DEFAULT VALUES INSERTED.")


def init_url():
    urls()
    print("URL TABLE CREATED.")
    urls_init()
    print("URL VALUES INSERTED.")


def init_messages():
    message()
    print("MESSAGES TABLE CREATED.")


def init_validation():
    validation()
    print("VALIDATION TABLE CREATED.")


def init_suspicious():
    suspicious()
    print("SUSPICIOUS TABLE CREATED.")


if __name__ == "__main__":
    print('DATABASE INITIALIZATION')
    # init_category()
    # init_url()
