
# Задание №3

my_file1 = open('text_1.txt', 'r')
content1 = my_file1.readlines()
print(f'Количество строк в файле1 - {len(content1)}')


my_file2 = open('text_2.txt','r')
content2 = my_file2.readlines(  )
print(f'Количество строк в файле2 - {len(content2)}')


my_file3 = open('text_3.txt','r')
content3 = my_file3.readlines(  )
print(f'Количество строк в файле3 - {len(content3)}')


my_file1.close()
my_file2.close()
my_file3.close()

# f = open('text_4.txt')

in_file = open('text_2.txt', 'r',)
indata = in_file.read()
out_file = open('text_4.txt', 'w', encoding='UTF-8')
out_file.write(indata + '\n')
out_file.close()
in_file.close()


in_file = open('text_1.txt', 'r',)
indata = in_file.read()
out_file = open('text_4.txt', 'a', encoding='UTF-8')
out_file.write(indata + '\n')
out_file.close()
in_file.close()


in_file = open('text_3.txt', 'r',)
indata = in_file.read()
out_file = open('text_4.txt', 'a', encoding='UTF-8')
out_file.write(indata + '\n')
out_file.close()
in_file.close()

print()

in_file = open('text_4.txt', 'r')
indata = in_file.read()
print(indata)
in_file.close()

# Второе условие к заданию не смог понять как сделать, Через какую функцию....