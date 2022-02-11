from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/emails/create/')
def create_emails():
    name = request.args['name']
    email = request.args['email']
    import sqlite3
    con = sqlite3.connect('emails.db')
    cur = con.cursor()
    sql = f'''
    INSERT INTO emails (name, email) 
    VALUES ('{name}', '{email}');'''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'ok'


@app.route('/emails/read/')
def read_emails():
    import sqlite3
    id_ = request.args.get('id')
    con = sqlite3.connect('emails.db')
    cur = con.cursor()
    if id_:
        sql = f'''SELECT * FROM emails WHERE id={id_};'''
    else:
        sql = f'''SELECT * FROM emails;'''
    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    return str(results)


@app.route('/emails/update/')
def update_emails():
    import sqlite3
    id_ = request.args['id']
    name = request.args['name']
    con = sqlite3.connect('emails.db')
    cur = con.cursor()
    sql = f'''UPDATE emails SET name='{name}' WHERE id='{id_}';'''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'ok'


@app.route('/emails/delete/')
def delete_emails():
    import sqlite3
    con = sqlite3.connect('emails.db')
    cur = con.cursor()
    sql = f'''DELETE FROM emails where id=1;'''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)