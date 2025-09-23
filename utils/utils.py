import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_auto_reply(platform, name, last_name, recipient_email, smtp_user, smtp_pass):
    if platform.lower() == 'windows':
        download_link = "https://github.com/StevetheGreek97/SegmentME-docs/releases/download/v1.0.2.0/SegmentME-v1.0.2.0..exe"
    elif platform.lower() == 'macos':
        download_link = "https://github.com/StevetheGreek97/SegmentME-docs/releases/download/v1.0.2.0/SegmentME-v1.0.2.0..dmg"

    subject = "🎉 Your SegmentME Installer is Ready"
    body = f"""
Hi {name} {last_name},

Thanks for your interest in SegmentME!

You can download the Windows installer here:
🔗 {download_link}


If you have any questions or feedback, feel free to reply to this email.

Best regards,  
PopGen Team
"""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def notify_admin(name, last_name, user_email, comments, smtp_user, smtp_pass, recipient_email):
    subject = "📥 New SegmentME Installer Request"
    body = f"""
You received a new request for the SegmentME installer.

👤 Name: {name} {last_name}
📧 Email: {user_email}
📝 Comments: {comments or 'None provided'}

Please follow up manually with the download link.
"""

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


def get_text(section, file_path='assets/text.yaml'
):
    """
    Get the text for a given section from the text.yaml file.
    
    Args:
        section (str): The section to retrieve text for.
        
    Returns:
        str: The text for the specified section.
    """
    import yaml
    from pathlib import Path

    # Load the YAML file
    text_file = Path(__file__).parent.parent / file_path
    with open(text_file, 'r') as file:
        text_data = yaml.safe_load(file)

    # Return the requested section
    return text_data.get(section, '')


if __name__ == "__main__":
    # Example usage
    section = 'intro'
    text = get_text(section)
    print(f"Text for section '{section}': {text}")
    # Output: Text for section 'intro': SegmentME is a powerful image annotation and segmentation tool designed for high-throughput phenotyping, object instance analysis, and smart annotation workflows using models like
