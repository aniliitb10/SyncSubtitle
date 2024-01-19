from datetime import datetime


class DateUtil:
    time_format = '%H:%M:%S,%f'
    time_stamp_sep = ' --> '

    @staticmethod
    def _assert_true(condition: bool, message: str) -> None:
        if not condition:
            raise ValueError(message)

    @classmethod
    def str_to_datetime(cls, time_str) -> datetime:
        return datetime.strptime(time_str, cls.time_format)

    @classmethod
    def datetime_to_str(cls, time_stamp: datetime) -> str:
        return time_stamp.strftime(cls.time_format)[:-3]  # dump first 3 digits only

    @classmethod
    def parse_time_line(cls, line: str) -> tuple[datetime, datetime]:
        date_strings = line.split(cls.time_stamp_sep)
        cls._assert_true(len(date_strings) == 2, f'Invalid time formats: {line}')
        return cls.str_to_datetime(date_strings[0]), cls.str_to_datetime(date_strings[1])

    @classmethod
    def to_time_line(cls, time_stamps: list[datetime]) -> str:
        return cls.time_stamp_sep.join([cls.datetime_to_str(time_stamp) for time_stamp in time_stamps])
