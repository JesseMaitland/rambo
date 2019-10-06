from rambo.terminal import provide_config
from rambo.config import load_config
from unittest.mock import MagicMock
from pathlib import Path


def test_provide_config():
    test_path = Path(__file__).absolute().parent / "fixtures" / "test_config.yml"
    test_config = load_config(test_path)

    mock_decorated_function = MagicMock()
    decorator = provide_config(test_path)
    wrapper = decorator(mock_decorated_function)
    wrapper()
    mock_decorated_function.assert_called_with(config=test_config)

