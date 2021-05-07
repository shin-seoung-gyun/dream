from person import Person,Employee

p1 = Person("홍길동",30,"남자")
p2 = Person("김하나",25,"여자")

p1.introduce()
p2.introduce()

e1 = Employee("임꺽정",35,"남자",5000,3)
e2 = Employee("임해성",33,"남자",5000,3)
e3 = Employee("김동해",25,"여자",5000,10)
print(e1==e2)
print(e1==e3)
print(e1 > e2)
print(e1 < e3)
print(len(e1))



employSet = set()
employSet.add(e1)
employSet.add(e2)
employSet.add(e3)

print(employSet)

for person in employSet :
    print(person)

personList =[]
personList.append(p1)
personList.append(p2)
personList.append(e1)

for person in personList:
    person.introduce()
    print("--------------")









