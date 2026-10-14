"""Текстовый отчёт по заказам."""


def render_report(orders):
    """orders: список dict {id, customer, items: [(name, price_str, qty)], status}.
    Возвращает строку отчёта."""
    out = []
    out.append("ORDERS REPORT")
    out.append("=============")
    paid_count = 0
    paid_sum = 0.0
    pending_count = 0
    pending_sum = 0.0
    for o in orders:
        if o["status"] == "paid":
            s = 0.0
            for it in o["items"]:
                s = s + float(it[1]) * it[2]
            paid_count = paid_count + 1
            paid_sum = paid_sum + s
            out.append("#" + str(o["id"]) + " " + o["customer"] + " PAID " + "%.2f" % s)
        elif o["status"] == "pending":
            s = 0.0
            for it in o["items"]:
                s = s + float(it[1]) * it[2]
            pending_count = pending_count + 1
            pending_sum = pending_sum + s
            out.append("#" + str(o["id"]) + " " + o["customer"] + " PENDING " + "%.2f" % s)
        else:
            s = 0.0
            for it in o["items"]:
                s = s + float(it[1]) * it[2]
            out.append("#" + str(o["id"]) + " " + o["customer"] + " " + o["status"].upper() + " " + "%.2f" % s)
    out.append("-------------")
    out.append("paid: " + str(paid_count) + " / " + "%.2f" % paid_sum)
    out.append("pending: " + str(pending_count) + " / " + "%.2f" % pending_sum)
    return "\n".join(out)
