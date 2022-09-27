class company_Volkswagen:
    def __init__(self, name):                     #Атрибуты
     self.name = name

    def has(self):                                #Методы
        return 'I have many companies'
    def get_name(self):                           #Вывод конкретных методов
        return f'The best company is {self.name}'

Volkswagen = company_Volkswagen('Volkswagen')
print(Volkswagen.name)
print(Volkswagen.has())
print(Volkswagen.get_name())                      #Получение конкретных значений
class company_Porsche(company_Volkswagen):        #Наследование
    # pass
    def __init__(self, name, model):              #Атрибуты
        super().__init__(name)
        self.model = model                        #Методы
    def have(self):
        return 'I have the best cars'
    # def set_model(self, mew_model):             #Изменение и вызов метода
    #     self.model = new_model
Porsche = company_Porsche('Porsche', '912_turbo')
# Porsche.model = '912_GT3'                       #Изменение и вызов метода
# print(Porsche.name, Porsche.model)              #Изменение и вызов метода
print(Porsche.have())
print(Porsche.model)

