# 1. Дано натуральне число N. Виведіть слово YES, якщо число N є точним ступенем двійки,
# або слово NO інакше. 8 - YES, 3 - NO

def natural_number_N(numb):
    if (numb & (numb-1) == 0) and numb != 0:
        return 'Yes'
    else:
        return 'NO'
