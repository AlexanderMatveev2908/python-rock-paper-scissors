from typing import Literal, Optional, TypeVar


T = TypeVar("T")
Nullable = Optional[T]

WinnerT = Literal["CPU", "USER", "TIE"]
