import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

email_from = ''
email_to = ''
subject = 'Приглашение!'

letter = """
From: {0}
To:  {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
# На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(email_from, email_to, subject)


name_website = letter.replace('%website%', 'https://dvmn.org/profession-ref-program/nikita5045/EkvHi/')
friend_name = name_website.replace('%friend_name%', 'Друг')
my_name = friend_name.replace('%my_name%', 'Никита')
my_name = my_name.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(login, email_to, my_name)
server.quit()

print (my_name)

