import csv
import logging
import time


def track(session, func):
    func(session)
    while True:
        try:
            if session.revalidate():
                func(session)
        except Exception as ex:
            if 'Session does not exist or has expired. Please restart.' in ex.args:
                break
            logging.error(ex)
        time.sleep(30)


def print_console(session):
    logging.info(session.credit)


def write_to_csv(file):
    def f(session):
        with open(file, 'a', newline='') as fd:
            writer = csv.writer(fd)
            writer.writerow([int(time.time()), session.credit])
    return f
