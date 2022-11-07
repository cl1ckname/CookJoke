from CookJoke import Cook, getRandomProfession
from CookJoke.laugh import getLaughString

if __name__ == '__main__':
	p1 = Cook('повар', 'повар')
	p2 = Cook('повар', 'повар')
	p1.ask(p2).whatIsProfession(maybe=getRandomProfession()).logCookAnswer().logMainProfession()
	print(getLaughString(10))