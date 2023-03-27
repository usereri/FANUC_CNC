import logging
from Command import Command
from MyUtils import MyUtils
from submodules.fanucpy_extended import Robot

class CommandExecutor:

    dryRun: bool = True
    
    def __init__(self, robot: Robot) -> None:
        self.robot = robot

    
    def _handleGCommand(self, command: Command):
        match command.command_no:
            case 0:
                logging.info("G0 - Fast move (quasilinear)")
                pass
            case 1:
                logging.info("G1 - Linear move")
                pass
            case 2:
                logging.info("G2 - Circular move CW")
                pass
            case 3:
                logging.info("G3 - Circular move CCW")
                pass
            case other:
                logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
                pass

    def _handleTCommand(self, command: Command):
        if command.command_no < 0:
            logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
            return
        logging.info(f"T{str(command.command_no)} - Load tool no.{str(command.command_no)}")


    def _handleMCommand(self, command: Command):
        match command.command_no:
            case 6:
                logging.info("M6 - Tool change")
            case other:
                logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
                pass

    def _handleSCommand(self, command: Command):
        if command.command_no < 0:
            logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
            return
        logging.info(f"S{str(command.command_no)} - Set speed to {str(command.command_no)}RPM")

    def execute(self, command: Command):
        match command.command_type:
            case 'G':
                self._handleGCommand(command)
            case 'T':
                self._handleTCommand(command)
            case 'M':
                self._handleMCommand(command)
            case 'S':
                self._handleSCommand(command)
            case other:
                logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")

