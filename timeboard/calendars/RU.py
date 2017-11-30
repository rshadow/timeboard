from .calendarbase import CalendarBase
from ..core import get_timestamp
from ..timeboard import Organizer
from itertools import product


def holidays(start_year, end_year, work_on_dec31):
    dates = ['01 Jan', '02 Jan', '03 Jan', '04 Jan', '05 Jan',
             '06 Jan', '07 Jan', '23 Feb', '08 Mar', '01 May',
             '09 May', '12 Jun', '04 Nov']
    if not work_on_dec31:
        dates.append('31 Dec')
    years = range(start_year, end_year + 1)
    return {"{} {}".format(day, year): 0
            for day, year in product(dates, years)}


def changes(eve_hours):
    x = eve_hours
    return {
        '10 Jan 2005': 0, '22 Feb 2005': x, '05 Mar 2005': x, '07 Mar 2005': 0,
        '02 May 2005': 0, '10 May 2005': 0, '14 May 2005': 8, '13 Jun 2005': 0,
        '03 Nov 2005': x,
        '09 Jan 2006': 0, '22 Feb 2006': x, '24 Feb 2006': 0, '26 Feb 2006': 8,
        '07 Mar 2006': x, '06 May 2006': x, '08 May 2006': 0, '03 Nov 2006': x,
        '06 Nov 2006': 0,
        '08 Jan 2007': 0, '22 Feb 2007': x, '07 Mar 2007': x, '28 Apr 2007': x,
        '30 Apr 2007': 0, '08 May 2007': x, '09 Jun 2007': x, '11 Jun 2007': 0,
        '05 Nov 2007': 0, '29 Dec 2007': x, '31 Dec 2007': 0,
        '08 Jan 2008': 0, '22 Feb 2008': x, '25 Feb 2008': 0, '07 Mar 2008': x,
        '10 Mar 2008': 0, '30 Apr 2008': x, '02 May 2008': 0, '04 May 2008': 8,
        '08 May 2008': x, '07 Jun 2008': 8, '11 Jun 2008': x, '13 Jun 2008': 0,
        '01 Nov 2008': x, '03 Nov 2008': 0, '31 Dec 2008': x,
        '08 Jan 2009': 0, '09 Jan 2009': 0, '11 Jan 2009': 8, '09 Mar 2009': 0,
        '30 Apr 2009': x, '08 May 2009': x, '11 May 2009': 0, '11 Jun 2009': x,
        '03 Nov 2009': x, '31 Dec 2009': x,
        '08 Jan 2010': 0, '22 Feb 2010': 0, '27 Feb 2010': x, '30 Apr 2010': x,
        '03 May 2010': 0, '10 May 2010': 0, '11 Jun 2010': x, '14 Jun 2010': 0,
        '03 Nov 2010': x, '05 Nov 2010': 0, '13 Nov 2010': 8, '31 Dec 2010': x,
        '10 Jan 2011': 0, '22 Feb 2011': x, '05 Mar 2011': x, '07 Mar 2011': 0,
        '02 May 2011': 0, '13 Jun 2011': 0, '03 Nov 2011': x,
        '09 Jan 2012': 0, '22 Feb 2012': x, '07 Mar 2012': x, '09 Mar 2012': 0,
        '11 Mar 2012': 8, '28 Apr 2012': x, '30 Apr 2012': 0, '05 May 2012': 8,
        '07 May 2012': 0, '08 May 2012': 0, '12 May 2012': x, '09 Jun 2012': x,
        '11 Jun 2012': 0, '05 Nov 2012': 0, '29 Dec 2012': x, '31 Dec 2012': 0,
        '08 Jan 2013': 0, '22 Feb 2013': x, '07 Mar 2013': x, '30 Apr 2013': x,
        '02 May 2013': 0, '03 May 2013': 0, '08 May 2013': x, '10 May 2013': 0,
        '11 Jun 2013': x, '31 Dec 2013': x,
        '08 Jan 2014': 0, '24 Feb 2014': x, '07 Mar 2014': x, '10 Mar 2014': 0,
        '30 Apr 2014': x, '02 May 2014': 0, '08 May 2014': x, '11 Jun 2014': x,
        '13 Jun 2014': 0, '03 Nov 2014': 0, '31 Dec 2014': x,
        '08 Jan 2015': 0, '09 Jan 2015': 0, '09 Mar 2015': 0, '30 Apr 2015': x,
        '04 May 2015': 0, '08 May 2015': x, '11 May 2015': 0, '11 Jun 2015': x,
        '03 Nov 2015': x, '31 Dec 2015': x,
        '08 Jan 2016': 0, '20 Feb 2016': x, '22 Feb 2016': 0, '07 Mar 2016': 0,
        '02 May 2016': 0, '03 May 2016': 0, '13 Jun 2016': 0, '03 Nov 2016': x,
        '22 Feb 2017': x, '24 Feb 2017': 0, '07 Mar 2017': x, '08 May 2017': 0,
        '03 Nov 2017': x, '06 Nov 2017': 0,
        '08 Jan 2018': 0, '22 Feb 2018': x, '07 Mar 2018': x, '09 Mar 2018': 0,
        '28 Apr 2018': x, '30 Apr 2018': 0, '02 May 2018': 0, '08 May 2018': x,
        '09 Jun 2018': x, '11 Jun 2018': 0, '05 Nov 2018': 0, '29 Dec 2018': x,
        '31 Dec 2018': 0
    }


class Week8x5(CalendarBase):

    @classmethod
    def parameters(cls):
        return {
            'base_unit_freq': 'D',
            'start': get_timestamp('01 Jan 2005'),
            'end': get_timestamp('31 Dec 2018'),
            'layout': Organizer(split_by='W', structure=[[8, 8, 8, 8, 8, 0, 0]])
        }

    @classmethod
    def amendments(cls, custom_start=None, custom_end=None,
                   custom_amendments=None,
                   work_on_dec31=True, short_eves=True):

        start, end = cls._get_bounds(custom_start, custom_end)

        if short_eves:
            eve_hours = 7
        else:
            eve_hours = 8
        result = changes(eve_hours)
        result.update(holidays(start.year, end.year, work_on_dec31))
        result = {k: v for k, v in result.items()
                      if start <= get_timestamp(k) <= end}
        if custom_amendments is not None:
            result.update(custom_amendments)

        return result