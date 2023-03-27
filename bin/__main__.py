from CommandProcessor import CommandProcessor
from CommandExecutor import CommandExecutor
from ..fanucpy_extended.src.fanucpy import Robot

if __name__ == "__main__":

    robot = Robot(
        robot_model="Fanuc",
        host="192.168.234.2",
        port=18735,
    )
    robot.connect()
    
    processor = CommandProcessor('test1.nc')
    executor = CommandExecutor(robot)

    no,commands = processor.nextCommand()
    while no >= 0:
        print(no)
        for command in commands:
            executor.execute(command)
        no,commands = processor.nextCommand()
            
