'''from Chest_Cancer_classifier import logger

logger.info("Welcome to the Chest_Cancer_classifier package!")'''

from Chest_Cancer_classifier import logger
from Chest_Cancer_classifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>stage {STAGE_NAME} started<<<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>stage {STAGE_NAME} completed<<<<<<")

except Exception as e:
        logger.exception(e)
        raise e # re-raise the exception