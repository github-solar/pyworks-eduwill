from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    # sql - select
    sql = 'select * from employee'
    cur.execute(sql)
    rs = cur.fetchall() # 데이터 목록 리스트 반환
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    #sql = "select * from employee where emp_id='e102'"
    sql = "select * from employee where emp_id=?"
    #위의 정적검색 방식은 원리를 배우는 것이고 여기처럼 ? 표를 넣어서 동적으로 값을 입력받아 자료를 찾는 것이 일반적이다.
    # ?를 '?'로 오입력하지 마라.
    cur.execute(sql, ('e103',))
    #동적 검색방식 구현. 여기서 컴마 빠트리지 마라.
    rs = cur.fetchone()
    print(rs)
    #conn.commit()
    conn.close()


def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?, ?, ?, ?)"
    #칼럼명과 그에 대응하는 값을 ? 표로 선언하고 아래처럼 입력하는 방식이 일반적이고 이를 동적입력방식이라 한다.
    #보통 웹화면의 텍스트 입력창 등에 자료값을 입력하고 등록하는 것으로 자료값을 입력한다.
    cur.execute(sql, ('e104', '김산', 22, 5000))
    conn.commit()
    conn.close()

'''
def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set age=30 where emp_id='e103'"

    cur.execute(sql, (30, 'e103))
    conn.commit()
    conn.close()
    
    '''

#박인비 급여 25000으로 변경
def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set salary=? where emp_id=?" nj

    cur.execute(sql, (25000, 'e102'))
    conn.commit()
    conn.close()

'''
def delete_emp():
    conn = getconn()
    cur = conn.cursor()
    #사원번호 e102 삭제
    sql = "delete from employee where emp_id=?"

    cur.execute(sql, ('e102',))
    conn.commit()
    conn.close()
    
    '''

#insert_emp()
#select_emp()
update_emp()
select_emp()






