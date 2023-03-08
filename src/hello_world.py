def get_name():
	return input("What's your name?\n")

def display_name(name):
	print(f"Hello {name}")



if __name__ == '__main__':
	name = get_name()
	display_name(name)
