from typing import Optional

import rich


class TerminalUtility(object):
    class Style:
        Normal = None
        Info = "green"
        Warning = "yellow"
        Error = "bold red"
        Header = "bold green"

    def __init__(self):
        self._console = rich.get_console()

    def print(self,
              message: str,
              new_line=True,
              style: Optional[str] = Style.Normal):
        end = "\n" if new_line else ""
        self._console.print(message, style=style, end=end)
