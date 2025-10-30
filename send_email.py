import os
import smtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import markdown

from parse_json_to_md import render_md_string


def send_email_notification(selected_papers, config):
    """
    Send email notification with selected papers.

    Args:
        selected_papers: Dictionary of selected papers
        config: ConfigParser object with email settings
    """
    # Get email configuration
    sender_email = config["EMAIL"]["sender_email"]
    recipient_email = os.environ.get("EMAIL_RECIPIENT")
    email_password = os.environ.get("EMAIL_PASSWORD")
    smtp_server = config["EMAIL"]["smtp_server"]
    smtp_port = int(config["EMAIL"]["smtp_port"])
    subject = config["EMAIL"]["email_subject"]

    # Validate required environment variables
    if not recipient_email:
        print("Warning: EMAIL_RECIPIENT not set - skipping email")
        return
    if not email_password:
        print("Warning: EMAIL_PASSWORD not set - skipping email")
        return

    # Check if there are any papers to send
    if not selected_papers or len(selected_papers) == 0:
        print("No papers to send via email")
        return

    # Generate markdown content
    md_content = render_md_string(selected_papers)

    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'nl2br']
    )

    # Add some basic styling
    html_with_style = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2 {{
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }}
                a {{
                    color: #3498db;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .paper {{
                    margin-bottom: 30px;
                    padding: 15px;
                    background-color: #f8f9fa;
                    border-left: 4px solid #3498db;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
    </html>
    """

    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    # Add both plain text and HTML versions
    part1 = MIMEText(md_content, "plain")
    part2 = MIMEText(html_with_style, "html")

    message.attach(part1)
    message.attach(part2)

    # Send email
    try:
        print(f"Connecting to {smtp_server}:{smtp_port}...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            print("Logging in...")
            server.login(sender_email, email_password)
            print(f"Sending email to {recipient_email}...")
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent successfully to {recipient_email}")
            print(f"Sent {len(selected_papers)} paper(s)")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise


if __name__ == "__main__":
    # Test the email functionality
    config = configparser.ConfigParser()
    config.read("configs/config.ini")

    # Load test data
    import json
    with open("out/output.json", "r") as f:
        selected_papers = json.load(f)

    send_email_notification(selected_papers, config)
