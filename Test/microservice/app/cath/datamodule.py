def get_caths(conn):
    cr = conn.cursor()
    cr.execute('SELECT cath_id, cath_short_name, cath_name FROM cath')
    caths =[]
    for cath in cr.fetchall():
        caths.append({'id': cath[0], 'short_name': cath[1], 'name': cath[2]})
    return caths