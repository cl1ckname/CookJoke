from random import choice, seed
seed(1)

PROFESSIONS = ['повар', 'милиционер', 'пожарник', "строитель", "бухгалтер"]
def getRandomProfession():
	return choice(PROFESSIONS)


class Question:
	def __init__(self, p1: 'Povar', p2: 'Povar'):
		print(f'{p1} спрашивает {p2}а:'.capitalize())

	def whatIsProfession(self, maybe: str):
		print(f'{p2}, какова твоя профессия?'.capitalize(), f'Ты {maybe}?')
		return Reply(p2, maybe == p2.getProfession())

class Reply:
	message: str
	sender: 'Povar'
	def __init__(self, sender: 'Povar', correct: bool):
		self.sender = sender
		if not correct:
			self.message = f'Нет! Отвечает {sender}.'
		else:
			self.message = f'Да, отвечает {sender}.'

	def logPovarAnswer(self):
		print(self.message)
		return self.sender

class Povar:
	def __init__(self, name: str, profession: str):
		self.name = name
		self.profession = profession

	def ask(self, povar: 'Povar'):
		return Question(self, povar)

	def getProfession(self):
		return self.profession

	def logMainProfession(self):
		print(f'Моя главная профессия - {self.getProfession()}')

	def __str__(self):
		return self.name


if __name__ == '__main__':
	p1 = Povar('повар', 'повар')
	p2 = Povar('повар', 'повар')
	p1.ask(p2).whatIsProfession(maybe=getRandomProfession()).logPovarAnswer().logMainProfession()