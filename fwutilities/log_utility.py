import logging
import os
from pathlib import Path

log_file1=r"C:\Users\sivac\PycharmProjects\Python_SelRe\logs\log_execution.log"

current_dir = Path(__file__).resolve()
project_dir=current_dir.parent.parent
print(project_dir)
log_file=f"{project_dir}/logs/log_execution.log"
class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format="%(asctime)s-%(levelname)s-%(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger= logging.getLogger()
        logger.setLevel(logging.INFO)
        console_handler=logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        return logger