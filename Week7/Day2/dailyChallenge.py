matrix = [
    ['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', '',  '#'],
    ['s', 'M', ''],
    ['$', 'a', ''],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]

decrypted_list = []
def search_str_matrix(matrix):
    for i in range(3):
        for item in matrix:
            if item[i].isalpha():
                decrypted_list.append(item[i])
                print(decrypted_list)
                if item[i+1].isalpha():
                    decrypted_list.append(" ")
print(decrypted_list)

search_str_matrix(matrix)