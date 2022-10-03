
class OpenhabGeneric:
 

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

      if type(string_umlaut) == tuple:
        string_umlaut= string_umlaut[0]

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

