class Command:
    command_type: str
    command_no: int
    params: dict[str, int | float]

    def copy(self):
        c = Command()
        c.command_type = self.command_type
        c.command_no = self.command_no
        c.params = self.params.copy()
        return c
    
    def __str__(self) -> str:
        ret = self.command_type + " no:"  + str(self.command_no) + " Params: "
        for (K,V) in self.params.items():
            ret = ret + "K: "+ K + " V: " + str(V) + " "
        return ret



