import sqlite3

def make_four_point_box(bbox):
    xs = [x[0] for x in bbox]
    ys = [y[1] for y in bbox]
    return  [min(xs),min(ys),max(xs),max(ys)]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def db_action(sql,many=False):
    con = sqlite3.connect('./extractions.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    res = cur.execute(sql)
    crrc =  res.fetchone() if many == False else res.fetchall()
    def closer(commit=False):
        if commit:
            con.commit()
        cur.close()
        con.close()
    return (crrc,closer)
