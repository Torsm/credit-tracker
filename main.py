import credit.tracker
import credit.version
import credit.session
import getpass
import logging
import argparse
import atexit


def get_md5():
    logging.info('Getting MD5 hash...')
    latest = credit.version.get_latest_version()
    logging.debug('Latest version: ' + latest)
    md5 = credit.version.hash_jar(latest)
    logging.debug('MD5 of latest jar: ' + md5)
    return md5


def create_session(md5):
    username = input('Username: ')
    password = getpass.getpass(prompt='Password: ')
    key = getpass.getpass(prompt='2FA key: ')

    logging.info('Logging in...')
    return credit.session.login(username, password, key, md5)


def main():
    md5 = get_md5()
    rm_session = create_session(md5)
    if rm_session:
        atexit.register(lambda: rm_session.close())
        file = args.output
        f = credit.tracker.write_to_csv(file) if file else credit.tracker.print_console
        logging.info('Starting to track credit')
        credit.tracker.track(rm_session, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help='print debug output', action="store_true")
    parser.add_argument('-o', '--output', metavar='FILE', type=str, help='output csv file')
    args = parser.parse_args()
    print(args)
    pass
    logging.basicConfig(format='%(asctime)s %(levelname)s:\t%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG if args.debug else logging.INFO)
    main()
