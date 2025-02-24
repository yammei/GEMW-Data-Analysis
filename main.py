from scripts.update import Update
from scripts.calculate import Calculate

update = Update()
calculate = Calculate()

def main() -> None:
    print(f"Enter item name or id: ")
    item_identifier = input()
    update.past90Days(item_name=item_identifier)
    calculate.trends(identifier=item_identifier)

if __name__ == "__main__":
    main()