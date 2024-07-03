from datetime import date, timedelta


class DateRangeIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


for day in DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5)):
    print(day)


# the issue with the above approach is that it uses StopIteration
# iterable will be empty and the end of the iteration
# and cannot be reused: ValueError: max() iterable argument is empty
r = DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5))
", ".join(map(str, r))
# max(r)


class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


for day in DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5)):
    print(day)
