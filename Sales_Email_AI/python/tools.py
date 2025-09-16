# %%writefile tools.py
import logging
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict
from config import settings
# In a real project, this would be imported from your agents library
from agents import function_tool # Placeholder

@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Sends an email using the SendGrid API with proper error handling.

    Args:
        subject: The subject line of the email.
        html_body: The HTML content of the email body.

    Returns:
        A dictionary indicating the status of the operation.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Attempting to send email with subject: '{subject}' to {settings.TO_EMAIL}")

    try:
        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        from_email = Email(settings.FROM_EMAIL)
        to_email = To(settings.TO_EMAIL)
        # Note: SendGrid requires a plain text content part even for HTML emails
        content = Content("text/html", html_body)
        mail = Mail(from_email, to_email, subject, content)
        
        response = sg.client.mail.send.post(request_body=mail.get())

        if 200 <= response.status_code < 300:
            logger.info(f"Email successfully sent. Status Code: {response.status_code}")
            return {"status": "success", "message": "Email sent successfully."}
        else:
            logger.error(f"Failed to send email. Status: {response.status_code}, Body: {response.body}")
            return {"status": "error", "message": f"SendGrid error: {response.status_code}"}

    except Exception as e:
        logger.critical(f"An unexpected error occurred while sending email: {e}", exc_info=True)
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}