
class OpenhabGeneric:
    def __set_group__(group1:str,group2:str,group3:str,group4:str):
        group = ""

        if group1:
            group += "g" + group1 + ","
        
        if group2:
            group += "g" + group2 + ","
        
        if group3:
            group += "g" + group3 + ","
        
        if group4:
            group += "g" + group4 + ","

        if group.endswith(","):
            group = group.removesuffix(",")

        return group 