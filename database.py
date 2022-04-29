import sqlite3
from datetime import datetime
import socket

class databaseLogger:
    def __init__(self) -> None:
        self.con = sqlite3.connect('wordle.db')
        self.cur = self.con.cursor()
        self.ip = self.getIp()
        self.currentGameId = None

    def createTable(self):
        self.cur.execute('''CREATE TABLE game (id integer primary key autoincrement, date text, localIp text)''')
        self.cur.execute('''CREATE TABLE attemptTable
               (id integer primary key autoincrement, attempt text, userWord text, gameWord text, success bool,  gameId integer, FOREIGN KEY(gameId) REFERENCES game(id))''')
        self.cur.execute('''CREATE Table statistics(id integer primary key autoincrement, gamesPlayed integer, game1Distribution integer,  game2Distribution integer, game3Distribution integer, game4Distribution integer, game5Distribution integer, game6Distribution integer, winPercentage integer, gameId integer, FOREIGN KEY(gameId) REFERENCES game(id))''')
       
    
    def getIp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0)
        try:
            # doesn't even have to be reachable
            sock.connect(('10.255.255.255', 1))
            ip = sock.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            sock.close()
        return ip

    def writeGame(self, time):
        self.cur.execute("insert into game values (NULL, ?, ?)", (time, self.ip))

    def getId(self, time):
        self.cur.execute("select * from game where date= :time", {"time": time})
        data = self.cur.fetchall()
        x = data[0]
        return x[0]

    def writeAttemptTable(self, attempt, userWord, gameWord, success):
        self.cur.execute("insert into attemptTable values (NULL, ?, ?, ?, ?, ?)",(attempt, userWord, gameWord, success, self.currentGameId))


    def writeGameStatistis(self, gamesPlayed, game1Distribution, game2Distribution, game3Distribution, game4Distribution, game5Distribution, game6Distribution, winPercentage):
        self.cur.execute("insert into statistics values (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (gamesPlayed, game1Distribution, game2Distribution, game3Distribution, game4Distribution, game5Distribution, game6Distribution, winPercentage, self.currentGameId))

    def generateReport(self, startDate, endDate):
        try:
            file1 = open('databaseReport.txt', 'w')
            file1.write("Game Statistics\n")
            file1.write(f"start date: {startDate}\n")
            file1.write(f"end date: {endDate}\n")

            self.cursor.execute("select * from statistics inner join game on game.id = statistics.gameId where game.date>= :startDate and date<= :endDate",{"startDate":startDate,"endDate":endDate})
            data = self.cursor.fetchall()
            for row in data:
                file1.write("Number of games played = {} \n".format(row.totalGamePlayedCount))
                file1.write("Win Percentage = {}% \n".format(row.winPercentage))
                for i in range(1, 6):
                    file1.write("Game distribution for {} = {}\n".format(i, row.game1Distribution))
            # file1.write(f'Total number of games played: {len(data)}\n')
            # file1.write(f'Total number of games played: {len(data)}\n')
        except FileNotFoundError as e:
            print(f"Cannot open file ({e})")
            



