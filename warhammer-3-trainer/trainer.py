import ctypes
import sys
import os
from typing import Optional

class Warhammer3Trainer:
    def __init__(self, process_name: str = "Warhammer3.exe"):
        self.process_name = process_name
        self.process_id: Optional[int] = None
        self.process_handle: Optional[int] = None
        self.base_address: Optional[int] = None

    def find_process(self) -> bool:
        """Find the Warhammer III process by name."""
        PROCESS_QUERY_INFORMATION = 0x0400
        PROCESS_VM_READ = 0x0010
        PROCESS_VM_WRITE = 0x0020
        PROCESS_VM_OPERATION = 0x0008

        snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(0x2, 0)
        if snapshot == -1:
            return False

        process_entry = ctypes.create_string_buffer(1024)
        process_entry.dwSize = ctypes.sizeof(process_entry)

        if not ctypes.windll.kernel32.Process32First(snapshot, ctypes.byref(process_entry)):
            ctypes.windll.kernel32.CloseHandle(snapshot)
            return False

        while True:
            if process_entry.szExeFile.decode('utf-8').lower() == self.process_name.lower():
                self.process_id = process_entry.th32ProcessID
                self.process_handle = ctypes.windll.kernel32.OpenProcess(
                    PROCESS_QUERY_INFORMATION | PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION,
                    False,
                    self.process_id
                )
                ctypes.windll.kernel32.CloseHandle(snapshot)
                return True

            if not ctypes.windll.kernel32.Process32Next(snapshot, ctypes.byref(process_entry)):
                break

        ctypes.windll.kernel32.CloseHandle(snapshot)
        return False

    def read_memory(self, address: int, size: int = 4) -> Optional[int]:
        """Read memory from the process."""
        if not self.process_handle:
            return None

        buffer = ctypes.create_string_buffer(size)
        bytes_read = ctypes.c_size_t()

        if ctypes.windll.kernel32.ReadProcessMemory(
            self.process_handle,
            address,
            buffer,
            size,
            ctypes.byref(bytes_read)
        ):
            return int.from_bytes(buffer.raw, byteorder='little')
        return None

    def write_memory(self, address: int, value: int, size: int = 4) -> bool:
        """Write memory to the process."""
        if not self.process_handle:
            return False

        buffer = ctypes.create_string_buffer(value.to_bytes(size, byteorder='little'))
        bytes_written = ctypes.c_size_t()

        return ctypes.windll.kernel32.WriteProcessMemory(
            self.process_handle,
            address,
            buffer,
            size,
            ctypes.byref(bytes_written)
        ) != 0

    def set_money(self, amount: int = 999999) -> bool:
        """Set money to the specified amount."""
        if not self.base_address:
            module_snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(0x8, self.process_id)
            if module_snapshot == -1:
                return False

            module_entry = ctypes.create_string_buffer(1024)
            module_entry.dwSize = ctypes.sizeof(module_entry)

            if not ctypes.windll.kernel32.Module32First(module_snapshot, ctypes.byref(module_entry)):
                ctypes.windll.kernel32.CloseHandle(module_snapshot)
                return False

            while True:
                if module_entry.szModule.decode('utf-8').lower() == self.process_name.lower():
                    self.base_address = module_entry.modBaseAddr
                    break

                if not ctypes.windll.kernel32.Module32Next(module_snapshot, ctypes.byref(module_entry)):
                    break

            ctypes.windll.kernel32.CloseHandle(module_snapshot)

        if not self.base_address:
            return False

        # Example offset (this would need to be found via Cheat Engine or similar)
        money_offset = 0x01A3F8D0
        money_address = self.base_address + money_offset

        return self.write_memory(money_address, amount)