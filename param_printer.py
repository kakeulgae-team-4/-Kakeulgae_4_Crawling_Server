class ParamPrinter:
    @staticmethod
    def print_class_params(obj):
        for key, value in obj.__dict__.items():
            print(f"{str(key)[7:]}: {value}")
        print()

    @staticmethod
    def log_class_param(logger, obj, *args):
        message = f'{args[0]}'
        for key, value in obj.__dict__.items():
            message += f"{str(key)[7:]}: {value}"
            message += ' '
        logger.log(message)
