
class SoccerPlayer :
    def __init__(self,name,position,backNumber):
        self.name = name
        self.position = position
        self.backNumber = backNumber

    def changeBackBumber(self,backNumber):
        print(f"선수의 등번호 변경 : From{self.backNumber} to {backNumber}")
        self.backNumber = backNumber

    def __str__(self):
        return f"name:{self.name}, Position:{self.position}, BackNumber:{self.backNumber}"

player1 = SoccerPlayer("김현수","수비수",10)
player1.changeBackBumber(13)
print(player1)

names = ["홍길동","임꺽정","추신수","안정환"]
positions = ["MF","DF","CF","WF","GK"]
numbers =[10,4,7,13,1]
playerObjects = [SoccerPlayer(name, position, backNumber) for name, position, backNumber in zip(names,positions,numbers)]
print(playerObjects[-1])


for player in playerObjects:
    print(player)



from noteBook import Note
from noteBook import NoteBook
sentence1 = "삶이 있는 한 희망은 있다. - 키게로"
note1 = Note(sentence1)
sentence2 = "하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌수 있다."
note2 = Note(sentence2)

print(note1)
print(note2)


note1.removeAll()
print(note1)

sayingsNotebook = NoteBook("명언노트")
sayingsNotebook.addNote(note1)
sayingsNotebook.addNote(note2)
sayingsNotebook.addNote(Note("행복의 문이 하나 닫히면 다른 문이 열린다-헬런 켈러"))

print(sayingsNotebook.getPageSize())
print(sayingsNotebook.getNote(1))

sayingsNotebook.removeNote(100)
sayingsNotebook.removeNote(1)
print(sayingsNotebook.getNote(1))








