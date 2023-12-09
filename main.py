import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import os
import csv

not_sent = [ ["7",'aryusoni2005@gmail.com'], ["11", 'en21cs304099@medicaps.ac.in'],  ["15",'govindnair702@gmail.com'], ["16",'harshitarathore106@gmail.com'],  ["20",'jayeshkushwah31@gmail.com'], ["22",'mansipandey00077@gmail.com'], ["25",'mridulmangal7@gmail.com'], ["42",'pandeyshyam2133@gmail.com'], ["44",'kaleyashika66@gmail.com'], ["48",'charuarya8103@gmail.com'],  ["54",'utsavtiwari4252@gmail.com'], ["56",'mahakkesharwani@gmail.com']]
resend = [["49",'aryanikhil011@gmail.com']]
final = []

def send_email(subject, body, to_email, attachment_path):
    # Email configuration
    from_email = 'connectwithmuacm@gmail.com'  # Replace with your email
    password = 'xnjfewejvsipuvme'     # Replace with your email password
    smtp_server = 'smtp.gmail.com'       # Replace with your SMTP server

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach body text
    message.attach(MIMEText(body, 'plain'))

    # Attach image
    with open(attachment_path, 'rb') as attachment:
        image_mime = MIMEImage(attachment.read(), name=os.path.basename(attachment_path))
        message.attach(image_mime)

    # Connect to SMTP server and send the email
    try:
        with smtplib.SMTP_SSL(smtp_server, 465) as server:
            print(f"sending email to {to_email}")
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message.as_string())
            print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"unable to send email to {to_email}")
        final.append(to_email)
        print(f"Error: {e}")
    


# Example usage
subject = 'Participation Certificate of AINNOVATE'
body = '''
Dear AI enthusiast,

We hope this message finds you well. MUACM Team would like to express its sincere gratitude for your active participation in the immersive AI speaker’s session, ‘AINNOVATE’.

Wait wait wait, before we present you with your certificate, we have an important message for you!  MUACM will soon be conducting recruitments for its executive team.We encourage you to connect with us on Instagram and LInkedIn to stay tuned with all the latest updates.
Instagram handle- mu_acm https://www.instagram.com/mu_acm/?utm_source=ig_web_button_share_sheet&igshid=OGQ5ZDc2ODk2ZA==
LinkedIn page- https://www.linkedin.com/company/acm-student-chapter-medicaps 

Well, needless to say, your presence added immense value to the event. We hope you found the experience insightful and enriching. As a token of appreciation, we are delighted to share your AINNOVATE participation certificate, which you can proudly showcase on your LinkedIn profile. Don't forget to tag MUACM in your post to let your network know about your accomplishment!

[Attachment: Certificate]

We hope the following LinkedIn caption will come in handy when you post your certificate:  
“Hey connections!
I attended a really informative and interactive expert session on #ai called ‘AINNOVATE’ organised by [@medi-caps university acm student chapter]. I am really glad to have received my participation certificate for the same. Excited to be a part of more such immersive sessions in the future!” 

Thank you once again for your contribution to the success of AINNOVATE. We look forward to staying connected and hope to welcome you to our executive team in the near future!

Best regards,
Team MUACM
'''

# with open("sheet.csv","r") as file:
#     sheet = csv.reader(file)


for row in resend:
        # print(int(row[0]))
    img_name = f"./images/{row[0]}.png"
    email = row[1]
    print(row)
    send_email(subject, body, email, img_name)
else:
    print("All Emails sent successfully")

print(final)