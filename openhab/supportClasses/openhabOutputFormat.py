

class OpenhabOutputFormat():
    def __init__(self, output_format: str):
        self.output_format = output_format

    def toString(self) -> str:
        return self.output_format
