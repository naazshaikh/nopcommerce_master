import logging


class LogGen:


    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename='.\\Logs\\automation.log', format=' %(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m%d%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
