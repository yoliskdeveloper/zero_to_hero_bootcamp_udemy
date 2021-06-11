import smtplib
import getpass

# CREATE AKSES TO EMAIL SERVER
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
# optional Port: 485 atau tidak usah dikasih no port nanti library yang akan assign automatic

# CONNECTING TO EMAIL SERVER
smtp_object.ehlo()

# ESTABLISHING CONNECTION WITH TLS
smtp_object.starttls()

# connecting to email login
# email = input('Email: ')                 # optional sign with clear text
email = getpass.getpass('Email: ')         # RECOMMENDED
password = getpass.getpass('Password: ')
smtp_object.login(email, password)
    # must create app_password access or 2FA in gmail account first, and pass the key in password field when prompted

# email body
pengirim = email
penerima = email
subject = input('Masukkan subjet email: ')
message = input('Masukkan pesan email: ')
msg = f'Subject: {subject}\n{message}'

# sending email
smtp_object.sendmail(pengirim,penerima,msg)

# jika setelah proses ini ada tampilan simbol dictionary yang kosong maka itu tandanya email telah berhasil terkirim,
# jika tidak coba cek connection portnya atau password emailnya

# quit connection
smtp_object.quit()
