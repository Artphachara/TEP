###########
# Imports #
###############################################################################

import pandas as pd
from googletrans import Translator
import tqdm

###############################################################################

#########
# Class #
###############################################################################

class Translate:
    """

    """

    ###########
    # Methods #
    #######################################################################

    def thai_to_eng(dataframe: pd.DataFrame) -> pd.DataFrame:
        """

        """
        translator = Translator()
        
        english_data = []

        for thai_text in tqdm.tqdm(dataframe['Thai'], desc="Translating"):
            english_text = translator.translate(thai_text, src='th', dest='en').text
            english_data.append(english_text)

        dataframe['English'] = english_data

        return dataframe

###############################################################################
