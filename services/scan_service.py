import json
import psutil
from config import Config
from services.logger_service import LoggerService

class ScanService:
    def __init__(self):
        self.logger = LoggerService()
        self.rules = self.load_rules()

    def load_rules(self):
        try:
            with open(Config.SIGNATURE_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            self.logger.log(f"Erro ao carregar regras: {e}")
            return {"suspicious_processes": []}

    def check_processes(self):
        suspicious = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pname = proc.info['name'].lower()
                for rule in self.rules.get("suspicious_processes", []):
                    if rule.lower() in pname:
                        suspicious.append(f"Processo suspeito encontrado: {pname} (PID: {proc.pid})")
            except Exception:
                continue
        return suspicious

    def run_scan(self):
        self.logger.log("Iniciando escaneamento...")

        findings = self.check_processes()

        if findings:
            for f in findings:
                self.logger.log(f)
            return f"⚠️ Foram encontrados {len(findings)} possíveis keyloggers!"
        else:
            self.logger.log("Nenhuma ameaça encontrada.")
            return "✔️ Nenhum keylogger detectado."
