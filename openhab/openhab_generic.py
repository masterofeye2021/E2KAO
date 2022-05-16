
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

    def __remove_umlaut__(string_umlaut):
      """
      Removes umlauts from strings and replaces them with the letter+e convention
      :param string: string to remove umlauts from
      :return: unumlauted string
      """
      u = 'ü'.encode()
      U = 'Ü'.encode()
      a = 'ä'.encode()
      A = 'Ä'.encode()
      o = 'ö'.encode()
      O = 'Ö'.encode()
      ss = 'ß'.encode()

      string_umlaut = string_umlaut.encode()
      string_umlaut = string_umlaut.replace(u, b'ue')
      string_umlaut = string_umlaut.replace(U, b'Ue')
      string_umlaut = string_umlaut.replace(a, b'ae')
      string_umlaut = string_umlaut.replace(A, b'Ae')
      string_umlaut = string_umlaut.replace(o, b'oe')
      string_umlaut = string_umlaut.replace(O, b'Oe')
      string_umlaut = string_umlaut.replace(ss, b'ss')

      string_umlaut = string_umlaut.decode('utf-8')
      return string_umlaut

