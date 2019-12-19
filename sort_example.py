#初級者向けバブルソートのサンプル

dt_list = [1,8,3,5,2,6,7,4,9]
print(dt_list)                  #初期状態を確認

s_flag = 1
dt_len = dt_list.__len__()-1    #データリストの長さを取得
while s_flag == 1:              #並び替えが発生し亡くなるまで繰り返す
    s_flag = 0
    idx = 0
    while idx < dt_len:
        a = dt_list[idx]
        b = dt_list[idx + 1]
        if a > b:               #指定位置と次を比較する
           dt_list[idx + 1] = a
           dt_list[idx] = b
           s_flag = 1           #並び替えが発生したらフラグを立てる
        idx = idx + 1

print(dt_list)                  #並び替え後の確認

#参考：list型の場合は以下で簡単にソートできる
#dt_list.sort()
#print(dt_list)