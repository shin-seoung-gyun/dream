class Person :
    def __init__(self, name, age, gender):
        self.name=name
        self.age = age
        self.gender=gender
    def introduce(self):
        print("제 이름은", self.name,"입니다.")
        print("제 나이는", self.age,"입니다.")

class Employee(Person):
    def __init__(self, name, age, gender, salary, id) :
        super().__init__(name, age, gender)
        self.salary = salary
        self.id=id

    def do_work(self):
        print("일하고 있는 중 입니다.")

    def introduce(self):
        super().introduce()
        print("제 급여는",self.salary,"입니다.")

##파이선2까지 사용했던 방식
    # def __cmp__(self,other):
    #     if self.id==other.id :
    #         return 0
    #     elif self.id < other.id :
    #         return -1
    #     else :
    #         return 1


##파이썬 3부터 사용한 방식
##항등연산자에 대한 정의
    def __eq__(self,other):
        return self.id == other.id
##부등호 연산자에 대한 정의
    def __ne__(self,other):
        return self.id != other.id

##보다 큼 연산자에 대한 정의
    def __gt__(self,other):
        return self.id > other.id

##보다 작음 연산자에 대한 정의
    def __lt__(self,other):
        return self.id < other.id

##보다 크거나 같음 연산자에 대한 정의
    def __ge__(self,other):
        return self.id >= other.id

##보다 작거나 같음 연산자에 대한 정의
    def __le__(self,other):
        return self.id <= other.id

##해시코드에 대한 정의
    def __hash__(self):
        return hash(self.id)

#len함수 정의
    def __len__(self):
        return len(self.name)

##str함수정의
    def __str__(self):
        return f"이름 : {self.name}, id : {self.id}"

##repr
    def __repr__(self):
         return f"[이름 : {self.name}, id : {self.id}]"