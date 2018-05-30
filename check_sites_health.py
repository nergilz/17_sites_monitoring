import whois
import argparse
import datetime
import requests
import sys
import calendar
import socket


def get_arguments():

    parser = argparse.ArgumentParser(
        description='Path to domain names file'
        )
    parser.add_argument(
        '--path',
        required=False,
        default='urls.txt',
        help='Optional parameter: "urls.txt"'
        )
    return parser.parse_args()


def load_urls4check(path):

    with open(path, 'r') as file_handler:
        list_urls = file_handler.read().split('\n')

    return [url for url in list_urls if url is not '']


def is_server_respond_with_200(url):

    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False


def get_domain_expiration_date(domain_name):

    response = whois.whois(domain_name)
    expiration_date = response["expiration_date"]

    if isinstance(expiration_date, list):
        return expiration_date[0]
    else:
        return expiration_date


def check_payment_date(expiration_date):

    date_now = datetime.datetime.now()
    days_in_month = calendar.monthrange(date_now.year, date_now.month)[1]
    check_date = date_now + datetime.timedelta(days=days_in_month)

    if check_date < expiration_date:
        return True
    else:
        return False


def pprint_sites_health(url, status, check_date, expiration_date):

    print('{}; status: {}; domain_payment_>_month: {}; date to: {}'.format(
        url,
        status,
        check_date,
        expiration_date.strftime('%Y-%m-%d')
        )
    )


def check_urls(list_urls4check):

    for url in list_urls4check:

        try:
            status = is_server_respond_with_200(url)
            expiration_date = get_domain_expiration_date(url)
            check_date = check_payment_date(expiration_date)
            pprint_sites_health(
                url,
                status,
                check_date,
                expiration_date
                )

        except ConnectionResetError as err:
            print(' ERROR WHOIS response: {}; error: {}'.format(url, err))

        except socket.error as err:
            print(' ERROR {}; socket: {}'.format(url, err))


if __name__ == '__main__':
    arguments = get_arguments()

    try:
        list_urls4check = load_urls4check(arguments.path)

    except FileNotFoundError as err:
        sys.exit(' ERROR: {}'.format(err))

    check_urls(list_urls4check)
