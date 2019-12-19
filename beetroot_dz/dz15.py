class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.mail=''

    @property
    def email(self):
        try:
            return self.mail
        except:
            return None
        '''
        if hasattr(self,'email'):
            return self.email
        else:
            return None
        '''
    @property
    def full_name(self):
        return self.first_name+' '+self.last_name
    @full_name.setter
    def full_name(self,full_name):
        try:
            firts_name,last_name=full_name.split()
            self.first_name = firts_name
            self.last_name = last_name
        except Exception:
            print('Must be string with space')



    @email.setter
    def email(self,domain):

        if '.' not in domain:
            print('Dot must be in domain')
            return
        if len(domain.split('.'))!=2:
            print('Only first level domain allowed')

        email=self.first_name+'.'+self.last_name+'@'+domain

        self.mail=email
    @property
    def age(self):
        try:
            return self.person_age
        except Exception:
            return None
    @age.setter
    def age(self,age):
        self.person_age=age



person=Person('John','Walker')
print(person.first_name)
print(person.email)
person.email='ukr.net'
print(person.email)
person.full_name='Next Space'
print(person.first_name)
print('--------Age-------')
print(person.age)
person.age=21
print(person.age)