import argparse
from .trainer import Warhammer3Trainer

def main():
    parser = argparse.ArgumentParser(description="Warhammer III Trainer")
    parser.add_argument("--money", type=int, help="Set money amount")
    args = parser.parse_args()

    trainer = Warhammer3Trainer()
    if not trainer.find_process():
        print("Warhammer III process not found!")
        return

    print("Warhammer III process found!")

    if args.money:
        if trainer.set_money(args.money):
            print(f"Money set to {args.money}!")
        else:
            print("Failed to set money.")

if __name__ == "__main__":
    main()