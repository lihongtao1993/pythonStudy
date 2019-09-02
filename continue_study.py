# continue 某一条件满足时，不执行后续重复的代码。执行到continue时，直接跳到循环条件判断处

i = 0

while i < 10:
    if i == 3:

        i += 1 #注意，使用continue关键字时，确认循环的计数是否修改，否则可能会造成死循环

        continue
    print(i)
    i += 1
