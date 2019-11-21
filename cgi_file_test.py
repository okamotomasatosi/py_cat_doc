import cgi
import os

# パラメータの受け取り
form = cgi.FieldStorage()
str_name = form["name"].value

# ファイルに書き出し（追記モード）
f = open('./data/test.txt','a')
f.write(str_name + "\n")
f.close()

# ファイルから読込
read_str = ""
with open('./data/test.txt','r') as f:
    for row in f:
       read_str = read_str +"<br>"+ row.strip()

# htmlで出力する
print ("Content-Type: text/html")
print ()
print ("<html><body>")
print ("これまでに入力された名前は",read_str,"<br>")
print ("<a href=\"../file_test.html\">戻る</a>")
print ("</body></html>")
