def exchange_first_last(list):
    list[0], list[-1] = list[-1], list[0]
    return list

list = [1, 2, 3, 4, 5]
print(exchange_first_last(list))


# long method
def exchange_first_last2(list):
    list.insert(0, list.pop(len(list)-1))
    list.append(list.pop(1))
    return list


list = [1, 2, 3, 4, 5]
print(exchange_first_last2(list))

# another method
def exchange_first_last3(list):
    x = list[0], list[-1]
    list[-1], list[0] = x
    x=2
    return list,x
list = [1, 2, 3, 4, 5]
list,x=exchange_first_last3(list)
print(x)
print(list)