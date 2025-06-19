from unittest.mock import patch
import hivebox

def test_version_count():
    with patch("builtins.print") as mock_print:
        with patch("sys.exit") as mock_exit:
            hivebox.version_count()
            mock_print.assert_called_with("The Current Version Of The App Is : V0.0.1")
            mock_exit.assert_called_once()
