from Command import Command
from MyUtils import MyUtils
from ..fanucpy_extended.src.fanucpy import Robot

class CommandExecutor:
    
    def __init__(self, robot: Robot) -> None:
        self.robot = robot

    def execute(self, command: Command):
        print(command)
