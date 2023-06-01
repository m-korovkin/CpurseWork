import sqlite3 as db
from models import Trip


def tripGetAll():
	con = db.connect('my.db')
	cur = con.cursor()
	tripList = [[part for part in el] for el in cur.execute('SELECT * FROM trip')]
	returnList = []
	for el in tripList:
		id_, cityFrom, cityTo, date, time, price, free_places, busNumber, stationNumber = el[0], el[1], el[2], el[3], el[4], el[5], el[6], el[7], el[8]
		print(id_, cityFrom, cityTo, date, time, price, free_places, busNumber, stationNumber)
		returnList.append(Trip(id_, cityFrom, cityTo, date, time, price, free_places, busNumber, stationNumber))
	return returnList


def tripCreate():
	con = db.connect('my.db')
	cur = con.cursor()
	query = "CREATE TABLE IF NOT EXISTS trip(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, city_from TEXT, city_to TEXT, date_ TEXT, time_ TEXT, price TEXT, free_places TEXT, bus_number TEXT, station_number TEXT);"
	cur.execute(query)


def tripAppend(tripList):
	dbName = 'my.db'
	con = db.connect(dbName)
	cur = con.cursor()
	data = [(el.id, el.cityFrom, el.cityTo, el.date, el.time, el.price, el.free_places, el.busNumber, el.stationNumber) for el in tripList]
	cur.executemany("INSERT INTO trip VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
	res = cur.execute("SELECT * FROM trip")
	res.fetchall()


def tripAppend1():
	dbName = 'my.db'
	
	con = db.connect(dbName)
	cur = con.cursor()
	sql = 'INSERT INTO trip (id, city_from, city_to, date_, time_, price, free_places, bus_number, station_number) values(?, ?, ?, ?, ?, ?, ?, ?)'
	data = []
	for row in range(len(tripList)):
		data.append((tripList[row].cityFrom, tripList[row].cityTo, tripList[row].date, tripList[row].time, tripList[row].price, tripList[row].free_places, tripList[row].busNumber, tripList[row].stationNumber))
		with cur:
			cur.executemany(sql, data)
		data = []
	for el in data:
		print(el)
	


def databaseTest():
	con = db.connect('my.db')
	with con:
		con.execute("""
			CREATE TABLE USER (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				name TEXT,
				age INTEGER
			);
		""")

	sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
	data = [
		(1, 'Alice', 21),
		(2, 'Bob', 22),
		(3, 'Chris', 23)
	]
	with con:
		con.executemany(sql, data)

	with con:
		content = con.execute("SELECT * FROM USER WHERE age <= 22")
		for row in content:
			print(row)


if __name__ == "__main__":
	tripList = [
		Trip('01', 'Москва', 'Нижний Новгород', '2023-06-01', '09:45', '2000', '11111001011000010100', '10', '2'),
		Trip('02', 'Санкт-Петербург', 'Москва', '2023-06-01', '09:45', '3000', '00001100000000111101', '14', '3'),
		Trip('03', 'Москва', 'Санкт-Петербург', '2023-06-01', '14:00', '3000', '11111001011000010100', '11', '1'),
		Trip('04', 'Нижний Новгород', 'Москва', '2023-06-01', '17:30', '2000', '00001100000000111101', '12', '2'),
		Trip('05', 'Санкт-Петербург', 'Москва', '2023-06-02', '09:45', '3000', '00001100000000111101', '14', '1'),
		Trip('06', 'Москва', 'Нижний Новгород', '2023-06-02', '14:00', '2000', '11111001011000010100', '10', '3'),
		Trip('07', 'Нижний Новгород', 'Санкт-Петербург', '2023-06-02', '14:00', '4000', '00001100000000111101', '13', '2'),
		Trip('08', 'Санкт-Петербург', 'Нижний Новгород', '2023-06-03', '09:45', '4000', '11111001011000010100', '15', '1'),
		Trip('09', 'Санкт-Петербург', 'Москва', '2023-06-03', '09:45', '3000', '00001100000000111101', '14', '3'),
		Trip('10', 'Москва', 'Нижний Новгород', '2023-06-03', '17:30', '2000', '11111001011000010100', '10', '3'),
		Trip('11', 'Нижний Новгород', 'Москва', '2023-06-03', '17:30', '2000', '00001100000000111101', '12', '2'),
		Trip('12', 'Москва', 'Нижний Новгород', '2023-06-04', '14:00', '2000', '11111001011000010100', '10', '2'),
		Trip('13', 'Санкт-Петербург', 'Москва', '2023-06-04', '17:30', '3000', '00001100000000111101', '14', '1'),
		Trip('14', 'Москва', 'Нижний Новгород', '2023-06-05', '09:45', '2000', '11111001011000010100', '10', '3'),
		Trip('15', 'Санкт-Петербург', 'Нижний Новгород', '2023-06-05', '09:45', '4000', '00001100000000111101', '15', '1'),
		Trip('16', 'Нижний Новгород', 'Москва', '2023-06-05', '17:30', '2000', '11111001011000010100', '12', '1'),
		Trip('17', 'Санкт-Петербург', 'Москва', '2023-06-06', '09:45', '3000', '00001100000000111101', '14', '1'),
		Trip('18', 'Москва', 'Нижний Новгород', '2023-06-06', '17:30', '2000', '11111001011000010100', '10', '2'),
		Trip('19', 'Нижний Новгород', 'Москва', '2023-06-06', '17:30', '2000', '00001100000000111101', '12', '3'),
		Trip('20', 'Москва', 'Нижний Новгород', '2023-06-07', '14:00', '2000', '11111001011000010100', '10', '2'),
		Trip('21', 'Санкт-Петербург', 'Москва', '2023-06-07', '14:00', '3000', '00001100000000111101', '14', '3'),
		Trip('22', 'Нижний Новгород', 'Санкт-Петербург', '2023-06-07', '17:30', '4000', '11111001011000010100', '13', '1'),
		Trip('23', 'Москва', 'Санкт-Петербург', '2023-06-07', '17:30', '3000', '00001100000000111101', '11', '2'),
		Trip('24', 'Нижний Новгород', 'Санкт-Петербург', '2023-06-08', '09:45', '4000', '11111001011000010100', '13', '2'),
		Trip('25', 'Москва', 'Санкт-Петербург', '2023-06-08', '09:45', '3000', '00001100000000111101', '11', '3'),
		Trip('26', 'Москва', 'Нижний Новгород', '2023-06-08', '17:30', '2000', '11111001011000010100', '10', '1'),
		Trip('27', 'Санкт-Петербург', 'Москва', '2023-06-09', '09:45', '3000', '00001100000000111101', '14', '1'),
		Trip('28', 'Москва', 'Нижний Новгород', '2023-06-09', '14:00', '2000', '11111001011000010100', '10', '2'),
		Trip('29', 'Нижний Новгород', 'Москва', '2023-06-09', '14:00', '2000', '00001100000000111101', '12', '1'),
		Trip('30', 'Москва', 'Санкт-Петербург', '2023-06-09', '17:30', '3000', '11111001011000010100', '11', '3'),
	]
	tripCreate()
	# print('OK')
	tripAppend(tripList)
	# print('OK')
	#data = tripGetAll()
	#for el in data:
	#	print(el.id, el.price, el.cityFrom, el.cityTo)
