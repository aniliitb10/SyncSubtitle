from __future__ import annotations

from srt.displayed_line import DisplayedLine


class SubtitleMain:
    def __init__(self, source: str):
        self.source = source
        self.displayed_lines: list[DisplayedLine] = []

        with open(self.source) as file:
            self._lines = file.read().splitlines()

        # if last line is not empty, insert an empty line to ensure further processing is smooth
        if self._lines[-1]:
            self._lines.append('')

        start_index: int = 0
        for index, line in enumerate(self._lines):
            if not line:
                relevant_lines: list[str] = self._lines[start_index:index]
                if len(relevant_lines) < 3:
                    raise ValueError(f'Invalid format in: [{relevant_lines}]')

                self.displayed_lines.append(DisplayedLine.instance(relevant_lines))
                start_index = index + 1

    def sync_by_seconds(self, seconds: float) -> SubtitleMain:
        """
        This method is the while purpose of this project, rest are just helpers
        :param seconds: positive/negative float representing the seconds to delay / hasten by
        :return: None, just updates internal time stamps
        """
        for displayed_line in self.displayed_lines:
            displayed_line.sync_by_seconds(seconds)

        return self  # to enable chaining

    def to_file(self, filename: str):
        with open(filename, 'w') as file:
            for displayed_line in self.displayed_lines:
                file.write(str(displayed_line))


if __name__ == '__main__':
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-i", "--input", required=True, help="The input file path")
    arg_parser.add_argument("-o", "--output", required=True, help="The output file path")
    arg_parser.add_argument("-s", "--sync", required=True, help="+/- seconds to delay / hasten by", type=float)

    args = arg_parser.parse_args()
    if args.sync != 0:
        SubtitleMain(args.input).sync_by_seconds(args.sync).to_file(args.output)
        print(f'Output file [{args.output}] has been [{"delayed" if args.sync > 0 else "hastened"}] '
              f'by [{abs(args.sync)}] seconds')
