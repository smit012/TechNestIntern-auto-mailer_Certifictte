import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

# For full HTML rendering
import streamlit.components.v1 as components

# Configuration (use st.secrets in production)
YOUR_EMAIL = "technestintern.intern@gmail.com"
YOUR_PASSWORD = "mogkdkvyjgwqeaeq"

# Streamlit UI
st.set_page_config(page_title="TechNest Auto Mail Tool", layout="centered")
st.markdown("### 💌🏆 TechNest Internship Certificate - Auto Mail Sender")

receiver_email = st.text_input("Enter Intern's Email")
send_button = st.button("Send Email")

# Email subject
subject = "🎉 Congratulations on Completing Your Internship at TechNest Intern"
st.markdown(f"**Email Subject:** {subject}")

# Email HTML Body
html_body = """
<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; line-height:2; color: #000; ">
    <p>Dear <strong>Intern</strong>,</p>

    <p>Congratulations on successfully completing your internship with <strong>TechNest Intern 🎓</strong>!</p>
    <p> We sincerely appreciate the dedication, consistency, and effort you demonstrated throughout the program. Your commitment to completing the assigned tasks on time and with quality has not gone unnoticed.</p>
    <p>As a recognition of your hard work, we are pleased to provide you with the following:.</p>
    
    <hr>  
    <h3>🏆 Certificate of Completion</h3>
    <ol>
      <li>
           This certificate acknowledges your successful completion of the internship and reflects your practical learning and project contributions.<br>
        👉 <a href="https://drive.google.com/drive/u/4/folders/1ZJPaI2tD_ATzJ5OvYpxprMmW55OE7lZO" target="_blank"> Download Completion Certificate</a>
      </li><br></ol>
      <hr>
    <h3>✉️ Letter of Recommendation</h3>
    <ol>
      <li>
           Based on your performance, we are also happy to issue you a Letter of Recommendation, which you can use to strengthen your resume or future job applications.<br>
         <a href="https://drive.google.com/drive/u/4/folders/1gphuN6ypxg3qGQJltrmQbLwL0E-Mb5jY" target="_blank">👉 Download Letter of Recommendation</a>
      </li><br></ol>
<hr>
    <p>We hope this internship experience has added value to your professional journey and provided you with meaningful insights and skills. Feel free to add this internship to your LinkedIn profile and resume to showcase your learning and contributions.🚀</p>
    <p> ⚠️   Kindly add this certificate in your linkedin and tag us<strong> @TechNest Intern </strong>, and also add experience section , our team will visit your linkedin profile soon.</p>
    <p>⚠️    Add your task individually not in video and also try to complete the remaining task , that is really going to be helpful in your future.</p>
    <p> Wishing you all the best for your future endeavors. Keep growing and keep shining! 🌟</p>
    <hr>
    <p>Best regards,<br>
    <strong>TechNest Intern</strong><br>
    🔗 <a href="https://www.linkedin.com/company/technestintern/about/" target="_blank">LinkedIn</a></p>

    <img src="https://i.ibb.co/Y4vZ2819/logo.png" alt="TechNest Logo" width="160"/>
  </body>
</html>
"""



# Email Sending Logic
if send_button and receiver_email:
    email_list = [email.strip() for email in receiver_email.split(",") if email.strip()]

    success_list = []
    fail_list = []

    for email in email_list:
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = YOUR_EMAIL
            msg["To"] = email

            msg.attach(MIMEText(html_body, "html"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(YOUR_EMAIL, YOUR_PASSWORD)
                server.sendmail(YOUR_EMAIL, email, msg.as_string())

            success_list.append(email)
        except Exception as e:
            fail_list.append((email, str(e)))

    if success_list:
        st.success("✅ Email sent to:\n" + ", ".join(success_list))
    if fail_list:
        st.error("❌ Failed to send to:")
        for email, err in fail_list:
            st.error(f"{email} ➜ {err}")

# Full HTML Preview
st.markdown("### 📨 Email Preview")
components.html(html_body, height=2000,)