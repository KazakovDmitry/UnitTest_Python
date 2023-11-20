class Spiski:
    list1 = [5, 6, 10]
    list2 = []

    def average(self, list1):
        sum = 0
        for i in range(list1):
            sum += i
        return sum / len(list1)
