import unittest
from unittest.mock import patch, MagicMock
from warhammer_3_trainer.trainer import Warhammer3Trainer

class TestWarhammer3Trainer(unittest.TestCase):
    @patch('ctypes.windll.kernel32')
    def test_find_process_success(self, mock_kernel32):
        trainer = Warhammer3Trainer()
        mock_kernel32.CreateToolhelp32Snapshot.return_value = 1
        mock_kernel32.Process32First.return_value = True
        mock_kernel32.Process32Next.return_value = False

        process_entry = MagicMock()
        process_entry.szExeFile = b"Warhammer3.exe"
        process_entry.th32ProcessID = 1234
        mock_kernel32.Process32First.return_value = True
        mock_kernel32.Process32First.side_effect = lambda *args: setattr(args[1], 'contents', process_entry)

        self.assertTrue(trainer.find_process())
        self.assertEqual(trainer.process_id, 1234)

    @patch('ctypes.windll.kernel32')
    def test_find_process_failure(self, mock_kernel32):
        trainer = Warhammer3Trainer()
        mock_kernel32.CreateToolhelp32Snapshot.return_value = 1
        mock_kernel32.Process32First.return_value = False

        self.assertFalse(trainer.find_process())

    @patch('ctypes.windll.kernel32')
    def test_write_memory_success(self, mock_kernel32):
        trainer = Warhammer3Trainer()
        trainer.process_handle = 1234
        mock_kernel32.WriteProcessMemory.return_value = 1

        self.assertTrue(trainer.write_memory(0x12345678, 999999))

if __name__ == "__main__":
    unittest.main()