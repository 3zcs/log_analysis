#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

hostname = 'localhost'
username = 'vagrant'
password = ''
database = 'news'


def most_view_article():
    db = psycopg2.connect(dbname=database)
    cur = db.cursor()
    print 'Most popular three articles of all time:'
    cur.execute('select path, count(path) from log group by path order by count(path) DESC limit 3 offset 1')  # noqa
    rows = cur.fetchall()
    for row in rows:
        print("   {} - {} views".format(row[0], str(row[1])))
    print("-" * 70)
    db.close()


def most_view_author():
    db = psycopg2.connect(dbname=database)
    cur = db.cursor()
    print 'Most popular article authors of all time:'
    cur.execute("select name, count(author) from articles join log on path like '%' || slug join authors on authors.id = author group by name order by count DESC;")  # noqa
    rows = cur.fetchall()
    for row in rows:
        print '   {} - {} views'.format(row[0], str(row[1]))
    print("-" * 70)
    db.close()


def more_1_error_():
    db = psycopg2.connect(dbname=database)
    cur = db.cursor()
    print 'Days with more than 1% errors:'
    cur.execute("select * from (select to_char(time, 'DD Mon YYYY') as day,cast(sum(case status when '200 OK' then 0 else 1 end)  AS FLOAT)/ cast(sum(case status when '200 OK' then 1 else 0 end)  AS FLOAT) * 100 as error from log group by day) as innerjoin where error > 1;")  # noqa
    rows = cur.fetchall()
    for row in rows:
        print("   {} - {}% errors".format(row[0], str("%.2f" % row[1])))
    db.close()


most_view_article()
most_view_author()
more_1_error_()
