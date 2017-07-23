import os, re


directory = os.listdir('')
os.chdir(' 경로입력')

for file in directory:
	open_file = open(file, 'r')
	read_file = open_file.read()
	regex = re.compile('ĂŁžĆžß ÇŇ łťżë') //바꿀단어
	read_file = regex.sub('šŮ˛Ü łťżë', read_file) //바뀔단어
	write_file = open(file, 'w')
	write_file.write(read_file)
