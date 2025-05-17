from database import init_db, get_computers_by_room
from report import generate_report

def main():
    init_db()
    
    try:
        room_id = int(input("Введите ID помещения: "))
    except ValueError:
        print("Ошибка: введите число")
        return
    
    computers, room_name = get_computers_by_room(room_id)
    
    if not computers:
        print(f"В помещении {room_name or 'с таким ID'} нет компьютеров")
        return
    
    print(f"\nКомпьютеры в помещении '{room_name}':")
    print("ID | Дата покупки   | Цена     |")
    print("-"*30)
    for comp in computers:
        print(f"{comp[0]:2} | {comp[1]:14} | {comp[2]:8.2f} |")
    
    generate_report(computers, room_name)
    print("\nОтчет сохранен в файл 'computers_report.txt'")

if __name__ == "__main__":
    main()