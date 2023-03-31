import logging
from CommandProcessor import CommandProcessor
from CommandExecutor import CommandExecutor
from submodules.fanucpy_extended import Robot
from time import sleep
import getch

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    robot = None
    # robot = Robot(
    #     robot_model="Fanuc",
    #     host="192.168.234.2",
    #     port=18735,
    # )
    # robot.connect()
    
    processor = CommandProcessor('test2.nc')
    executor = CommandExecutor(robot,True)

    no,commands = processor.nextCommand()
    while no >= 0:
        for command in commands:
            executor.execute(command)
        no,commands = processor.nextCommand()
    


            
