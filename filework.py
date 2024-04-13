myfile = open('justtext.txt')

for line in myfile:
  line = line.rstrip()
  print(line)