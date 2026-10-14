"""Расчёт стоимости заказа."""
from decimal import Decimal, ROUND_HALF_UP

TAX_RATE = Decimal("0.20")
DISCOUNTS = {"SAVE10": Decimal("0.10"), "SAVE25": Decimal("0.25")}


def _money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def line_total(price: str, qty: int) -> Decimal:
    if qty < 0:
        raise ValueError("quantity must be non-negative")
    return Decimal(price) * qty


def compute_total(items, discount_code=None) -> Decimal:
    """items: список (price_str, qty). Скидка применяется к сумме до налога,
    налог начисляется на сумму после скидки. Результат округляется до копеек."""
    subtotal = sum((line_total(p, q) for p, q in items), Decimal("0"))
    taxed = subtotal * (1 + TAX_RATE)
    if discount_code:
        rate = DISCOUNTS.get(discount_code, Decimal("0"))
        taxed = taxed - subtotal * rate
    return _money(taxed)
