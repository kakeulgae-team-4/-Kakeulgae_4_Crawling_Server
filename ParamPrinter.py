class ParamPrinter:
    @staticmethod
    def print_class_params(obj):
        for key, value in obj.__dict__.items():
            print(f"{str(key)[7:]}: {value}")
        print()