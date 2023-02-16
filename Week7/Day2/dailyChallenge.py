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
        x = 0
        for j in range(len(matrix)-1):
            print(matrix[j][i])
            if matrix[j][i].isalpha() and matrix[len(matrix)-1][i].isalpha():
                decrypted_list.append(" ")
        for item in matrix:
            if item[i].isalpha():
                decrypted_list.append(item[i])
                print(decrypted_list)

print(decrypted_list)

search_str_matrix(matrix)