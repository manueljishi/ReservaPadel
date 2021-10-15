import datetime
import sys

# Module to convert dates to proper format to find the button in UPV's website
# WeekdayNumber/Month/Year


def parseDate(day, month, year):
    return "{0}\n{1}/{2}/{3}".format(translateDay(day, month, year), day, month, year)


def translateDay(day, month, year):
    # declare the translation
    weekdays = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }
    date = datetime.datetime(year, month, day)
    weekDay = date.strftime("%A")
    return weekdays.get(weekDay)


# def getCourtLink(court, time):
#     court = int(court)
#     if court == 1:
#         court = 547
#     elif court == 2:
#         court = 548
#     elif court == 3:
#         court = 549
#     elif court == 4:
#         court = 550
#     return "https://intranet.upv.es/pls/soalu/sic_depreservas.solicita_reservar?p_idioma=c&p_vista=intranet&p_volver_a=IN&p_res_pista=8F5528&p_res_fecha=20211014&p_res_horaini={0}:00:00&p_volver_campus=V&p_volver_deporte=279&p_volver_pag=1&p_volver_dia=14/10/21&p_volver_pista={1}".format(
#         time, court
#     )
