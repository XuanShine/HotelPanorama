from pyexcel_ods3 import get_data
from datetime import date, timedelta
import yaml


def format_date(date_str):
    return date(*map(int, date_str.split('-')))


def list_number_room_booked(file):
    """ Return a dict """
    reservations = get_data(file)

    result = dict()

    for reservation in reservations['Sheet1'][1:]:
        arrive = format_date(reservation[3])
        depart = format_date(reservation[4])
        one_day = timedelta(days=1)
        number = reservation[7]
        # FIXME: éviter les réservations annulées.
        while arrive != depart:
            try:
                result[arrive] += number
            except:
                result[arrive] = number
            arrive += one_day
    return result


# with open('reservation.txt', 'w') as f_out:
#     f_out.write(yaml.dump(result, default_flow_style=False))
