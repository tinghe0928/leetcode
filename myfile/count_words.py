def count_words(a, b):
    f1 = open(a, mode='r+')  # open用于打开一个文件，并返回一个文件对象, 使用open记得一定要close文件
    mydic = {}
    for words in f1.read().splitlines():
        mydic[words] = mydic.get(words, 0) + 1
    print(mydic)
    f2 = open(b, mode='w+')
    for words in mydic:
        f2.writelines(words+':'+str(mydic[words])+'\n')
    f1.close()
    f2.close()



count_words('a.txt','b.txt')