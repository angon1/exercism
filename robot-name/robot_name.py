import random, string

class RobotsList:
    __robot_list = set()

    @classmethod
    def get_list(cls):
        return cls.__robot_list

    @classmethod
    def add_robot_to_list(cls, name):
        if name in cls.__robot_list:
            return False
        else:
            cls.__robot_list.add(name)
            return True

    @classmethod
    def remove_robot_from_list(cls, name):
        if name in cls.__robot_list:
            cls.__robot_list.remove(name)
            return True
        else:
            return False

class RobotNameGenerator:

    @classmethod
    def generate_name(cls):
        random.seed()
        return ''.join(cls.__random_letters() + cls.__random_digits())

    @staticmethod
    def __random_letters():
        return ''.join(random.choices(string.ascii_uppercase,k=2))

    @staticmethod
    def __random_digits():
        return ''.join(random.choices(string.digits,k=3))


class RobotFactory:

    @staticmethod
    def build_robot():
        new_robot_name = RobotNameGenerator.generate_name()
        while RobotsList.add_robot_to_list(new_robot_name) is False:
            new_robot_name = RobotNameGenerator.generate_name()
        return new_robot_name

class Robot:
    def __init__(self):
        self.name = RobotFactory.build_robot()

    def reset(self):
        if RobotsList.remove_robot_from_list(self.name) is True:
            self.name = RobotFactory.build_robot()
            return True
        else:
            return False
