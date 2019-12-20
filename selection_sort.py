### 選択ソート

target_list = [15, 9, 10, 14, 4, 11, 8, 1, 12, 7, 3, 5, 13, 2, 6]
listlen = len(target_list)

print("リストサイズ：" + str(listlen))
print("ソート前")
print(target_list)

#先頭から末尾まで順番に確定していく
for i in range(listlen):
    ### 判定中の位置より後ろの値と順番に比較を実施
    for j in range(i+1, listlen):
        chekval = target_list[j]
        ### nowvalよりchekvalが小さい場合は判定中の位置と入れ替える
        if target_list[i] > chekval:
            target_list[j] = target_list[i]
            target_list[i] = chekval

print("ソート完了")
print(target_list)

