class Detector:

    def __init__(self, rules):
        self.rules = rules

    def detect_suspicious_processes(self, process_list):
        suspicious = []

        for proc in process_list:
            pname = proc["name"].lower()

            for rule in self.rules.get("suspicious_processes", []):
                if rule.lower() in pname:
                    suspicious.append(f"Processo suspeito encontrado: {pname} (PID: {proc['pid']})")

        return suspicious
