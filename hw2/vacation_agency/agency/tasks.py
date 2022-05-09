from .celery import app
from celery.schedules import crontab
from typing import List, Tuple
from agency.mail_sender import send_message

app.conf.timezone = 'UTC'


def get_all_birthdays_from_db() -> List[Tuple[str, str]]:
    return [('1email@g.com', 'Ema'), ('2email@g.com', 'Tom'), ('3email@g.com', 'Jim')]


# просим пользователя подтвердить имейл
@app.task
def email_confirmation(mail, name):
    print('Email almost sent')
    mail_text = f'Dear {name}, please confirm your mail'
    send_message(mail, mail_text)
    info_text = f'Dear {name}, check your mail, we\'ve sent a confirmation on {mail}'
    print(info_text)


# каждый день смотрим есть ли у нас юзеры у которых день рождения, давая им скидку
@app.task
def birthday_congratulation():
    all_birthday_mails = get_all_birthdays_from_db()
    text = "Happy birthday, {}" \
           "we also want congratulate you - voucher for you"
    for birthday_mail, birthday_name in all_birthday_mails:
        send_message(birthday_mail, text.format(birthday_name))


app.conf.beat_schedule = {
    'add-someone-birthday-congrats': {
        'task': 'agency.tasks.birthday_congratulation',
        'schedule': crontab(hour=14, minute=0),
        # 'args': (17, 16),
    },
}
