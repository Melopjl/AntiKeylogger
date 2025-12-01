import psutil

class Monitor:

    def list_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pname = proc.info['name']
                pid = proc.info['pid']
                processes.append({"name": pname, "pid": pid})
            except:
                continue
        return processes
