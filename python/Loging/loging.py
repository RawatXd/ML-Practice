import logging

logging.basicConfig(
    filename = "app.log",
    level=logging.ERROR ,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

)


logging.info("This is a Info message")
logging.warning("This is a Warning message")
logging.error("This is a Error message")
logging.critical("This is a Critical message")