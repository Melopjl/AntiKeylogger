import os

class Config:
    DEBUG = True
    LOG_PATH = os.path.join("logs", "scanner.log")
    SIGNATURE_FILE = os.path.join("scanner", "signatures", "keylogger_rules.json")
    SCAN_INTERVAL = 300  # segundos
