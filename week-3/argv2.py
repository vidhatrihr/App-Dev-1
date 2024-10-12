import sys
print(sys.argv)

name = sys.argv[1]
place = sys.argv[2]
weather = sys.argv[3]
print(f'I am {name}, I live in {place}. Today is a {weather} day.')
