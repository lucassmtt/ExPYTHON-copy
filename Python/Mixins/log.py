from pathlib import Path
FILE_DIR = Path(__file__).parent

class Log:
    def log(self, msg):
        raise NotImplementedError(
            'Implemente o metodo log'
        )
    
    def log_error(self, msg):
        return print(f'ERROR, {msg}')

    def log_sucess(self, msg):
        return print(f'SUCESS {msg}')

class LogFileMixin(Log):
    def log(self, msg):
        print('MSG')

class LogPrintMixin(Log):
    def log(self, msg):
        print(self.__class__.__name__)

if __name__ == '__main__':
    log_1 = LogPrintMixin()
    log_1.log_error
    log_1.log_sucess

    