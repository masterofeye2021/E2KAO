class FileGenerator():

    def __init__(self,output_dir: str, file_name: str) -> None:
        self.output_dir = output_dir
        self.file_name = file_name
        pass

    def replaceUmlaute(self, item_file_extention:str) -> None:

        f = open(self.output_dir + "/" + self.file_name + item_file_extention, "r+", encoding="utf-8")
        temp = self.__replaceUmlaute__(f.read())
        f.close()
        
        f = open(self.output_dir + "/" + self.file_name + item_file_extention, "w", encoding="utf-8")
        f.write(temp)
        f.close()

    def __replaceUmlaute__(self,string: str) -> str:
            string = string.replace("ü", "ue")
            string = string.replace("Ü", "Ue")
            string = string.replace("ä", "ae")
            string = string.replace("Ä", "Ae")
            string = string.replace("ö", "oe")
            string = string.replace("Ö", "Oe")
            string = string.replace("ß", "ss")
            return string