from FileReader import FileReader
from Command import Command
from MyUtils import MyUtils

class CommandProcessor:

    lastCommand: Command

    def __init__(self, path):
        self.fileReader = FileReader(path)

    def splitCommandNumber(self,line: str) -> tuple[int,str]:
        splited = line.split(" ", 1)
        no = splited[0]
        if no[0] != 'N':
            return (-1,"")
        return (int(no[1:]),splited[1])
    
    def _removeComments(self,command: str) -> list[str]:
        ret = []
        level = 0
        for elem in command.split(" "):
            if elem[0] == "(":
                level = level + 1
                continue
            if level > 0:     
                if elem[-1] == ")":
                    level = level - 1
                    assert(level >= 0)
                continue
            ret.append(elem)
        return ret
    
    def _groupCommands(self,commands: list[str]) -> list[list[str]]:
        groups = []
        actualGroup = []
        
        for elem in commands:
            if elem[0] in MyUtils.commandPrefix:
                if len(actualGroup) > 0:
                    groups.append(actualGroup.copy())
                actualGroup = [elem]
            else:
                actualGroup.append(elem)
        if len(actualGroup) > 0:
                    groups.append(actualGroup)
        return groups

    def _handleCommand(self, commandAndParam: list[str]):
        command = Command()
        command.params = {}
        command.command_type = commandAndParam[0][0]
        if not command.command_type in MyUtils.commandPrefix :
            command = self.lastCommand
        else:    
            command.command_no = int(commandAndParam[0][1:])
            commandAndParam.pop(0)
        for elem in commandAndParam:
            param_type = elem[0]
            param_val = float(elem[1:])
            command.params[param_type] = param_val
        if command.command_type == "G" and command.command_no in [0,1,2,3]:
            self.lastCommand = command.copy()
        return command
        
    def nextCommand(self) -> tuple[int,list[Command]]:
        no = -1
        command = ""
        while no < 0:
            line = self.fileReader.yieldLine()
            if line == "":
                return (-1, [])
            no, command = self.splitCommandNumber(line)
        commands = self._removeComments(command)
        commandsInGroup = self._groupCommands(commands)
        ret = []
        for elem in commandsInGroup:
            ret.append(self._handleCommand(elem))
        return (no,ret)

    def __del__(self) -> None:
        pass