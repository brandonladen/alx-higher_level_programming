#!/usr/bin/python3
"""Lists all cities from the city passed as an argument"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("""select cities.name from cities INNER JOIN
                   states ON cities.state_id=states.id
                   WHERE states.name=%s;""", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
