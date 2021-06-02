class Note :##페이지 하나 글을 쓰는 용도
    def __init__(self, contents=None):
        self.contents=contents
    
    def writeContents(self,contents):
        self.contents=contents

    def removeAll(self):
        self.contents=""
    
    def __str__(self):
        return self.contents

class NoteBook :
    def __init__(self,title) :
        self.title=title
        self.pageNumber = 1
        self.notes = {}

    def addNote(self,note,page=0):
        if self.pageNumber <300:
            self.notes[self.pageNumber]=note
            self.pageNumber+=1
        else :
            print("페이지가 모두 채워졌습니다.")

    def removeNote(self,pageNumber):
        if pageNumber in self.notes.keys():
            return self.notes.pop(pageNumber)
        else:
            print("해당페이지는 존재하지 않습니다.")

    def getPageSize(self):
       return len(self.notes.keys())

    def getNote(self, pageNumber):
        return self.notes[pageNumber]