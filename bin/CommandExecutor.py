import logging
from Command import Command
from MyUtils import MyUtils
from submodules.fanucpy_extended import Robot
from Visualization import Visualization


class CommandExecutor:

    dryRun: bool = True
    
    def __init__(self, robot: Robot | None) -> None:
        self.robot = robot
        if self.robot == None:
            self.dryRun = True
        self.visualization = Visualization()
        self.curPos = [0,0,0]
 
    def _handleGCommand(self, command: Command):
        match command.command_no:
            case 0:
                logging.info("G0 - Fast move (quasilinear)")
                self.curPos[0] = command.params.get("X",self.curPos[0])
                self.curPos[1] = command.params.get("Y",self.curPos[1])
                self.curPos[2] = command.params.get("Z",self.curPos[2])
                self.visualization.addPoint(self.curPos[0],self.curPos[1],self.curPos[2])
                pass
            case 1:
                logging.info("G1 - Linear move")
                self.curPos[0] = command.params.get("X",self.curPos[0])
                self.curPos[1] = command.params.get("Y",self.curPos[1])
                self.curPos[2] = command.params.get("Z",self.curPos[2])
                self.visualization.addPoint(self.curPos[0],self.curPos[1],self.curPos[2])
                pass
            case 2:
                logging.info("G2 - Circular move CW")
                pass
            case 3:
                logging.info("G3 - Circular move CCW")
                pass
            case 17:
                logging.info("G17 - XY Plane Selection")
                pass
            case 21:
                logging.info("G21 - Metric units convention")
                pass
            case 28:
                logging.info("G28 - Go home")
                pass
            #TODO: What is G40-G42
            case 40:
                logging.warn("G40 - ")
                pass
            case 41:
                logging.warn("G41 - ")
                pass
            case 43:
                logging.info("G43 - Tool length compensation")
                pass
            case 54:
                logging.info("G54 - Active Coordinate System")
                pass
            case 90:
                logging.info("G90 - Absolute positioning")
                pass
            case 91:
                logging.info("G91 - Incremental positioning")
                pass
            case other:
                logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
                pass

    def _handleTCommand(self, command: Command):
        if command.command_no < 0:
            logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
            return
        logging.info(f"T{str(command.command_no)} - Load tool no.{str(command.command_no)}")
        #TODO: handle tool changing


    def _handleMCommand(self, command: Command):
        match command.command_no:
            case 3:
                logging.info("M3 - Start spindle")
            case 6:
                logging.info("M6 - Tool change")
            case 8:
                logging.info("M8 - Turn on tool flood coolant")
            case 9:
                logging.info("M9 - Turn off coolant")
            case 30:
                logging.info("M30 - Program end")
            case other:
                logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
                pass

    def _handleSCommand(self, command: Command):
        if command.command_no < 0:
            logging.error(f"Unrecognize command!: {command.command_type} {str(command.command_no)}")
            return
        logging.info(f"S{str(command.command_no)} - Set speed to {str(command.command_no)}RPM")
        #TODO: control spindle

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

