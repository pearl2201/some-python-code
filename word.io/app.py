from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit, send

import socketio
import time
from threading import Thread
import sqlite3
import os
import codecs
import random
class NetworkManager(Thread):
    gameManager = None
    app = Flask(__name__)
    socketio = SocketIO(app)
    roomwc = 'wordconnect'
    def __init__(self, _gameManager):
        Thread.__init__(self)
        
        gameManager = _gameManager
        

    def run(self):
        self.socketio.run(self.app,None,4568)

    @socketio.on('beep')
    def handle_my_custom_event():
        
        pass
    
    @socketio.on('join')
    def join(message):
        socketio.enter_room(sid,roomwc )
    
    @socketio.on('login')
    def handle_login_event(message):
        gameManager.databaseManager.loginUser(message[iduser])
    
    @socketio.on('answer')
    def handle_answer_event(message)):

    def sendMessage(message)):
        self.socketio.emit(event, data)

class GameManager(Thread):
   
    def __init__(self):
        Thread.__init__(self)
        self.databaseManager = DatabaseManager();
        self.wordManager = WordManager()
        self.currQuestion = ""
        
        self.currIdQuestion = 0
        
    def run(self):
        try:
            while (True):
                self.currQuestion = self.wordManager.GetWord()
                question = self.ArrangeQuestion(self.currQuestion)
                self.currIdQuestion = self.currIdQuestion + 1;
                self.networkManager.sendMessage('question',{"question":question, "idQuestion":self.currIdQuestion})
                
                time.sleep(1)
        except SystemExit, e:
            self.databaseManager.closeDatabase()
       
        pass

    def regisNetWorkManager(self,_networkManager):
        self.networkManager = _networkManager

    def ArrangeQuestion(self,question):
        listChar = list(question)
        newQuestion = ""
        rd = random.Random()
        while (len(listChar)>0):
            r = rd.randint(0, len(listChar)-1)
            w = listChar[r]
            
            newQuestion = newQuestion + w
            listChar.remove(w)
        
        return newQuestion

class WordManager:
    def __init__(self):
        fn = os.path.join(os.path.dirname(__file__), 'data/dict.txt')
        dictTxt = codecs.open(fn, 'r',"utf-8")
        self.listWord = list([])
        self.listIndexRemain = []
        i =0
        for line in dictTxt:
               self.listWord.append(line.strip())
               self.listIndexRemain.append(i)
               i = i+1
        
    def GetWord(self):
        if (len(self.listIndexRemain)<10):
            self.listIndexRemain.clear()
            i =0
            for line in self.listWord:
                self.listIndexRemain.append(i)
                i = i+1
        rd = random.Random()
        r = rd.randrange(0, len(self.listIndexRemain))
        id = self.listIndexRemain[r]
        self.listIndexRemain.remove(id)
        return self.listWord[id]
               


class DatabaseManager:


    def __init__(self, gameManager):
        
        self.conn = sqlite3.connect('user.db')
        self.c = conn.cursor
        self.gameManager = gameManager

   
    def loginUser(self, idUser):
        for row in c.execute("SELECT idUser FROM scores WHERE idUser = (?)",(idUser)):
            break
        else:
            c.execute('INSERT INTO score(iduser,score) VALUES (?,?)', (idUser,0))
        pass

    def getRankUser((self,idUser)):
        rank = -1
        for row in c.execute("select  p1.*, (select  count(*) from scores as p2   where   p2.score > p1.score ) as rank from scores as p1 where iduser = (?)",(idUser)):
            rank = row[3]
            break
        return rank

    def getLeaderBoard(self):
        
        for row in c.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 50"):
            name, age = row
            break
        else:
            print("not found")
            
        pass

    def getListRank(self, idUser):
        for row in c.execute("SELECT MAX(score) FROM scores LIMIT 5 WHERE idUser = (?)", (idUser)):
            name, age = row
            break
        else:
            print("not found")
            
        pass
    
    def updateScore(self,idUser, currScore):
        cursor.execute("UPDATE scores SET score WHERE idUser= ? ",(currScore,idUser))
        pass

    def closeDatabase(self):
        self.conn.commit()
        self.conn.close()

class User:

    def __init__(self,id, idUser, score ):
        self.id = id
        self.idUser = idUser
        self.score = score
 
if __name__ == '__main__':
  
    gameManager = GameManager()
    networkManager = NetworkManager(gameManager)
    gameManager.regisNetWorkManager(networkManager)
    gameManager.start()
    networkManager.start()
    
