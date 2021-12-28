
import smtplib
#處理游件內容的函示
from email.mime.text import MIMEText
#處理郵件附件，需要導入MIMEMultipart,Herder,MIMEBass
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

mailserver='smtp.gmail.com'     #郵件服務端URL
userName_SendMil='roy980630@gmail.com' #發件人
userName_AuthCode='nkniytzwgcuryepu'   #寄件人
received_mail=['royhongci@gmail.com'] #定義由件接收者

#發送一封簡單的郵件

# =============================================================================
# content='這是一封測試信件'
# email=MIMEText(content,'plain','utf-8')#以純文本方指呃郵件內容的定義，透過MIMEText進行操作
# 
# email["Subject"] ='郵件主題'#郵件主旨
# email["From"]=userName_SendMil #發件人
# email["To"]=','.join(received_mail) #收件人
# =============================================================================




#發送一封HTML內容的郵件
# =============================================================================
# content="""
# <p>這是一封HTML文本的郵件</p>
# <p><a href="https://ithelp.ithome.com.tw/users/20111432/ironman/1635?page=4">點擊這裡看文章</p>
# 
# 
# """
# email=MIMEText(content,'html','utf-8')#內容，展示行式，編碼方式
# email["Subject"] ='郵件主題_HTML'#郵件主旨
# email["From"]=userName_SendMil #發件人
# email["To"]=','.join(received_mail) #收件人
# =============================================================================


#郵件發送附件
#附件配置email
email=MIMEMultipart()    #以純文本方指呃郵件內容的定義，透過MIMEText進行操作

email["Subject"] ='郵件主題'#郵件主旨
email["From"]=userName_SendMil #發件人
email["To"]=','.join(received_mail) #收件人


#一般附件
att=MIMEBase('application','octet-stream')
att.set_payload(open('自動化測試.docx','rb').read())
att.add_header('Content-Disposition', 'attachment',filename=Header('自動化測試.docx','gbk').encode())
encoders.encode_base64(att)
email.attach(att)








#圖片附件




att1=MIMEBase('application','octet-stream')
att1.set_payload(open('未0名.png','rb').read())
att1.add_header('Content-Disposition', 'attachment',filename=Header('未0名.png','gbk').encode())
encoders.encode_base64(att1)
email.attach(att1)












#發送郵件

smtp=smtplib.SMTP_SSL(mailserver,port=465)#port=465 gmail的外送port  內送port=993
smtp.login(userName_SendMil,userName_AuthCode) #登入
smtp.sendmail(userName_SendMil,','.join(received_mail),email.as_string())


smtp.quit()

print("complete")


