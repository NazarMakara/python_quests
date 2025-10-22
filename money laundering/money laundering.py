def shadow(limit=200):
    def decorator(func):
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            total = 0.0
            for item in gen:
                try:
                    parts = item.split()
                    if len(parts) != 2:
                        continue
                    action, amount_str = parts
                    if action not in ('payment', 'refund', 'transfer'):
                        continue
                    amount = float(amount_str)
                    if action == 'refund':
                        amount = -amount
                    total += amount
                    if total > limit:
                        print("Тіньовий ліміт перевищено. Активую схему")
                    print(item)
                    yield item
                except ValueError:
                    continue
            yield total 
        return wrapper
    return decorator


@shadow(limit=200)
def transactions():
    yield "payment 120"
    yield "refund 50"
    yield "invalid line"
    yield "transfer 300"
    yield "bad abc"
    yield "payment 100"
print(list(transactions()))