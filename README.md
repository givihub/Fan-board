# Проект Фанатский сервер
В основе проекта лежит база данных db.sqlite3

## Инструкции по Установке
Используется Python 3.11

Для установки Django выполните команду: pip install django

Установите все необходимые библиотеки, выполнив команду: pip install -r requirements.txt

Запустите приложение: python manage.py runserver

На основе фанатского сервера известной игры The Lord of the Rings Online был разработан интернет-ресурс, представляющий собой своеобразную доску объявлений. Пользователи ресурса имеют возможность зарегистрироваться по электронной почте, получив при этом письмо с кодом подтверждения регистрации.

После успешной регистрации пользователи получают доступ к созданию и редактированию объявлений. Каждое объявление включает в себя заголовок и текст, который может содержать изображения, встроенные видео и другой контент.

Пользователи могут отправлять отклики на объявления других пользователей, представленные в виде простого текста. При отправке отклика пользователь автоматически получает уведомление на свою электронную почту.

Также предусмотрена приватная страница пользователя, где отображаются отклики на его объявления. На этой странице пользователь может фильтровать отклики по объявлениям, удалять их, а также принимать (при принятии отклика отправителю также приходит уведомление).

Дополнительно, пользователь обязан указать своё объявление в одной из категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Предусмотрена возможность отправки новостных рассылок пользователям.