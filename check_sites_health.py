import whois
import argparse
import datetime
import requests
import sys
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
    parser.add_argument(
        '--days',
        required=False,
        default=30,
        help='Amount of days to check the payment date'
    )
    return parser.parse_args()


def load_urls4check(path):

    with open(path, 'r') as file_handler:
        list_urls = file_handler.read().split('\n')

    return [url for url in list_urls if url is not '']


def is_server_respond_with_ok(url):
    try:
        response = requests.get(url)
        return response.ok
    except requests.exceptions.ConnectionError:
        return None


def get_domain_expiration_date(domain_name):

    try:
        response = whois.whois(domain_name)
        expiration_date = response['expiration_date']

        if isinstance(expiration_date, list):
            return expiration_date[0]
        else:
            return expiration_date

    except ConnectionResetError:
        return False

    except socket.error:
        return False


def check_payment_date(expiration_date, amount_of_days):
    date_now = datetime.datetime.now()

    check_date = date_now + datetime.timedelta(amount_of_days)
    return bool(check_date < expiration_date)


def check_urls(list_urls4check, amount_of_days):
    verified_urls = {}

    for url in list_urls4check:
        check_payment = False

        status = is_server_respond_with_ok(url)
        if status is not None:
            expiration_date = get_domain_expiration_date(url)

            if expiration_date is False:
                expiration_date = 'WHOIS_connection_reset'
            elif expiration_date is None:
                expiration_date = 'Date_not_defined'
            else:
                check_payment = check_payment_date(expiration_date, amount_of_days)
                expiration_date.strftime('%Y-%m-%d')

            verified_urls.setdefault(url, [status, check_payment, expiration_date])

        else:
            verified_urls.setdefault(url, status)

    return verified_urls


def pprint_sites_health(verified_urls):

    for url, check_list in verified_urls.items():

        if check_list is not None:
            print('{}; status: {}; domain_payment_>_month: {}; date to: {}'.format(
                url,
                check_list[0],
                check_list[1],
                check_list[2]
                )
            )
        else:
            print('{}; status: NO domain access'.format(url))


if __name__ == '__main__':
    arguments = get_arguments()

    try:
        list_urls4check = load_urls4check(arguments.path)

    except FileNotFoundError as err:
        sys.exit(' ERROR: {}'.format(err))

    verified_urls = check_urls(list_urls4check, arguments.days)
    pprint_sites_health(verified_urls)
