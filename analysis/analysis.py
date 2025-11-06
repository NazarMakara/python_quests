import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def analyze_supplies(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено: {file_path}")
        return
    
    df['total_price'] = df['quantity'] * df['price_per_unit']

    avg_price = np.mean(df['price_per_unit'])
    median_quantity = np.median(df['quantity'])
    std_dev_price = np.std(df['price_per_unit'])

    supplier_profit = df.groupby('supplier')['total_price'].sum()
    best_supplier = supplier_profit.idxmax()
    max_profit = supplier_profit.max()
    
    category_summary = df.groupby('category')['quantity'].sum().reset_index()

    low_supply_file_name = 'low_supply.csv'
    low_supply_df = df[df['quantity'] < 100].copy()
    low_supply_df.to_csv(low_supply_file_name, index=False)

    df_sorted = df.sort_values(by='total_price', ascending=False)
    
    print("\n--- Топ-3 поставок за загальною вартістю ---")
    print(df_sorted[['supplier', 'category', 'total_price']].head(3).to_string(index=False))

    report_file_name = 'report.txt'
    report_content = f"""
Звіт про Аналіз Поставок

1. Середні Показники:
   - Середня ціна: {avg_price:.2f}
   - Медіана кількості: {median_quantity:.0f}
   - Стандартне відхилення ціни: {std_dev_price:.2f}

2. Постачальник з Найбільшим Прибутком:
   - {best_supplier} (Прибуток: {max_profit:.2f})

3. Файл з Дефіцитними Поставками (quantity < 100):
   - {low_supply_file_name}
"""
    with open(report_file_name, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"Звіт збережено у: {report_file_name}")
    print(f"Файл низьких запасів збережено у: {low_supply_file_name}")

    plt.figure(figsize=(10, 6))
    plt.bar(category_summary['category'], category_summary['quantity'])
    plt.title('Розподіл КІлькості за Категоріями')
    plt.xlabel('Категорія')
    plt.ylabel('Сумарна Кількість')
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', type=str, nargs='?', 
                        default='supplies.csv') 
    
    args = parser.parse_args()
    analyze_supplies(args.csv_file)