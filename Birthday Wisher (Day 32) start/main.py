import smtplib

my_email = "tonigundersson@gmail.com"
password = "happynewyearandgodjul!"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tomoyuki.eguchi@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )


