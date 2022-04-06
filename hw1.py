'''
our function prints time and weather info at Berlin, NY and Kyiv
wrapper - changes it via adding UTC format to date
'''
from functools import wraps
from datetime import datetime, timedelta
from random import choice

weather_encount = ['sunny', 'cloudy', 'rainy', 'windy', 'foggy']


def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        info_sent = func(*args, **kwargs)
        if 'NY' in info_sent:
            gmt_zone = 'GMT-4 '
        elif 'Berlin' in info_sent:
            gmt_zone = 'GMT+2 '
        else:
            gmt_zone = 'GMT+3 '

        insertion_place = info_sent.rfind(':') + 4
        return info_sent[:insertion_place] + gmt_zone \
               + info_sent[insertion_place:]

    return wrapper


@decorate
def decorated_function_ny() -> str:
    return f'Today in NY is ' \
           f'{(datetime.now() - timedelta(hours=7)).strftime("%m/%d/%Y, %H:%M:%S")}' \
           f' and {choice(weather_encount)}'


@decorate
def decorated_function_berlin() -> str:
    return f'Today in Berlin is ' \
           f'{(datetime.now() - timedelta(hours=1)).strftime("%m/%d/%Y, %H:%M:%S")} ' \
           f'and {choice(weather_encount)}'


@decorate
def decorated_function_kyiv() -> str:
    return f'Today in Kyiv is ' \
           f'{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} ' \
           f'and {choice(weather_encount)}'


def default_function_ny() -> str:
    return f'Today in NY is ' \
           f'{(datetime.now() - timedelta(hours=7)).strftime("%m/%d/%Y, %H:%M:%S")} ' \
           f'and {choice(weather_encount)}'


def main():
    print(decorated_function_ny() + '\nvs\n' + default_function_ny())
    print('Location decorated_test {} and its name {}'
          .format(decorated_function_ny, decorated_function_ny.__name__))
    print(f'Location default test {default_function_ny} '
          f'and its name {decorated_function_ny.__name__}')


if __name__ == '__main__':
    main()
