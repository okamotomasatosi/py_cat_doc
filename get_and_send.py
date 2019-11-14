import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl

from datetime import datetime

import requests
from bs4 import BeautifulSoup

def web_get_test():
    get_data = requests.get('https://www.chancelab.jp/')
    soup_data = BeautifulSoup(get_data.text, 'html.parser')
    print(soup_data.p)    # pタグの文字列を取得する　※最初の行しか取れない
    print('---------------')
    #p_teams = soup_data.select('.info-title')  #classを指定する場合
    p_teams = soup_data.select('p') # pタグを指定して全行を取得する
    for p_man in p_teams:
        print(p_man)
    return

def web_get_chart():
    get_data = requests.get('https://仮想通貨の情報がhtmlで取れるサイトURL')
    soup_data = BeautifulSoup(get_data.text, 'html.parser')
    p_teams = soup_data.select('.currencyPrice')  #classを指定する場合
    p_man = p_teams[0]
    print(str(p_man))
    st_pos = 1 + str(p_man).find('>')
    ed_pos = str(p_man).find('</dd>')
    ret_str = str(p_man)[st_pos:ed_pos]
    print(ret_str)
    return ret_str

##　ココから下はメール処理
#gmailの設定で、安全性の低いアプリのアクセス　を有効　にしないと動作しないよ
def mail_test(str_message):
    FROM_ADDRESS = '送り元めーるあどれす@gmail.com'
    MY_PASSWORD = 'ぱすわーど'
    TO_ADDRESS = '送りたいメールアドレス@ドメイン.jp'
    BCC = ''
    SUBJECT = 'GmailのSMTPサーバ経由'
    BODY = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S")) + '\n１ビットコイン＝' + str_message + '円'
    msg = MIMEText(BODY)
    msg['Subject'] = SUBJECT
    msg['From'] = FROM_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Bcc'] = BCC
    msg['Date'] = formatdate()

    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_string())
    smtpobj.close()
    return


#ココから処理開始　いわゆる　ｍａｉｎ
if __name__ == '__main__':
    str_message = web_get_chart()
    mail_test(str_message)