
def make_four_point_box(bbox):
    xs = [x[0] for x in bbox]
    ys = [y[1] for y in bbox]
    return  [min(xs),min(ys),max(xs),max(ys)]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d