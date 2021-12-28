
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mailserver='smtp.gmail.com'     #郵件服務端URL
userName_SendMil='roy980630@gmail.com' #發件人
userName_AuthCode='nkniytzwgcuryepu'   #授權碼
received_mail='royhongci@gmail.com' #定義由件接收者

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "Learn Code With Mike"  #郵件標題
content["from"] = userName_SendMil #寄件者
content["to"] = received_mail #收件者
content.attach(MIMEText("測試用文件"))  #郵件內容

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login(userName_SendMil,userName_AuthCode)  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)




# =============================================================================
# import os
# import sys
# import smtplib
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# 
# COMMASPACE = ', '
# 
# def main():
#     sender = '你的EMAIL'
#     gmail_password = '你的EMAIL密碼'
#     recipients = ['收件人01的EMAIL','收件人02的EMAIL']
#     
#     # 建立郵件主題
#     outer = MIMEMultipart()
#     outer['Subject'] = '主題'
#     outer['To'] = COMMASPACE.join(recipients)
#     outer['From'] = sender
#     outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
# 
#     # 檔案位置 在windows底下記得要加上r 如下 要完整的路徑
#     attachments = [r'C:\Users\witkaiy\OneDrive\code sample\work\your_file.xls']
# 
#     # 加入檔案到MAIL底下
#     for file in attachments:
#         try:
#             with open(file, 'rb') as fp:
#                 print ('can read faile')
#                 msg = MIMEBase('application', "octet-stream")
#                 msg.set_payload(fp.read())
#             encoders.encode_base64(msg)
#             msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
#             outer.attach(msg)
#         except:
#             print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
#             raise
# 
#     composed = outer.as_string()
# 
#     # 寄送EMAIL
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as s:
#             s.ehlo()
#             s.starttls()
#             s.ehlo()
#             s.login(sender, gmail_password)
#             s.sendmail(sender, recipients, composed)
#             s.close()
#         print("Email sent!")
#     except:
#         print("Unable to send the email. Error: ", sys.exc_info()[0])
#         raise
# 
# if __name__ == '__main__':
#     main()
# 
# =============================================================================




