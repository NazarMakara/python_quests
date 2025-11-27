from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict, Any
from operator import attrgetter

@dataclass(order=True)
class Item:
    sort_key: tuple = field(init=False, repr=False)
    name: str
    category: str
    quantity: int
    value: float
    condition: str
    location: str
    date_added: date = field(default_factory=date.today)

    def __post_init__(self):
        self.sort_key = (self.category, self.value)
        self.quantity = int(self.quantity)
        self.value = float(self.value)

    def total_value(self):
        return self.quantity * self.value

    def __str__(self):
        return f"[{self.category}] {self.name} ({self.quantity} pcs) | {self.value:.2f} UAH | {self.condition}"

@dataclass
class Inventory:
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item):
        self.items.append(item)

    def total_inventory_value(self):
        return sum(item.total_value() for item in self.items)
    
    def export_summary(self):
        summary: Dict[str, int] = {}
        for item in self.items:
            summary[item.category] = summary.get(item.category, 0) + item.quantity
        return summary

    def filter_and_sort(self, filters: Dict[str, Any] = None, sort_by: str = 'category'):
        filtered_items = self.items
        if filters:
            for k, v in filters.items():
                if hasattr(Item, k):
                    filtered_items = [i for i in filtered_items if str(getattr(i, k)).lower() == str(v).lower()]
        
        if hasattr(Item, sort_by):
            if sort_by == 'sort_key':
                return sorted(filtered_items, key=attrgetter('sort_key'))
            return sorted(filtered_items, key=attrgetter(sort_by))
        return filtered_items

if __name__ == '__main__':
    inv = Inventory()
    inv.add_item(Item("Crowbar", "scrap metal", 5, 25.00, "used", "shed"))
    inv.add_item(Item("Soldering Iron", "electronics", 1, 150.50, "new", "garage"))
    inv.add_item(Item("Pliers", "tools", 2, 85.99, "used", "garage"))
    inv.add_item(Item("USB Hub", "electronics", 3, 40.00, "broken", "pantry"))
    
    print("--- INVENTORY LIST ---")
    sorted_items = inv.filter_and_sort(sort_by='sort_key')
    for item in sorted_items:
        print(item)
    
    print("--- TOTAL ---")
    print(f"Total Value: {inv.total_inventory_value():.2f} UAH")
    
    print("--- SUMMARY ---")
    print(inv.export_summary())
    
    print("--- FILTER: NEW ---")
    filtered = inv.filter_and_sort(filters={'condition': 'new'}, sort_by='name')
    for item in filtered:
        print(item)