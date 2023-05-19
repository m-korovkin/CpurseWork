# import mysql.connector
from messages import Response
from config import *


def handleGetTickets(request):
    pass


def handleBuyTicket(request):
    #TODO Создание записи в бд
    content_type = 'text/html; charset=uft-8'
    try:
        with open(f'{directoryName}{mainPageName}', 'rb') as file:
            body = file.read()
        status, reason = '202', 'Created'
    except Exception as e:
        print(e)
        body = 'Sorry, bro! No page...'.encode('utf-8')
        status, reason = '404', 'Not Found'
    headers = [('Content-Type', content_type), ('Content-Length', len(body))]
    return Response(status, reason, headers, body)


def handleReturnTicket(request):
    #TODO Удаление брони билета в бд
    content_type = 'text/html; charset=uft-8'
    try:
        with open(f'{directoryName}{mainPageName}', 'rb') as file:
            body = file.read()
        status, reason = '202', 'Created'
    except Exception as e:
        print(e)
        body = 'Sorry, bro! No page...'.encode('utf-8')
        status, reason = '404', 'Not Found'
    headers = [('Content-Type', content_type), ('Content-Length', len(body))]
    return Response(status, reason, headers, body)


"""
def handle_create_task(request):
    pass


def handle_add_task(request):
    pass


def handle_edit_task(request):
    pass


def handle_delete_task(request):
    pass
"""
"""
def handle_create_user(request):
    body_arr = str(request.body).split('&')
    for i in range(len(body_arr)):
        body_arr[i] = body_arr[i].split('=')[1]
    #print(body_arr)
    path = request.target
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=password_python, database=database_name)
    mycursor = mydb.cursor()
    sql = "INSERT INTO Users (UserName, UserPass, UserPhone, UserSex) VALUES (%s, %s, %s, %s)"
    val = []
    for el in body_arr:
        val.append(el)
    #print(f'val = {val}')
    mycursor.execute(sql, val)
    
    mydb.commit()
    content_type = 'text/html; charset=uft-8'
    try:
        with open(f'files{path}', 'rb') as file:
            body = file.read()
        status, reason = '202', 'Created'
    except Exception as e:
        #print(e)
        body = 'Sorry, bro! No page...'.encode('utf-8')
        status, reason = '404', 'Not Found'
    headers = [('Content-Type', content_type), ('Content-Length', len(body))]
    return Response(status, reason, headers, body)
"""
"""
def handle_get_tasks(request):
    with open("db.csv", "r") as db:
        db_data = db.read()
    tasks_list = db_data.split(";")
    tasks = [task.split(',') for task in tasks_list]
    try:
        print(tasks[-1][3])
    except Exception:
        tasks.pop(-1)
    for task in tasks:
        print(task)
    content_type = 'text/html; charset=utf-8'
    body = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Матрица Эйзенхауэра</title><link rel="stylesheet" href="page.css"></head><body><div class="body"><div class="main"><div class="matrix"><div class="matrix-l"><a>Важно</a><br><br><br><br><br><br><br><br><br><br><a>Не важно</a></div><div class="matrix-s"><div class="matrix-header"><a>Срочно</a><a>Не срочно</a></div><div class="block-a">'
    for task in tasks:
        if task[3] == 'lt':
            body += f'<div>{task[0]}{task[1]}</div>'
    body += '<form action="handle_create_task" method="get"><button type="submit" value="lt" name="new_task">Добавить задачу</button></div><div class="block-b">'
    for task in tasks:
        if task[3] == 'rt':
            body += f'<div>{task[0]}{task[1]}</div>'
    body += '<button type="submit">Добавить задачу</button></div><div class="block-c">'
    for task in tasks:
        if task[3] == 'lb':
            body += f'<div>{task[0]}{task[1]}</div>'
    body += '<button type="submit">Добавить задачу</button></div><div class="block-d">'
    for task in tasks:
        if task[3] == 'rb':
            body += f'<div>{task[0]}{task[1]}</div>'
    body += '<button type="submit">Добавить задачу</button></div></div></div><div class="card"><form><button type="submit">Создать</button></form></div></div></div></body></html>'
    #body = 'Sorry, bro! No page...'.encode('utf-8')
    status, reason = '200', 'OK'
    body = body.encode('utf-8')
    headers = [('Content-Type', content_type), ('Content-Length', len(body))]
    return Response(status, reason, headers, body)
"""

"""
def handle_get_users(request):
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=password_python, database=database_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Users")
    myresult = mycursor.fetchall()

    contentType = 'text/html; charset=utf-8'
    body = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>'
    
    body += f'<div>Пользователи ({len(myresult)})</div>'
    body += '<table>'
    #body += f'<tr>#{x[0]}, {x[1]}, {x[2]}, {x[3]}, {x[4]}</tr>'
    for x in myresult:
        body += f'<tr><td>#{x[0]}</td><td>{x[1]}</td><td>{x[2]}</td><td>{x[3]}</td><td>{x[4]}</td></tr>'
    body += '</table>'
    body += '<a style="font-size: 120%; color: black; text-decoration: none;" href="index.html">Главная</a>'
    body += '</body></html>'
    body = body.encode('utf-8')
    
    headers = [('Content-Type', contentType),
               ('Content-Length', len(body))]
    status, reason = '200', 'OK', 
    return Response(status, reason, headers, body)
"""

if __name__ == '__main__':
    handleBuyTicket('example')
    # handle_create_user('123')
