if __name__ == '__main__':

    import pymysql, sys, os

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(BASE_DIR)

    import settings

    db = pymysql.connect(
        settings.DATABASES['default']['HOST'],
        settings.DATABASES['default']['USER'],
        settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['NAME'],
    )

    cursor = db.cursor()

    cursor.execute('select * from auth_user')

    fetchone = cursor.fetchone()

    print('auth_user: %s' % fetchone[2])

    cursor.execute('select * from blob_question')
    fetchall = cursor.fetchall()
    for row in fetchall:
        id = row[0]
        question = row[1]
        pub_date = row[2]
        print('id:%s, question:%s, pub_date:%s' % (id, question, pub_date))

    db.close()
