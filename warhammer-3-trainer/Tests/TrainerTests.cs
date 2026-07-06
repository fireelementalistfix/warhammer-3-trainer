using Xunit;
using Moq;
using Warhammer3Trainer.Core;

namespace Warhammer3Trainer.Tests;

public class TrainerTests
{
    [Fact]
    public void SetGold_WritesCorrectBytes()
    {
        var mockGame = new Mock<GameProcess>();
        var trainer = new TrainerEngine(mockGame.Object);

        trainer.SetGold(50000);

        // Verify that WriteBytes was called with expected address and value
        mockGame.Verify(g => g.WriteBytes(0x00A3F1B0, It.Is<byte[]>(b => BitConverter.ToInt32(b) == 50000)), Times.Once);
    }

    [Fact]
    public void ToggleUnlimitedMovement_FlipsState()
    {
        var mockGame = new Mock<GameProcess>();
        var trainer = new TrainerEngine(mockGame.Object);

        trainer.ToggleUnlimitedMovement();
        trainer.ToggleUnlimitedMovement();

        // First call writes 0x01, second writes 0x00
        mockGame.Verify(g => g.WriteBytes(0x00B2A400, new byte[] { 0x01 }), Times.Once);
        mockGame.Verify(g => g.WriteBytes(0x00B2A400, new byte[] { 0x00 }), Times.Once);
    }
}