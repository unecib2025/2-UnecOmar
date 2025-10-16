#labaratorniy 2


#2.1
# a = input('vedi parol:')
# b = len (a)
# if b >= 8:
#     print('parol prinat')
# if b < 8 :
#     print('slishkom korotkiy paol')


#2.2
# status = input()
# if status == 'online'
#     print('svaz ustanovlen')
# if status == 'ofline'
#     print('svaz poteran')
# else :
#     print('error')


#2.3
# a =int(input('vedi chislo:'))
# if a >=1 and a <= 30:
#     print(' nizkiy uroven uqrozi')
# elif a >= 31 and a<= 70:
#     print('sredniy uroven uqrozi')
# elif a >= 71 and a <=100:
#     print('kriticheskiy uroven uqrozi')
# else:
#     print('error')



#2.4 
# checksum_original = input("Введите оригинальную контрольную сумму: ")
# checksum_current = input("Введите текущую контрольную сумму: ")
# status = "Файл не изменён" if checksum_original == checksum_current else "Файл повреждён"
# print(status)  # вывод результата
# 
# print()

# 2.5
# event_code = input("Введите код события (ERR, WRN, INF): ")
# 
# match event_code:
#     case "ERR":
#         print("Ошибка системы")  # если код ERR
#     case "WRN":
#         print("Предупреждение")  # если код WRN
#     case "INF":
#         print("Информационное сообщение")  # если код INF
#     case _:
#         print("Неизвестный код события")  # если другой код