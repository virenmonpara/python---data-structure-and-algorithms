from collections import Counter


def anagram_subset(string):
    lst = string.split(' ')

    for i in range(len(lst)):
        lst[i] = ''.join(sorted(lst[i]))

    dictionary = Counter(lst)
    print(list(sorted(dictionary.items(),
          reverse=True, key=lambda item: item[1]))[0])


# driver code
string = 'ram hello olleh viren elloh mra nvire viern nrvie vkm'
anagram_subset(string)
