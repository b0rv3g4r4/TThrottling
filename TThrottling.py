import rumps
import subprocess
import re
from decimal import Decimal

def get_pmset():
	return subprocess.check_output(['pmset', '-g', 'therm']).decode( "utf-8", "ignore")

def get_limit():
    output = get_pmset()
    limit = re.search(r"CPU_Speed_Limit\s*=\s*(\d+)", output)
    return limit.group(1)

def get_scheduler_limit():
    output = get_pmset()
    limit = re.search(r"CPU_Scheduler_Limit\s*=\s*(\d+)", output)
    return limit.group(1)   

def get_avaiable_cpus():
    output = get_pmset()
    limit = re.search(r"CPU_Available_CPUs\s*=\s*(\d+)", output)
    return limit.group(1) 

def get_cpu_temp():
     return subprocess.check_output(["./osx-cpu-temp"]).decode(
            "utf-8", "ignore"
        )[:5]


class TThrottling(object):
    def __init__(self):
        self.config = {
            "app_name": "TThrottling",
            "polling_freq": 5
        }
        self.menu = [
            rumps.MenuItem("About", self.about),
            "Preferences",
            None
        ]
        self.app = rumps.App(self.config["app_name"])
        self.app.menu = self.menu
        self.app.icon = "ok.png"
        self.timer = rumps.Timer(self.refresh_status, 2)
        self.timer.start()
    

    def refresh_status(self,sender):
        limit = get_limit()
        cpu_temp = get_cpu_temp()
        self.app.title = limit+"% | "+cpu_temp + "°"
        self.app.icon = "bad.png"
        if int(limit) >= 90:
            self.app.icon = "ok.png"
        elif int(limit) >= 60:
             self.app.icon = "medium.png"
        else:
             self.app.icon = "bad.png"
       

    def about(self, sender) -> None:
        rumps.alert(title='TThrottling',
                    message=(f"Version 0.0.1 - by J. B0RV3G4RA\n"
                              "URL\n"  # noqa: E127
                              "\n"
                              "Simple Menubar app to monitor thermal throttling\n"
                              "\n"
                              "Licensed under MIT.\n"
                              "rumps licensed under BSD 3-Clause.\n"
                              "Framework7 icons licensed under MIT\n"
                              ""),
                    ok=None, cancel=None)
    def run(self):
        self.app.run()

if __name__ == "__main__":
    app = TThrottling()
    app.run()
