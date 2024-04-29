myfile = open('justtext.txt')

for line in myfile:
  line = line.rstrip()
  print(line) 
print('It is okay')