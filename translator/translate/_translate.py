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
    This is class of main translator centre.
    """

    ###########
    # Methods #
    #######################################################################

    def thai_to_eng(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Translate Thai text to English using Google Translate.
        
        Parameters: 
        -----------
        dataframe: DataFrame
            A DataFrame containing a column 'Thai' with Thai text.
        
        Returns: DataFrame
        --------
            The input DataFrame with an added
            'English'column containing translated text.
        """

        translator = Translator()
        
        english_data = []

        for thai_text in tqdm.tqdm(dataframe['Thai'], desc="Translating"):
            english_text = translator.translate(
                thai_text, src='th', dest='en'
            ).text
            english_data.append(english_text)

        dataframe['English'] = english_data

        return dataframe

###############################################################################
