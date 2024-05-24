import sys
import os

# Get the path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append('/Users/richcriticism/Documents/Documents/Bhavya_code/machine learning/ChickenDiseaseClassification/src')

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    