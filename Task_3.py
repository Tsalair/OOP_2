files = ['1.txt', '2.txt', '3.txt']

def count_strings(f):
    count = 0
    while True:
        st = f.readline()        
        if st == '':
            break
        count += 1
    return count

files_len = []
for file in files:
    with open(file, encoding = 'utf-8') as f:
        files_len.append([file, count_strings(f)])

def sort_key(file_len):
    return file_len[1]
files_len.sort(key=sort_key)

with open('final_file.txt', mode='w', encoding = 'utf-8') as f_file:
    for file in files_len:
        with open(file[0], mode='r', encoding = 'utf-8') as f:
                text = f.read()
                f_file.write(file[0])
                f_file.write('\n')
                f_file.write(str(file[1]))
                f_file.write('\n')
                f_file.write(text)
                f_file.write('\n')


