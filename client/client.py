clients = [
    {"ім’я": "Іван", "сума угоди": 50, "статус перевірки": "clean"},
    {"ім’я": "Оля", "сума угоди": 550, "статус перевірки": "suspicious"},
    {"ім’я": "Петро", "сума угоди": 2000, "статус перевірки": "fraud"},
    {"ім’я": "Марія", "сума угоди": "?", "статус перевірки": "clean"},
    {"ім’я": "Андрій", "сума угоди": 800, "статус перевірки": "unknown"}
]

result = []

for client in clients:
    name = client["name"]
    amount = client["deal_amount"]
    status = client["status"]

    if not isinstance(amount, (int, float)):
        category = "Invalid data"
        decision = "—"
    else:
        if amount < 100:
            category = "Small client"
        elif amount < 1000:
            category = "Medium client"
        else:
            category = "Big client"

        match status:
            case "clean":
                decision = "Proceed without issues"
            case "suspicious":
                decision = "Check documents"
            case "fraud":
                decision = "Blacklist"
            case _:
                decision = "Unknown status"

    result.append(f"{name}: {category} → {decision}")

for i in result:
    print(i)