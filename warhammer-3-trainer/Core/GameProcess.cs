using System.Diagnostics;
using MemorySharp;

namespace Warhammer3Trainer.Core;

public class GameProcess : IDisposable
{
    private Process? _process;
    private SharpMemory? _memory;

    public bool Attach(string processName)
    {
        var processes = Process.GetProcessesByName(processName);
        if (processes.Length == 0)
            return false;

        _process = processes[0];
        _memory = new SharpMemory(_process.Id);
        return true;
    }

    public void WriteBytes(long address, byte[] data)
    {
        _memory?.WriteBytes((IntPtr)address, data);
    }

    public byte[] ReadBytes(long address, int count)
    {
        return _memory?.ReadBytes((IntPtr)address, count) ?? Array.Empty<byte>();
    }

    public void Dispose()
    {
        _memory?.Dispose();
        _process?.Dispose();
    }
}