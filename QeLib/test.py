from QeLib.QeBaseClass import QeBaseClass


class ExampleClass(QeBaseClass):
    def __init__(self) -> None:
        super().__init__()
        self.data = self.LUMBERTYPES.CLS
        print(self.data)


ExampleClass()
