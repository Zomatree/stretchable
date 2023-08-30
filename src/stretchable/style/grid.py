from enum import IntEnum
from typing import Self

from attrs import define, field, validators


class GridIndexType(IntEnum):
    AUTO = 0
    INDEX = 1
    SPAN = 2


@define(frozen=True)
class GridIndex:
    value: int = None
    span: bool = False

    # TODO: add validator

    @staticmethod
    def from_value(value: object) -> Self:
        # TODO: support more types of values
        if value is None:
            return GridIndex()
        elif isinstance(value, GridIndex):
            return value
        elif isinstance(value, int):
            return GridIndex(value)
        else:
            raise TypeError("Unsupported value type")

    @property
    def type(self) -> int:
        if self.value is None:
            return GridIndexType.AUTO
        elif self.span:
            return GridIndexType.SPAN
        else:
            return GridIndexType.INDEX

    def to_taffy(self) -> dict[str, int]:
        return dict(
            kind=self.type.value,
            value=self.value,
        )


@define(frozen=True)
class GridPlacement:
    start: GridIndex = field(
        default=None,
        converter=GridIndex.from_value,
        validator=[validators.optional(validators.instance_of(GridIndex))],
    )
    end: GridIndex = field(
        default=None,
        converter=GridIndex.from_value,
        validator=[validators.optional(validators.instance_of(GridIndex))],
    )

    @staticmethod
    def from_value(value: object) -> Self:
        # TODO: support more types of values
        if value is None:
            return GridPlacement()
        elif isinstance(value, GridPlacement):
            return value
        else:
            raise TypeError("Unsupported value type")

    def to_taffy(self) -> dict[str, int]:
        print(self.start)
        print(self.start.to_taffy())
        print(self.end)
        print(self.end.to_taffy())
        return dict(
            start=self.start.to_taffy(),
            end=self.end.to_taffy(),
        )
