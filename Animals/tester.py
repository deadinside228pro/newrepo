import unittest
from jiraf import *
from hare import *
from wolf import *
from zoo import *


class Test_Animal_Volier_Zoo(unittest.TestCase):
    def setUp(self):
        self._albert1 = Jiraf('Albert1', 10, 4, 15)
        self._albert2 = Jiraf('Albert2', 7, 5, 12)
        self._albert3 = Jiraf("Albert3", 6, 2, 13)
        self._albertMega = Jiraf('Albert3', 15, 27, 555)
        self._robert1 = Wolf('Robert1', 5, 6, 12)
        self._robert2 = Wolf('Robert2', 4, 5, 11)
        self._Hare_mega1 = Hare('mega1', 2, 5, 1)

        self._volier1 = Volier('вольер для жирафов', 'Савана', 35)
        self._volier3 = Volier('вольер для жирафов', 'Савана', 45)
        self._volier2 = Volier('вольер для волков', 'леса умеренных широт, тайга, тундра, степи и горные системы', 35)
        self._zoo1 = Zoo('Зоопарк', [self._volier1])

        self._volier1.AddAnimal(self._albert1)
        self._zoo1.addVolier(self._volier3)

        self._albert1.eat('морковка')
        self._albert1.eat('морковка')
        self._albert1.eat('морковка')
        self._albert1.eat('морковка')

        self._albert2.eat('qqq')

    def test_add_animal_in_volier_1(self):
        expected = True
        actual = self._volier3.AddAnimal(self._albert2)
        self.assertEqual(expected, actual, 'ok1')  # проверка на добовление животного в пустой вальер

    def test_add_animal_in_volier_2(self):
        expected = "there is can not be two similar animals"
        actual = self._volier1.AddAnimal(self._albert1)
        self.assertEqual(expected, actual, 'ok2')  # проверка на добовление одного и того же животного в один вольер

    def test_add_animal_in_volier_3(self):
        expected = 'он здесь не уживётся'
        actual = self._volier1.AddAnimal(self._Hare_mega1)
        self.assertEqual(expected, actual, 'ok3')  # проверка на добовление животного в вольер с другим биомом

    def test_add_animal_in_volier_4(self):
        expected = False
        actual = self._volier1.AddAnimal(self._albertMega)
        self.assertEqual(expected, actual, 'ok4')  # проверка на добовление животного, в вольер,  где не хватает места

    def test_add_animal_in_volier_5(self):
        self._volier2.AddAnimal(self._robert1)
        expected = True
        actual = self._volier2.AddAnimal(self._robert2)
        self.assertEqual(expected, actual, 'ok5')  # проверка на добовление хищника

    def test_add_animal_in_volier_6(self):
        expected = True
        actual = self._volier1.AddAnimal(self._albert2)
        self.assertEqual(expected, actual, 'ok6')  # проверка на добовление травоядного

    def test_kill_animal_in_volier_1(self):
        expected = None, 35
        actual = self._volier1.KillAnimal(self._albert1), self._volier1.sizeOfVolier
        self.assertEqual(expected, actual,
                         'ok1')  # проверка на убирание животного из вольера(проверка освобождения места
        # после отселения животного)

    def test_kill_animal_in_volier_2(self):
        expected = False
        actual = self._volier1.KillAnimal(self._albert2)
        self.assertEqual(expected, actual, 'ok')  # проверка на убирание животного, которого нет в вольере

    def test_eat_food_animals_in_volier(self):
        expected = False
        actual = self._volier1.EatFood('qqq')
        self.assertEqual(expected, actual, 'ok')  # проверка на передачу в метод не того типа, который нужен

    def test_eat_food_animals_in_volier2(self):
        expected = 'кормушка пуста'
        actual = self._volier1.EatFood([])
        self.assertEqual(expected, actual,
                         'ok')  # проверка на оперделение количества еды в кормушке(кормушка изначально пуста)

    def test_eat_food_animals_in_volier3(self):
        expected = None
        actual = self._volier1.EatFood(['морковка', 'qqq'])
        self.assertEqual(expected, actual, 'ok')  # проверка на кушанье животными еды из их рациона

    def test_eat_food_animals_in_volier4(self):
        self._volier1.AddAnimal(self._albert2)
        expected = None
        actual = self._volier1.EatFood(['морковка'])
        self.assertEqual(expected, actual, 'ok')

    def test_food_in_manger_in_volier_1(self):
        expected = 'тут пусто'
        actual = self._volier1.foodInManger
        self.assertEqual(expected, actual, 'ok')  # проверка на количество еды в курмушке в вольере

    def test_food_in_manger_in_volier_2(self):
        self._volier1.EatFood(['морковка'])
        expected = ['морковка']
        actual = self._volier1.foodInManger
        self.assertEqual(expected, actual, 'ok')  # проверка на показ еды в кормушке в вольере

    def test_need_food_animal_in_volier(self):
        expected1 = True
        actual1 = self._volier1.needFoodAnimal
        self.assertEqual(expected1, actual1, 'ok1')  # проверка на сытость всех животных в вольере
        self._volier2.AddAnimal(self._robert1)
        expected2 = False
        actual2 = self._volier2.needFoodAnimal
        self.assertEqual(expected2, actual2, 'ok2')  # проверка на голодность животных в вольере

    def test_add_food_in_manger(self):
        expected1 = False
        actual1 = self._volier1._addFoodInManger('qqq')
        self.assertEqual(expected1, actual1, 'ok1')  # проверка на передачу не того типа, который нужен
        expected2 = ['морковка']
        actual2 = self._volier1._addFoodInManger(['морковка'])
        self.assertEqual(expected2, actual2, 'ok2')  # проверка на добавление в кормушку еды

    def test_add_voliers_in_zoo(self):
        expected1 = True
        actual1 = self._zoo1.addVolier(self._volier2)
        self.assertEqual(expected1, actual1, 'ok1')  # проверка на правильное добавление вольера в зоопарк
        expected2 = False
        actual2 = self._zoo1.addVolier(self._volier1)
        self.assertEqual(expected2, actual2,
                         'ok2')  # проверка на неправильно добавление вольера(передан уже имеющийся вольер)
        expected3 = False
        actual3 = self._zoo1.addVolier(self._zoo1)
        self.assertEqual(expected3, actual3, 'ok3')  # проверка на неправильное добавление вольера(передан не вольер)

    def test_delete_volier_in_zoo(self):
        expected1 = False
        actual1 = self._zoo1.deleteVolier(self._volier2)
        self.assertEqual(expected1, actual1,
                         'ok1')  # проверка на неправильное удаление(удаляется несуществующий вольер)
        expected2 = False
        actual2 = self._zoo1.deleteVolier(self._volier1)
        self.assertEqual(expected2, actual2, 'ok2')  # проверка на неправильное удаление(удаляется вольер с животными)
        expected3 = None
        self._zoo1.addVolier(self._volier2)
        actual3 = self._zoo1.deleteVolier(self._volier2)
        self.assertEqual(expected3, actual3, 'ok3')  # проверка на праивльное удаление вольера

    def test_add_animal_in_volier_in_zoo(self):
        expected1 = False
        actual1 = self._zoo1.addAnimalInvolier(self._albert2, self._volier2)
        self.assertEqual(expected1, actual1, 'ok1')  # проверка на неправильное добваление(добавление животного
        # в несуществующий в этом зоопарке вольер)
        expected2 = True
        actual2 = self._zoo1.addAnimalInvolier(self._albert2, self._volier1)
        self.assertEqual(expected2, actual2, 'ok2')  # проверка на правильное добавление 1 животного
        expected3 = True
        actual3 = self._zoo1.addAnimalInvolier([self._albert2, self._albert3], self._volier1)
        self.assertEqual(expected3, actual3, 'ok3')  # проверка на правильное добавление нескольких животных

    def test_remove_animal_in_voliers_in_zoo(self):
        expected1 = False
        actual1 = self._zoo1.removeAnimal(self._volier1, self._albert2, self._volier3)
        self.assertEqual(expected1, actual1,
                         'ok1')  # проверка на неправльное перемещение(попытка переместить несуществующее
        # в этом зоопарке животное)
        expected2 = False
        actual2 = self._zoo1.removeAnimal(self._volier1, self._albert1, self._volier2)
        self.assertEqual(expected2, actual2, 'ok2')  # проверка на неправльное перемещение(попытка переместить животное
        # в несуществующий вольер)
        expected3 = True
        actual3 = self._zoo1.removeAnimal(self._volier1, self._albert1, self._volier3)
        self.assertEqual(expected3, actual3, 'ok3')  # проверка на правльное перемещение

    def test_add_food_in_voliers(self):
        expected1 = False
        actual1 = self._zoo1.addFoodInvoliers(self._volier1, 'qqq')
        self.assertEqual(expected1, actual1,
                         'ok1')  # проверка на неправльное добавление еды в вольеры(неправильный тип переменных)
        expected2 = False
        actual2 = self._zoo1.addFoodInvoliers([self._volier1], 'qqq')
        self.assertEqual(expected2, actual2,
                         'ok2')  # проверка на неправльное добавление еды в вольеры(неправильный тип переменных)
        expected3 = True
        actual3 = self._zoo1.addFoodInvoliers([self._volier1], ['морковка'])
        self.assertEqual(expected3, actual3, 'ok3')  # проверка на правльное добавление еды в вольеры

    def test_init_animal(self):
        expected = ['Albert1', 10, 4, 15]
        actual = [self._albert1.name, self._albert1.age, self._albert1.needdedFood, self._albert1.size]
        self.assertEqual(expected, actual, 'Ok')  # проверка инита

    def test_type_of_food_animal(self):
        expected = ['листья', 'груша', 'морковка']
        actual = self._albert1.typeFood
        self.assertEqual(expected, actual, "Ok")

    def test_if_feeded(self):
        expected = True
        actual = self._albert1.isFedded
        self.assertEqual(expected, actual, 'ok')

    def test_eat_animal_3(self):
        expected = 'я больше не буду'
        actual = self._albert1.eat('морковка')
        self.assertEqual(expected, actual, "ok")  # попытка накормить уже сытое животное

    def test_eat_animal_2(self):
        expected = 'я такое не ем'
        actual = self._albert2.eat('qqq')
        self.assertEqual(expected, actual,
                         'неправильно передан тип, либо он уже наелся, либо передана еда которую он не ест')

    def test_animal_1(self):
        expected = True
        actual = self._albert2.eat('морковка')
        self.assertEqual(expected, actual, 'ok')  # проверка на правильное кормление

    def test_size_setter(self):
        expected = 11
        actual = self._albert1.size = 11
        self.assertEqual(expected, actual, 'ok')

    def test_how_many_food_need(self):
        expected = 4
        actual = self._albert1.needdedFood
        self.assertEqual(expected, actual, 'ok')

    def test_name_setter(self):
        expected = 'qqq'
        actual = self._albert1.name = 'qqq'
        self.assertEqual(expected, actual, 'ok')

    def test_age_setter(self):
        expected = 13
        actual = self._albert1.age = 13
        self.assertEqual(expected, actual, 'ok')


if __name__ == "__mane__":
    unittest.main()
