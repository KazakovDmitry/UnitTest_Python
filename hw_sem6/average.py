class Spiski:

    def average(list1):
        # list1 = args
        summ = 0
        for i in list1:
            summ += i
        return summ / len(list1)

    def compare(list1, list2):
        a = Spiski.average(list1)
        b = Spiski.average(list2)
        if a > b:
            return "Первый список имеет большее среднее значение"
        elif a == b:
            return "Средние значения равны"
        else:
            return "Второй список имеет большее среднее значение"



