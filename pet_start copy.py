from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/pet')

def start():
    db = sqlite3.connect("pet.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'select m_num, m_name, m_addr, m_sex from member'
    ).fetchall()
    db.close()
    return render_template('start.html',items=items)

@app.route('/pet/m_join/', methods=['GET','POST'])
def m_join():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        name=request.form['mem_name']
        num=request.form['mem_number']
        addr=request.form['mem_addr']
        sex=request.form['mem_sex']
        pet_num=request.form['pet_number']
        val=(num, name, addr, sex)
        sql="INSERT into member (m_num,m_name,m_addr,m_sex) values (?,?,?,?)"
        db.execute(sql, val)

        item=db.execute(
            'select p_num, p_birth, p_sex, p_name, p_breed, p_weight from pet'
        ).fetchall()

        db.commit()
        db.close()
        return render_template('p_join.html',pet_number=request.form['pet_number'],item=item)
        #return redirect(url_for('p_join'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        item=db.execute(
            'select m_num, m_name, m_addr,m_sex from member'
        ).fetchall()
        db.close()
        return render_template('m_join.html',item=item)

@app.route('/pet/m_join/p_join', methods=['GET','POST'])
def p_join():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        name=request.form['p_name']
        num=request.form['p_number']
        breed=request.form['p_breed']
        birth=request.form['p_birth']
        sex=request.form['p_sex']
        weight=request.form['p_weight']
        val=(num, birth, sex, name, breed, weight)

        sql="INSERT into pet (p_num, p_birth, p_sex, p_name, p_breed, p_weight) values (?,?,?,?,?,?)"
        db.execute(sql, val)
        db.commit()
        db.close()
        return redirect(url_for('start'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        item=db.execute(
            'select p_num, p_birth, p_sex, p_name, p_breed, p_weight from pet'
        ).fetchall()
        db.close()
        return render_template('p_join.html',item=item)

@app.route('/pet/login/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.commit()
        db.close()
        return redirect(url_for('start'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.close()
        return render_template('login.html')

@app.route('/pet/login/mypage/', methods=['GET','POST'])
def mypage():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        
        db.commit()
        db.close()
        return redirect(url_for('login'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.close()
        return render_template('mypage.html')

@app.route('/pet/login/reservation', methods=['GET','POST'])
def reservation():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        
        db.commit()
        db.close()
        return redirect(url_for('login'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.close()
        return render_template('reservation.html')

@app.route('/pet/login/drop_out', methods=['GET','POST'])
def drop_out():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        
        db.commit()
        db.close()
        return redirect(url_for('login'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.close()
        return render_template('drop_out.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)