using Warhammer3Trainer.Core;

namespace Warhammer3Trainer;

public class TrainerEngine
{
    private readonly GameProcess _game;
    private bool _unlimitedMovement;
    private bool _godMode;

    public TrainerEngine(GameProcess game)
    {
        _game = game;
    }

    public void SetGold(int amount)
    {
        // Example offset for player gold (static pointer)
        long goldAddress = 0x00A3F1B0;
        byte[] goldBytes = BitConverter.GetBytes(amount);
        _game.WriteBytes(goldAddress, goldBytes);
        Console.WriteLine($"Gold set to {amount}");
    }

    public void SetInfluence(int amount)
    {
        long influenceAddress = 0x00A3F1C0;
        byte[] influenceBytes = BitConverter.GetBytes(amount);
        _game.WriteBytes(influenceAddress, influenceBytes);
        Console.WriteLine($"Influence set to {amount}");
    }

    public void ToggleUnlimitedMovement()
    {
        _unlimitedMovement = !_unlimitedMovement;
        long movementAddress = 0x00B2A400;
        byte[] value = _unlimitedMovement ? new byte[] { 0x01 } : new byte[] { 0x00 };
        _game.WriteBytes(movementAddress, value);
        Console.WriteLine($"Unlimited movement: {(_unlimitedMovement ? "ON" : "OFF")}");
    }

    public void ToggleGodMode()
    {
        _godMode = !_godMode;
        long godAddress = 0x00B2A410;
        byte[] value = _godMode ? new byte[] { 0x01 } : new byte[] { 0x00 };
        _game.WriteBytes(godAddress, value);
        Console.WriteLine($"God mode: {(_godMode ? "ON" : "OFF")}");
    }
}