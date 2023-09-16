#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("""select cities.id, cities.name, states.name As states_name
                   from cities INNER JOIN states ON
                   cities.state_id=states.id;""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
