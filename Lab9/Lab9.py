#####################################################################################################################
################################################## Test data: #######################################################
#####################################################################################################################
# Count: 13
################## 1 победитель (Семенов Егор 11 225):
################## Результат: Васильев Кирилл
#Семенов Егор 11 225
#Васильев Кирилл 7 100
#Шилов Сергей 8 25
#Максимов Евгений 9 22
#Иванов Евгений 10 25
#Шишкин Евгений 9 25
#Леснов Евгений 11 25
#Селезнёв Евгений 9 25
#Петров Евгений 9 25
#Симонов Евгений 7 25
#Шишов Алексей 10 25
#Сизов Евгений 9 25
#Соболев Евгений 8 25
################## Фаворитов больше 20%:
################## Результат: Селезнёв Евгений
#Семенов Егор 11 225
#Васильев Кирилл 7 225
#Шилов Сергей 8 225
#Максимов Евгений 9 225
#Иванов Евгений 10 225
#Шишкин Евгений 9 225
#Леснов Евгений 11 225
#Селезнёв Евгений 9 100
#Петров Евгений 9 25
#Симонов Евгений 7 25
#Шишов Алексей 10 25
#Сизов Евгений 9 25
#Соболев Евгений 8 25
################## Фаворитов больше 20%:
################## Результат: 7
#Семенов Егор 11 225
#Васильев Кирилл 7 225
#Шилов Сергей 8 225
#Максимов Евгений 9 225
#Иванов Евгений 10 225
#Шишкин Евгений 9 225
#Леснов Евгений 11 225
#Селезнёв Евгений 9 100
#Петров Евгений 9 100
#Симонов Евгений 7 100
#Шишов Алексей 10 25
#Сизов Евгений 9 25
#Соболев Евгений 8 25
################## Фаворитов 2 (меньше 20%):
################## Результат: 4
#Семенов Егор 11 225
#Васильев Кирилл 7 225
#Шилов Сергей 8 25
#Максимов Евгений 9 25
#Иванов Евгений 10 25
#Шишкин Евгений 9 25
#Леснов Евгений 11 25
#Селезнёв Евгений 9 100
#Петров Евгений 9 100
#Симонов Евгений 7 100
#Шишов Алексей 10 100
#Сизов Евгений 9 25
#Соболев Евгений 8 25
#####################################################################################################################
##################################################### Data: #########################################################
#####################################################################################################################
class CMember:
    surname = None
    name = None
    points = None

    def __init__(self, surname, name, points):
        self.surname = surname
        self.name = name
        self.points = points
#####################################################################################################################
##################################################### Funcs: ########################################################
#####################################################################################################################
def main():
    members_count = int(input("Количество учащихся: "))
      
    members_list = list()
    members_more200_points_count = 0
    members_top_no_favorite_points = 0
    favorites_is_exist = None
    max_point = 0

    print("Введите имена учеников:")
    member_index = 0
    while member_index < members_count:
        member_index += 1

        input_string = input()
        points = None

        # Обработка данных участника.
        surname, name, member_class, points = input_string.split(" ")
        member_class = int(member_class)
        points = int(points)

        if len(surname) > 20:
            print("Фамилия слишком длинная!")
            print("Повторите попытку ввода.")
            continue

        if len(name) > 15:
            print("Имя слишком длинное!")
            print("Повторите попытку ввода.")
            continue

        if member_class < 7 or member_class > 11:
            print("Не верный класс!")
            print("Повторите попытку ввода.")
            continue
        
        # Инициализация объектов класса учаник.
        member = CMember(surname, name, points)

        # балл больше 200 ?
        if points > 200:
            members_more200_points_count += 1
        elif points > members_top_no_favorite_points:
            members_top_no_favorite_points = points

        # Сравнение суммы балов ученика, с последним наивысшим баллом.
        if max_point < points:
            max_point = points

        # Добавление в общий список учеников.
        members_list.append(member)

    # Высший заработанный бал больше 200?
    if max_point > 200:
        one_percent = members_count / 100
        percent_of_favorites = members_more200_points_count / one_percent

        if percent_of_favorites > 20:
            # Нет победителей, слишком много участников набрало больше 200 баллов!
            favorites_is_exist = False
        else:
            # Есть победители, набрали больше 200 баллов!
            # определять фамилию и имя лучшего участника, не ставшего победителем олимпиады.
            max_point = members_top_no_favorite_points
            favorites_is_exist = True
    else:
        # Нет победителей, никто из участников не набрало больше 200 баллов!
        favorites_is_exist = False
    
    # Поиск всех учеников с наивысшим баллом.
    members_result = get_members_result(members_list, max_point)
    
    # Вывод призёров.
    if favorites_is_exist is True:
        print("Победители есть!")
    else:
        print("Победителей нет!")

    members_resut_count = len(members_result)
    if members_resut_count > 1:
        print(members_resut_count)
    else:
        member = members_result[0]
        print(member.surname, member.name)

# Программу, которая будет определять фамилию и имя лучшего участника, не ставшего победителем олимпиады.
# Если таких участников несколько, т.е. если следующий за баллом победителей один и тот же балл набрали несколько человек,
# или, если победителей нет, а лучших участников несколько (в этом случае именно они являются искомыми),
# то выдается только количество искомых участников. Гарантируется, что искомые участники (участник) имеются. 
#Программа должна выводить через пробел фамилию и имя искомого участника или их количество.
#Пример выходных данных (один искомый участник):
#Семенов Егор
#Второй вариант выходных данных (несколько искомых участников):
#12

def get_members_result(members_list, max_point):
    # Поиск всех учеников с наивысшим баллом.
    members_favorites = list()
    for member in members_list:  
        if max_point == member.points:
            members_favorites.append(member)
  
    return members_favorites
#####################################################################################################################
##################################################### Exec: #########################################################
#####################################################################################################################
main()