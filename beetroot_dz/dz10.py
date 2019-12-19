class Human():
    def __init__(self,name,lastname,age):
        if type(name) is not str:
            print('Parametr name must be string')
            return
        if type(lastname) is not str:
            print('Parametr name must be string')
            return
        if type(age) is not int:
            print('Parametr name must be string')
            return
        self.name=name
        self.lastname=lastname
        self.age=age
        self.info=[self.name,self.lastname,self.age]
    def talk(self):
        print('Hello my name is {} {} my age is {}'.format(*self.info))


human1=Human('Vitaliy','Ivanoff',22)
human1.talk()

