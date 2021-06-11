import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')
email_add =  getpass.getpass('Email: ')
password = getpass.getpass('Password: ')        # GUNAKAN APP PASSWORD FROM GOOGLE ACCOUNT

M.login(email_add, password)

# CHECK EMAIL METHOD (INBOX,PERSONAL, RECEIPTS, SENT, DLL )
M.list()

# SELECT FITUR MANA YANG KITA PILIH
M.select('inbox')   # contoh pilih inbox
    # jika berhasil akan muncul tanda ok beserta no connection

typ, data = M.search(None, 'SUBJECT "your text in here"')
    # ingat FROM, TO, dll adalah huruf besar, sedangkan element yang kita cari bisa huruf capital atau huruf kecil

# sebelmum masuk ke sini, cari tahu dulu berapa email yang ada berdasarkan pencarian kita dengan memanggil print(
# data). lalu kita akan mencari berdasarkan index yang ditampilkan oleh email
# print(data)

email_id = data[0]
result , email_data = M.fetch(email_id, '(RFC822)') # RFC822 adalah protokol email

# print(email_data)  # untuk mengecek email yang akan kita ambil, lalu masukkan berdasarkan indenya

raw_email = email_data[0][1]

raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

#LOOPIING
for part in email_message.walk():

    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
