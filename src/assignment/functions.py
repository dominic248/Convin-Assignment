import hashlib
from django.conf import settings
from django.core.mail import EmailMessage

def sendHTMLEmail(html_content,emails,subject,attachment=None):
    email = EmailMessage(subject, html_content, settings.EMAIL_HOST_USER, emails)
    email.content_subtype = "html"
    if attachment:
        email.attach_file(attachment)
    res = email.send()

def calc_sha256(afile):
        hasher = hashlib.sha256()
        blocksize=65536
        try:
            buf = afile.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(blocksize)
            return hasher.hexdigest()
        except:
            return None