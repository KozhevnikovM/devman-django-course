# Сайт "Куда пойти" 
## Демо:
Демонстрационная версия сайта доступна по [ссылке](https://mikhailkozhevnikov.pythonanywhere.com/)

## Системные требования:
python3.5+

## Установка:
### Локально:

```bash
git clone https://github.com/KozhevnikovM/devman-django-course
cd devman-django-course
mv example.env .env
```
1. Откройте файл .env в вашем любимом текстовом редакторе и пропишите ваши переменные окружение
  
  ```
  DEBUG=True #Локально используйте True, в продакшене - False
  SECRET_KEY='Secure-Me' #длинная и сложная строка для предотвращения CSRF-атак 
  ALLOWED_HOSTS=localhost,127.0.0.1,'*' #список доменов, подключенных к сайту. Можно прописать несколько доменов, разделив их запятыми.
  ```
  
2. Установите зависимости

  ```bash
  pip install -r requirements.txt
  ```
2. Создайте суперпользователя
  ```bash
  python manage.py createsuperuser
  
  ```
4. Запустите сервер разработки
  ```bash
  python manage.py runserver
  ```
### На бесплатном хостинге python-anywhere:
1. Создайте папку для проекта, пропишите переменные окружения в файл ```.env``` 
  ```bash
  mkdir your-project-name && cd your-project-name
  wget https://raw.githubusercontent.com/KozhevnikovM/devman-django-course/master/example.env
  mv example.env .env
  nano .env
  ```
2. Пропишите ваши переменные окружения (Ctrl+X выход из текстового редактора)
  ```
  DEBUG=False
  SECRET_KEY=sUpEr-Long-aNd-sEcurE-StRing
  ALLOWED_HOSTS=[mydomain.pythonanyware.com, mydomain.com]
  ```
4. Установите вспомогательную утилиту от pythonanywhere и запустите деплой. Процесс пройдет автоматически.
  ```bash
  pip3.6 install --user pythonanywhere
  pa_autoconfigure_django.py https://github.com/KozhevnikovM/devman-django-course
  ```
4. При необходимости, создайте суперпользователя и импортируйте точки.

## Импорт данных о точках из json:
Из интернета:
```
python manage.py load_place --url url-for-your-json-url
```
или из файла расположенного локально:
```
python manage.py load_place --path your-json-local-file
```

Со структурой json-файла для импорта можно ознакомиться по [данной ссылке](https://github.com/devmanorg/where-to-go-places/tree/master/places)

Скачать демонстрационные файлы json без картинок:
```
mkdir temp/ && cd temp/
git init
git remote add –f origin https://github.com/devmanorg/where-to-go-places.git

git config core.sparsecheckout true
echo places/ >> .git/info/sparse-checkout
git pull origin master
```

Для обработки сразу нескольких файлов из папки, можно воспользоваться циклом bash:
```
for filename in temp/places/*.json; do
  python manage.py load_place --path "$filename"
done
```

## Project Goals
Код написан в образовательных целях в рамках курса Django с сайта [dvmn.org](dvmn.org).
