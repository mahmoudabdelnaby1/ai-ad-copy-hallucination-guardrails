import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from copy_guardrails import validate_ad_copy

class TestGuardrails(unittest.TestCase):
    def test_val(self):
        c = Path(__file__).resolve().parent.parent / "examples" / "unreviewed_ad_copy_sample.csv"
        b = Path(__file__).resolve().parent.parent / "config" / "authorized_offer_bounds.sample.json"
        o = Path(__file__).resolve().parent.parent / "reports" / "flagged_claims_report.csv"
        count = validate_ad_copy(str(c), str(b), str(o))
        self.assertGreaterEqual(count, 1)

if __name__ == "__main__":
    unittest.main()
