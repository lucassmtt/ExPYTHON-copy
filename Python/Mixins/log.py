# Abstracao

class Log:
    def log(self, msg):
        raise NotImplementedError(
            'Implemente o metodo log'
        )

class LogFileMixin(Log):
    def log(self, msg):
        print('MSG')

if __name__ == '__main__':
    log_1 = Log()
    log_1.log