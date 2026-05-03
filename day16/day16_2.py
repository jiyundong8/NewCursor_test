import sys, os, hashlib, time, datetime, re

# ---- 1. 复用第12天的 qytang_multicmd ----
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day12_1 import qytang_multicmd  # noqa: E402

raw = qytang_multicmd(
    '10.10.1.1',
    'admin',
    'Cisco123',
    ['terminal length 0', 'show running-config'],
    verbose=True   # 👈 一定要开
)

print("RESULT:", raw)