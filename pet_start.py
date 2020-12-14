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
        
        if num=='':
            return redirect(url_for('login_fail'))

        val=(num, name, addr, sex)
        sql="INSERT into member (m_num,m_name,m_addr,m_sex) values (?,?,?,?)"

        db.execute(sql, val)

        db.commit()
        db.close()
        return render_template('p_join.html',phoneNumber=num)
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
        
        phoneNumber=request.form['phone_Number']        
        name=request.form['p_name']
        num=request.form['p_number']
        breed=request.form['p_breed']
        birth=request.form['p_birth']
        sex=request.form['p_sex']
        weight=request.form['p_weight']

        if num=='':
            return redirect(url_for('login_fail'))

        val=(phoneNumber,num, int(birth), sex, name, breed, float(weight))
        print(val)
        sql="INSERT into pet (m_num,p_num, p_birth, p_sex, p_name, p_breed, p_weight) values (?,?,?,?,?,?,?)"
        db.execute(sql, val)

        db.commit()
        db.close()
        return redirect(url_for('start'))
        #return render_template('start.html')
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        item=db.execute(
            'select p_num, p_birth, p_sex, p_name, p_breed, p_weight from pet'
        ).fetchall()
        db.close()
        return render_template('p_join.html')

@app.route('/pet/login/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        
        user_id=request.form['user_id']
        user_pw=request.form['user_pw']

        if user_id=='' or user_pw=='':
            return redirect(url_for('login_fail'))

        user_id=user_id.split()[0]
        user_pw=user_pw.split()[0]

        if user_id==user_pw:
            sql="select m_num from member where m_num like '%"+user_id+"%'"
            phoneNumber=db.execute(sql).fetchone()

            db.commit()
            db.close()

            if phoneNumber==None:
                return redirect(url_for('login_fail'))

            phoneNumber=phoneNumber[0]

            return render_template('login_success.html',phoneNumber=phoneNumber)

        else:
            return redirect(url_for('login_fail'))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.close()
        return render_template('login.html')

@app.route('/pet/login_fail/')
def login_fail():    
    return render_template('login_fail.html')

@app.route('/pet/login/login_success/<phoneNumber>')
def login_success(phoneNumber):
    return render_template('login_success.html',phoneNumber=phoneNumber)

@app.route('/pet/login/login_success/mypage/<phoneNumber>/', methods=['GET','POST'])
def mypage(phoneNumber):
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
        return render_template('mypage.html',phoneNumber=phoneNumber)

@app.route('/pet/login/login_success/reservation/<phoneNumber>/', methods=['GET','POST'])
def reservation(phoneNumber):
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        m_num=request.form['phoneNumber']
        i_num=request.form['instructor']
        p_num=request.form['pet']
        day=request.form['day']
        time=request.form['time']
        
        if m_num==''or i_num==''or p_num==''or day=='' or time=='':
            return redirect(url_for('login_fail'))
        
        val=(m_num,i_num,p_num,day,time)
        sql="INSERT into reservation (m_num,i_num,p_num,r_day,r_time) values (?,?,?,?,?)"

        db.execute(sql, val)

        db.commit()
        db.close()
        return redirect(url_for('login_success',phoneNumber=phoneNumber))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        sql1="select p_name, p_num from pet where m_num='"+phoneNumber+"'"
        p_item=db.execute(sql1).fetchall()

        sql2="select i_name, i_num from instructor"
        i_item=db.execute(sql2).fetchall()
        
        db.close()
        return render_template('reservation.html',phoneNumber=phoneNumber,p_item=p_item,i_item=i_item)

@app.route('/pet/login/login_success/drop_out/<phoneNumber>/', methods=['GET','POST'])
def drop_out(phoneNumber):
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        sql="DELETE FROM member WHERE m_num='"+phoneNumber+"'"
        result=db.execute(sql)
        db.commit()
        db.close()
        return redirect(url_for('start'))
    else:        
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        db.close()
        return render_template('drop_out.html',phoneNumber=phoneNumber)

@app.route('/pet/login/login_success/mypage/pet_add/<phoneNumber>/', methods=['GET','POST'])
def pet_add(phoneNumber):
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        
        phoneNumber=request.form['phone_Number']        
        name=request.form['p_name']
        num=request.form['p_number']
        breed=request.form['p_breed']
        birth=request.form['p_birth']
        sex=request.form['p_sex']
        weight=request.form['p_weight']

        if num=='':
            return redirect(url_for('login_fail'))
            #return redirect(url_for('mypage',phoneNumber=phoneNumber))

        val=(phoneNumber,num, int(birth), sex, name, breed, float(weight))
        print(val)
        sql="INSERT into pet (m_num,p_num, p_birth, p_sex, p_name, p_breed, p_weight) values (?,?,?,?,?,?,?)"
        db.execute(sql, val)

        db.commit()
        db.close()
        return redirect(url_for('mypage',phoneNumber=phoneNumber))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        item=db.execute(
            'select p_num, p_birth, p_sex, p_name, p_breed, p_weight from pet'
        ).fetchall()
        db.close()
        return render_template('pet_add.html',phoneNumber=phoneNumber)

@app.route('/pet/login/login_success/mypage/pet_delte/<phoneNumber>/', methods=['GET','POST'])
def pet_delete(phoneNumber):
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        p_num=request.form['pet']
        sql="DELETE FROM pet WHERE p_num='"+p_num+"'"

        db.execute(sql)

        db.commit()
        db.close()
        return redirect(url_for('mypage',phoneNumber=phoneNumber))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        sql1="select p_name, p_num from pet where m_num='"+phoneNumber+"'"
        p_item=db.execute(sql1).fetchall()
        
        db.close()
        return render_template('pet_delete.html',phoneNumber=phoneNumber,p_item=p_item)

@app.route('/pet/login/login_success/mypage/reservation_check/<phoneNumber>/')
def reservation_check(phoneNumber):
    db = sqlite3.connect("pet.db")
    db.row_factory = sqlite3.Row

    sql="SELECT i_name,i.i_num, p_name, r_day, r_time \
        FROM reservation r, instructor i, pet p \
        WHERE r.i_num=i.i_num and p.p_num=r.p_num and r.m_num='"+phoneNumber+ \
        "' order by p_name, r_day"

    items = db.execute(sql).fetchall()

    db.close()
    return render_template('reservation_check.html',phoneNumber=phoneNumber, items=items)

@app.route('/pet/login/login_success/mypage/pet_check/<phoneNumber>/', methods=['GET','POST'])
def pet_check(phoneNumber):
    db = sqlite3.connect("pet.db")
    db.row_factory = sqlite3.Row

    sql1="select * from pet where m_num='"+phoneNumber+"'"
    p_item=db.execute(sql1).fetchall()
        
    db.close()
    return render_template('pet_check.html',phoneNumber=phoneNumber,p_item=p_item)

@app.route('/pet/login/login_success/mypage/pet_check/pet_edit/<phoneNumber>/<p_num>', methods=['GET','POST'])
def pet_edit(phoneNumber,p_num):
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        
        name=request.form['p_name']
        num=request.form['p_number']
        weight=request.form['p_weight']
        
        val=(name, weight)
        sql="update pet set p_name=?,p_weight=? where m_num='"+phoneNumber+"' and p_num='"+num+"'"

        db.execute(sql, val)

        db.commit()
        db.close()
        return redirect(url_for('pet_check',phoneNumber=phoneNumber))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        sql1="select * from pet where m_num='"+phoneNumber+"' and p_num='"+p_num+"'"
        p_item=db.execute(sql1).fetchone()
        
        db.close()
        return render_template('pet_edit.html',phoneNumber=phoneNumber,p_item=p_item)

@app.route('/pet/login/login_success/mypage/pet_diary_check/<phoneNumber>/')
def pet_diary_check(phoneNumber):
    db = sqlite3.connect("pet.db")
    db.row_factory = sqlite3.Row

    sql="select p.p_name,log_day,sleep,diet \
         from daily_log d, pet p\
         where d.m_num='"+phoneNumber+"' and p.p_num=d.p_num\
         order by p.p_name, log_day"

    items = db.execute(sql).fetchall()

    db.close()
    return render_template('pet_diary_check.html',phoneNumber=phoneNumber, items=items)

@app.route('/pet/login/login_success/mypage/my_info/<phoneNumber>/', methods=['GET','POST'])
def my_info(phoneNumber):
    if request.method=='POST':
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row
        
        name=request.form['mem_name']
        num=request.form['mem_number']
        addr=request.form['mem_addr']
        sex=request.form['mem_sex']
        
        if num=='':
            return redirect(url_for('login_fail'))
        
        val=(num, name, addr, sex)
        sql="update member set m_num=?,m_name=?, m_addr=?, m_sex=? where m_num='"+phoneNumber+"'"

        db.execute(sql, val)

        db.commit()
        db.close()
        return redirect(url_for('mypage',phoneNumber=num))
    else:
        db = sqlite3.connect("pet.db")
        db.row_factory = sqlite3.Row

        sql="select * from member where m_num='"+phoneNumber+"'"
        item=db.execute(sql).fetchone()
        db.close()
        return render_template('my_info.html',phoneNumber=phoneNumber,item=item)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
