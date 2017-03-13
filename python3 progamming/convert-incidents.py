# -*- coding:utf-8 -*-

import datetime

class IncidentError(Exception):pass

class Incident:
    def __init__(self, report_id, date, airport, aircraft_id, aircraft_type, pilot_percent_hour_on_type, pilot_total_hours, midair, narrative=""):
        assert len(report_id) >= 8 and len(report_id.spilt()) == 1, "invalid report ID"
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_id = aircraft_id
        self.aircraft_type = aircraft_type
        self.pilot_percent_hour_on_type = pilot_percent_hour_on_type
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,date):
        assert isinstance(date,datetime.date), "invalid date"
        self.__date = date

    @property
    def airport(self):
        return self.__airport

    @airport.setter
    def airport(self, airport):
        assert isinstance(airport, str), "invalid airport"
        self.__airport = airport

    @property
    def aircraft_id(self):
        return self.__aircraft_id

    @aircraft_id.setter
    def aircraft_id(self, aircraft_id):
        assert isinstance(aircraft_id, str), "invalid aircraft ID"
        self.__aircraft_id = aircraft_id

    @property
    def aircraft_type(self):
        return self.__aircraft_type

    @aircraft_type.setter
    def aircraft_type(self, aircraft_type):
        assert isinstance(aircraft_type, str), "invalid aircraft_type"
        self.__aircraft_type = aircraft_type

    @property
    def pilot_percent_hour_on_type(self):
        return self.__pilot_percent_hour_on_type

    @pilot_percent_hour_on_type.setter
    def pilot_percent_hour_on_type(self, pilot_percent_hour_on_type):
        assert isinstance(pilot_percent_hour_on_type, float), "invalid pilot_percent_hour_on_type"
        self.__pilot_percent_hour_on_type = pilot_percent_hour_on_type

    @property
    def pilot_total_hours(self):
        return self.__pilot_total_hours

    @pilot_total_hours.setter
    def pilot_total_hours(self, pilot_total_hours):
        assert isinstance(pilot_total_hours, int), "invalid pilot_total_hours"
        self.__pilot_total_hours = pilot_total_hours

    @property
    def midair(self):
        return self.__midair

    @midair.setter
    def midair(self, midair):
        assert isinstance(midair, bool), "invalid midair"
        self.__midair = midair

    @property
    def narrative(self):
        return self.__narrative

    @narrative.setter
    def narrative(self, narrative):
        assert isinstance(narrative, str), "invaild narrative"
        self.__narrative = narrative

class IncidentCollection(dict):

    def values(self):
        for report in self.keys():
            yield self[report_id]

    def items(self):
        for report_id in self.keys():
            yield(report_id, self[report_id])

    def _iter_(self):
        for report_id in sorted(super().keys()):
            yield report_id

    keys = _iter_


