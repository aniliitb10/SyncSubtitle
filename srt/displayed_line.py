from __future__ import annotations

from datetime import timedelta, datetime

from pydantic import BaseModel

from srt.dateutil import DateUtil


class DisplayedLine(BaseModel):
    line_id: int
    begin_time: datetime
    end_time: datetime
    lines: list[str]

    def sync_by_seconds(self, seconds: float):
        """
        This method is the while purpose of this project, rest are just helpers
        :param seconds: positive/negative float representing the seconds to delay / hasten by
        :return: None, just updates internal time stamps
        """
        self.begin_time = self.begin_time + timedelta(milliseconds=int(seconds * 1000))
        self.end_time += timedelta(milliseconds=int(seconds * 1000))

    @staticmethod
    def instance(source: list[str]) -> DisplayedLine:
        begin_time, end_time = DateUtil.parse_time_line(source[1])
        return DisplayedLine(
            line_id=int(source[0]),
            begin_time=begin_time,
            end_time=end_time,
            lines=source[2:]
        )

    def __str__(self):
        lines = '\n'.join(self.lines)
        return (f"{self.line_id}\n"
                f"{DateUtil.to_time_line([self.begin_time, self.end_time])}\n"
                f"{lines}\n\n")
