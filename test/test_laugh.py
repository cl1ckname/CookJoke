from src.CookJoke.laugh import getLaughString

def test_laugh():
	laugh = getLaughString(10)
	assert len(laugh) > 10