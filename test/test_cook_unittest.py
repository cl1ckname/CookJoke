from unittest import TestCase
from src.CookJoke import Cook, getRandomProfession

class CookTest(TestCase):
	cookProfession = 'profession'
	def test_cookCreationTest(self):
		cook = Cook('name', self.cookProfession)
		assert self.cookProfession == cook.getProfession()
		assert cook.logMainProfession() is None
		assert str(cook) == 'name'

	def test_cook_question(self):
		cook1 = Cook('name', self.cookProfession)
		cook2 = Cook('name', self.cookProfession)
		question = cook1.ask(cook2)
		replyFalse = question.whatIsProfession('maybe')
		assert replyFalse.message == 'Нет! Отвечает name.'
		replyTrue = question.whatIsProfession(self.cookProfession)
		assert replyTrue.message == 'Да, отвечает name.'
		sender = replyTrue.logCookAnswer()
		assert sender is cook2

	def test_random_profession(self):
		assert getRandomProfession() == 'милиционер'

		