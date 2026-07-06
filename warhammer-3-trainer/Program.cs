using Warhammer3Trainer.Core;

namespace Warhammer3Trainer;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("=== Warhammer III Trainer ===");
        Console.WriteLine("Waiting for game process...");

        var game = new GameProcess();
        if (!game.Attach("warhammer3"))
        {
            Console.WriteLine("Game not found. Start Total War: Warhammer III first.");
            return;
        }

        Console.WriteLine("Game attached. Use menu below.");

        var trainer = new TrainerEngine(game);
        var menu = new Menu(trainer);
        menu.Run();
    }
}