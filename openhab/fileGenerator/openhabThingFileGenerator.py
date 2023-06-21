from openhab.fileGenerator.fileGenerator import FileGenerator


class OpenhabThingFileGenerator(FileGenerator):
    item_file_extention = ".things"
    item_file_deliminiter = " "

    def __init__(self, output_dir: str, file_name: str) -> None:
        super().__init__(output_dir, file_name)

    def generate(self) -> str:
        self.item_file = open(self.output_dir + "/" +
                              self.file_name + self.item_file_extention, "w",encoding="utf-8")
