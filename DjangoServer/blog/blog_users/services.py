import pandas as pd
from random_id import random_id
from sqlalchemy import create_engine

class UserServices(object):
    def __init__(self):
        global random, random_email, random_nickname, random_password
        random = [i for i in range(1,101)]
        # random = [random_id() for i in range(100)]
        random_email = [f'{random_id()}@naver.com' for i in range(100)]
        random_nickname = [random_id() for i in range(100)]
        random_password = [random_id() for i in range(100)]

    def random_id(self):
        df = pd.DataFrame({
            'blog_userid' : random,
            'email' : random_email,
            'nickname' : random_nickname,
            'password' : random_password
        })
        ls = list(df)
        df.duplicated(['blog_userid'])
        # engine = create_engine(
        #     "mysql+pymysql://root:root@localhost:3306/mydb",
        #     encoding='utf-8')
        # df.to_sql(name='blog_users',
        #           if_exists='append',
        #           con=engine,
        #           index=False)
        return ls


if __name__ == '__main__':
    UserServices().random_id()