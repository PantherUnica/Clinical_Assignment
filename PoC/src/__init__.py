"""VetAI PoC pipeline package.

Importing anything from this package puts the PoC root on sys.path so that
`import config` works from scripts, the notebook and the Streamlit app alike.
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
