import sys


def a(string):
	return 1

def b(string):
	return 2

def c(string):
	return entry(string, l2, 1)

def d(string):
	return 3

def e(string):
	return 4

def f(string):
	return entry(string, l3, 2)

def g(string):
	return 5

def entry(string, l, i):
	try:
		return l[string[i]](string)
	except IndexError:
		print('String incomplete!')
	except KeyError:
		print('Incorrect Value!')


l3 = {
	'G': g
}

l2 = {
	'D': d,
	'E': e,
	'F': f
}

l1 = {
	'A': a,
	'B': b,
	'C': c
}

if __name__ == '__main__':
    string = sys.argv[1]
    print(entry(string, l1, 0))
