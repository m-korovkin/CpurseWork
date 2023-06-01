import datetime
import db
from models import Trip, Response
from config import *


def handleGetAllTickets(request):
    # data = list of objects "Trip"
    data = db.tripGetAll()
    body = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Фирма</title><link rel="stylesheet" href="style.css"></head><body><div class="main"><form action="getTicketsList" method="get"><div class="second"><div class="route"><div><div class="where_wrapper"><div class="where_block"><label class="where_label">Выберите маршрут:</label><div class="block_box"><select tabindex="1" class="box" name="route"> <option value="mn" selected>Москва - Нижний Новгород</option><option value="mp">Москва - Санкт-Петербург</option><option value="nm">Нижний Новгород - Москва</option><option value="mp">Нижний Новгород - Санкт-Петербург</option><option value="pm">Санкт-Петербург - Москва</option><option value="pn">Санкт-Петербург - Нижний Новгород</option></select></div></div></div></div></div><div class="data"><div class="data2"><form><p class="calendar_p">Выберите дату:<input tabindex="2" class="calendar" type="date" name="calendar" value="01-06-2023" max="05-06-2023" min="05-05-2023"></p></form></div></div><div class="passengers"><div class="passengers_2"><label class="passengers_label">Пассажиры:</label><div class="pass_block"><select tabindex="3" class="pass" name="quantity"><option value="1" selected>1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option></select></div></div></div><div class="find"><button class="find_button" role="button" type="submit"><span>Найти билет</span></button></div></div></form></div>'
    for trip in data:
        body += f'<br><div class="ticket"><div class="tick"><div class="ticket_noprice"><div class="trip"><label class="trip_label">{trip.cityFrom} - {trip.cityTo}</label></div><div class="inf"><label class="bus_num">Автобус номер {trip.busNumber}</label><label class="station_num">Вокзал номер {trip.stationNumber}</label></div></div><div class="sep"></div><div class="ticket_price"><div class="price"><label class="label_price">{trip.price}</label></div><div class="ticket_date"><label>{trip.date}</label></div></div><div class="sep"></div><div class="block_btn"><form method="post" action="choosePlace"><input type="text" name="choosePlace" value="{trip.id}" hidden><button value="uniqID03" class="choose_btn" role="button" type="submit"><span>Выбрать билет</span></button></form></div></div></div>'
    body += '<div class="map"><span><a class="custom-btn btn-2" href="map.html">Карта предприятий</a></span></div></body></html>'
    body = body.encode('utf-8')
    
    contentType = 'text/html; charset=utf-8'
    headers = [('Content-Type', contentType),
               ('Content-Length', len(body))]
    status, reason = '200', 'OK'
    print(f'[{datetime.datetime.now()}] "{status} {reason}"')
    return Response(status, reason, headers, body)


def handleChoosePlace(request):
    """
    Переход со страницы выбора рейса на страницу выбора места
    """
    # строка с кодом от формы
    # body = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Форма</title><link rel="stylesheet" href="form.css"></head><body><div class="form-block-left"><form action="index.php" method="post" class="railway"><h3>Введите данные:</h3><span></span><div class="form-group"><div class="block-input"><input name="name"  onfocus="if(this.value=="ФИО") this.value='';" onblur="if(!this.value)this.value="ФИО";" type="text" value="ФИО"/></div> <div class="block-input"> <input name="email" onfocus="if(this.value=="Серия и номер паспорта") this.value="";" onblur="if(!this.value)this.value="Серия и номер паспорта";" type="text" value="Серия и номер паспорта"/> </div> <div class="block-input"><input name="phone" onfocus="if(this.value=="Номер телефона") this.value='';" onblur="if(!this.value)this.value="Номер телефона";" type="tel" value="Номер телефона"/></div></div><div class="submit-button"><input class="button" type="submit" value="Отправить"></div></form></div></body></html>'
    # print(request.body.split('=')[1])
    trip_id = request.body.split('=')[1]
    # Тут идет запрос в бд поиск рейса по id,по нему вытаскиваем все данные маршрута
    body = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title><link rel="stylesheet" href="choose_place.css"></head><body><div class="seatmap"><div class="seatmap_title">        <span>Выберите место на схеме автобуса</span></div><div class="free_or_not"><div class="free"><span class="span_free"></span> - Свободное</div><div class="not_free"><span class="span_not_free"></span>- Занятое</div></div><div class="tir"><div class="tir_2"><div class="tir_3"><div class="tir_4"><div class="first_row">'
    for i in range(10):
        body += f'<div class="ticket_place"><div class="block_span_{i+1}"><span>{i+1}</span></div></div>'
    body += '</div><div class="first_row">'
    for i in range(10):
        body += f'<div class="ticket_place"><div class="block_span_{i+11}"><span>{i+11}</span></div></div>'
    body += '</div></div></div></div><style contenteditable>.ticket_place {border: 2px solid black;}</style></body></html>'
    body = body.encode('utf-8')
    
    contentType = 'text/html; charset=utf-8'
    headers = [('Content-Type', contentType),
               ('Content-Length', len(body))]
    status, reason = '200', 'OK'
    print(f'[{datetime.datetime.now()}] "{status} {reason}"')
    return Response(status, reason, headers, body)


def handleLoginAdmin(request):
    """
    Проверка введенных данных на соответствие логину и паролю админа
    переадресация на админ панель либо возврат на страницу авторизации
    """
    contentType = 'text/html; charset=utf-8'
    name, passw = str(request.body.split('&')[0].split('=')[1]), str(request.body.split('&')[1].split('=')[1])
    # print(name, passw)
    if name == admName and passw == admPass:
        status, reason = '200', 'OK'
        body = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Фирма</title><link rel="stylesheet" href="style.css"></head><body><h1>ADMIN PANEL</h1></body></html>'
        body = body.encode('utf-8')
    else:
        status, reason = '401', 'Unauthorized'
        with open(f'{config.directoryName}admin.html', 'rb') as file:
            body = file.read()
    headers = [('Content-Type', contentType),
               ('Content-Length', len(body))]
    return Response(status, reason, headers, body)


def handleGetTickets(request):
    """
    поиск автобусов, соответствующих запросу пользователя и отображение их на странице
    """
    query = [i.split('=') for i in request.query.split('&')]
    route, date, quantity = query[0][1], query[1][1], query[2][1]
    cityA, cityB = '', ''
    for city in citiesScheme:
        if route[0] == city[0]:
            cityA = city[1]
        if route[1] == city[0]:
            cityB = city[1]

    routesFromDB = [Trip('01', 'Москва', 'Нижний Новгород', '2023-06-19', '17:30', '1999', '11111001011000010100', '10', '3'), Trip('02', 'Санкт-Петербург', 'Москва', '2023-06-06', '09:45', '1400', '00001100000000111101', '229', '3')]
    returnList = []
    print(returnList)
    for trip in routesFromDB:
        print(f"trip.cityFrom {trip.cityFrom} : cityA {cityA} : trip.cityTo {trip.cityTo} : cityB {cityB} : trip.date {trip.date} : date {date}")
        if str(trip.cityFrom) == str(cityA) and str(trip.cityTo) == str(cityB) and str(trip.date) == str(date):
            returnList.append(trip.id)
  
    body = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Фирма</title><link rel="stylesheet" href="style.css"></head><body><div class="main"><form action="getTicketsList" method="get"><div class="second"><div class="route"><div><div class="where_wrapper"><div class="where_block"><label class="where_label">Выберите маршрут:</label><div class="block_box"><select tabindex="1" class="box" name="route"> <option value="mn" selected>Москва - Нижний Новгород</option><option value="mp">Москва - Санкт-Петербург</option><option value="nm">Нижний Новгород - Москва</option><option value="mp">Нижний Новгород - Санкт-Петербург</option><option value="pm">Санкт-Петербург - Москва</option><option value="pn">Санкт-Петербург - Нижний Новгород</option></select></div></div></div></div></div><div class="data"><div class="data2"><form><p class="calendar_p">Выберите дату:<input tabindex="2" class="calendar" type="date" name="calendar" value="01-06-2023" max="05-06-2023" min="05-05-2023"></p></form></div></div><div class="passengers"><div class="passengers_2"><label class="passengers_label">Пассажиры:</label><div class="pass_block"><select tabindex="3" class="pass" name="quantity"><option value="1" selected>1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option></select></div></div></div><div class="find"><button class="find_button" role="button" type="submit"><span>Найти билет</span></button></div></div></form></div>'
    for uniqID in returnList:
        for trip in routesFromDB:
            if trip.id == uniqID:
                content = f'<div class="ticket"><div class="tick"><div class="ticket_noprice"><div class="trip"><label class="trip_label">{trip.cityFrom} - {trip.cityTo}</label></div><div class="inf"><label class="bus_num">Автобус номер {trip.busNumber}</label><label class="station_num">Вокзал номер {trip.stationNumber}</label></div></div><div class="sep"></div><div class="ticket_price"><div class="price"><label class="label_price">{trip.price}</label></div><div class="ticket_date"><label>{trip.date}</label></div></div><div class="sep"></div><div class="block_btn"><form method="post" action="choosePlace"><input type="text" name="choosePlace" value="{trip.id}" hidden><button value="uniqID03" class="choose_btn" role="button" type="submit"><span>Выбрать билет</span></button></form></div></div></div>'
                body += content

    body += '<div class="map"><span><a class="custom-btn btn-2" href="map.html">Карта предприятий</a></span></div></body></html>'
    body = body.encode('utf-8')
    
    content_type = 'text/html; charset=uft-8'
    status, reason = '200', 'OK'
    headers = [('Content-Type', content_type), ('Content-Length', len(body))]
    print(f'[{datetime.datetime.now()}] "{status} {reason}"')
    return Response(status, reason, headers, body)


def handleBuyTicket(request):
    """
    Покупка билета
    """
    #TODO Создание записи в бд
    content_type = 'text/html; charset=uft-8'
    try:
        with open(f'{directoryName}"test.html"', 'rb') as file:
            body = file.read()
        status, reason = '202', 'Created'
    except Exception as e:
        print(e)
        body = 'Sorry, bro! No page...'.encode('utf-8')
        status, reason = '404', 'Not Found'
    headers = [('Content-Type', content_type), ('Content-Length', len(body))]
    print(f'[{datetime.datetime.now()}] "{status} {reason}"')
    return Response(status, reason, headers, body)


def handleReturnTicket(request):
    """
    # Возврат билета
    """
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
    print(f'[{datetime.datetime.now()}] "{status} {reason}"')
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
