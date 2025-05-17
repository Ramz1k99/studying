from datetime import datetime

def generate_report(computers, room_name, filename="computers_report.txt"):
    """Генерация отчета и сохранение в файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Отчет по компьютерам в помещении: {room_name}\n")
        file.write("="*50 + "\n")
        file.write("ID | Дата покупки   | Цена     |\n")
        file.write("-"*50 + "\n")
        
        for comp in computers:
            comp_id, date, price, _ = comp
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")
            file.write(f"{comp_id:2} | {date:14} | {price:8.2f} |\n")
        
        file.write("="*50 + "\n")
        file.write(f"Всего компьютеров: {len(computers)}\n")