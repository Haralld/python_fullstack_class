def authenticate(func):
    def wrapper(username, password, *args, **kwargs):
        authorized_users = {'Роман': 'correctpassword'}
        
        if username in authorized_users and password == authorized_users[username]:
            return func(username, *args, **kwargs)
        else:
            print("В доступе отказано!")

    return wrapper

@authenticate
def access_client_data(username):
    print(f"Доступ получен. Данные: ...")


access_client_data('Роман', 'correctpassword')
access_client_data('Олег', 'wrongpassword')


"""
Задание 5: Авторизация доступа к персональным данным клиентов

Описание:  

Для функции `access_client_data`, требующей строгой авторизации,
 Роман хочет добавить декоратор, который будет проверять, 
 есть ли у пользователя соответствующий аутентификационный токен. 
 Авторизоваться может только 'Роман' с паролем 'correctpassword'.


"""