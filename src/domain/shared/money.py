# src/domain/shared/money.py

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class Currency:
    code: str

    def __post_init__(self) -> None:
        normalized = self.code.strip().upper()

        if len(normalized) != 3:
            raise ValueError("Currency code must contain exactly 3 characters.")

        object.__setattr__(self, "code", normalized)


EUR = Currency("EUR")


@dataclass(frozen=True)
class MoneyAmount:
    value: Decimal
    currency: Currency = EUR

    def __post_init__(self) -> None:
        value = Decimal(str(self.value))

        if value < Decimal("0"):
            raise ValueError("Money amount cannot be negative.")

        object.__setattr__(self, "value", value.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        ))

    @classmethod
    def zero(cls, currency: Currency = EUR) -> "MoneyAmount":
        return cls(Decimal("0"), currency)

    def add(self, other: "MoneyAmount") -> "MoneyAmount":
        self._ensure_same_currency(other)

        return MoneyAmount(
            self.value + other.value,
            self.currency,
        )

    def _ensure_same_currency(self, other: "MoneyAmount") -> None:
        if self.currency != other.currency:
            raise ValueError("Cannot operate on different currencies.")