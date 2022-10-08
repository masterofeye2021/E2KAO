from openhab.items.item import OpenhabItem


class Persistence ():
    def __init__(self) -> None:
        self.file = "export/influxdb.persist"
        self.pid = None
        self.delimiter = " "
        pass

    def write_persisence(self, items: dict):
        self.write_start()
        self.write_starter()
                
        self.pid.write("Items {\n")
        for i in items.values() :
            self.write_items(i)
        self.pid.write("\n: strategy = everyChange, restoreOnStartup\n")
        self.pid.write("}")
        self.write_stop()

    def write_start(self):
        self.pid = open(self.file, 'w',encoding="utf-8")

    def write_starter(self):
        self.pid.write("Strategies {\n")
        self.pid.write("    everyHour : \"0 0 * * * ?\"\n")
        self.pid.write("    everyDay  : \"0 0 0 * * ?\"\n")
        self.pid.write("    // if no strategy is specified for an Item entry below, the default list will be used\n")
        self.pid.write("    default = everyChange\n")
        self.pid.write("}\n")

    def write_items(self, items):
        first = False
        for i in items:
            if i.persistence :
                if first :
                    self.pid.write(",")
                self.pid.write("\n\t" +i.name)
                first = True

    def write_stop(self):
        self.pid.close()