import os, re


directory = os.listdir('D:/git/www git (2)')
os.chdir('D:/git/www git (2)')

for file in directory:
	open_file = open(file, 'r')
	read_file = open_file.read()
	regex = re.compile('ĂŁžĆžß ÇŇ łťżë') //바꿀단어
	read_file = regex.sub('šŮ˛Ü łťżë', read_file)//
	write_file = open(file, 'w')
	write_file.write(read_file)
