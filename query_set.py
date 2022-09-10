def query_dict(query,session):
    data = {}
    rows = session.execute(query)
    for row in rows:
        data.update({"English":row[0],"Hindi":row[1],"mrtext":row[2]})
    return data

