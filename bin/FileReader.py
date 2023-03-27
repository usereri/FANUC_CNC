class FileReader:

    def __init__(self, path):
        self.filepath = path
        self.file = open(path,"r")

    def yieldLine(self) -> str:
        while(True):
            line = self.file.readline()
            if not self._valid(line):
                return ""
            line = line[:-1]
            if(len(line) > 0):
                return line
            
    def _valid(self, line) -> bool:
        if not line:
            return False
        return True

    def __del__(self) -> None:
        self.file.close()