import datetime

class AuditAgent:
    def log(self, message):
        time = str(datetime.datetime.now())

        with open("logs/audit_log.json", "a") as file:
            file.write(f"{time} : {message}\n")