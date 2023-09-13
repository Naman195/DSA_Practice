f = open('data.txt', 'r')
# print(f)
no_of_lines = 0
no_of_chars = 0
no_of_words = 0

for line in f:
    no_of_lines += 1
    line = line.strip('\n')
    no_of_chars += len(line)
    list1 = line.split()
    no_of_words += len(list1)
f.close()
print("no of Lines", no_of_lines)
print("no of chars", no_of_chars)
print("no of Lines", no_of_words)