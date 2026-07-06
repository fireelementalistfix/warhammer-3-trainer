namespace Warhammer3Trainer;

public class Menu
{
    private readonly TrainerEngine _trainer;

    public Menu(TrainerEngine trainer)
    {
        _trainer = trainer;
    }

    public void Run()
    {
        while (true)
        {
            Console.WriteLine("\n--- Trainer Menu ---");
            Console.WriteLine("1. Set Gold (99999)");
            Console.WriteLine("2. Set Influence (99999)");
            Console.WriteLine("3. Toggle Unlimited Movement");
            Console.WriteLine("4. Toggle God Mode");
            Console.WriteLine("5. Exit");
            Console.Write("> ");

            var input = Console.ReadLine();
            switch (input)
            {
                case "1":
                    _trainer.SetGold(99999);
                    break;
                case "2":
                    _trainer.SetInfluence(99999);
                    break;
                case "3":
                    _trainer.ToggleUnlimitedMovement();
                    break;
                case "4":
                    _trainer.ToggleGodMode();
                    break;
                case "5":
                    Console.WriteLine("Exiting...");
                    return;
                default:
                    Console.WriteLine("Invalid option.");
                    break;
            }
        }
    }
}