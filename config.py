import os

# Demo mode is active by default. Set DEMO_MODE=false or DEMO_MODE=0 in your env to disable.
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() not in ("false", "0", "no", "off")

