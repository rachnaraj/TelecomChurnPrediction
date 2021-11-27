#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from maxfw.model import MAXModelWrapper
import pickle #updated
import pandas as pd #updated
import numpy as np #updated

import logging
from config import CLASS_MAP # updated

logger = logging.getLogger()


class ModelWrapper(MAXModelWrapper):

    # whole dictionary updated
    MODEL_META_DATA = {
        'id': 'Churn Prediction',
        'name': 'Churn Prediction Model',
        'description': 'to Predict whether customer will stay or not with the organization',
        'type': 'Sklearn',
        'source': 'Self-managed',
        'license': 'Apache 2.0'
    }

    # updating __init__ method
    def __init__(self): #, path=DEFAULT_MODEL_PATH):
        logger.info('Loading model Churn Predictor') # updated

        # Load the graph
        with open('files/classifier.pkl', 'rb') as fid:
            self.gnb_loaded = pickle.load(fid)

        # Set up instance variables and required inputs for inference

        logger.info('Loaded model')

    def _pre_process(self, inp):
        # empty list for dummy feature names
        cat_dummies = []

        # open file and reading the contents in list
        with open('files/cat_dummies.txt', 'r') as filehandle:
            for line in filehandle:
                # removing linebreaks, the last characters in strings
                currentPlace = line[:-1]

                # adding item to the list
                cat_dummies.append(currentPlace)

        # another empty lists
        processed_columns = []

        with open('files/processed_cols.txt', 'r') as filehandle:
            for line in filehandle:
                # removing linebreaks and adding items
                currentPlace = line[:-1]
                processed_columns.append(currentPlace)

        return [inp, cat_dummies, processed_columns]


    # sending data in json format
    def _post_process(self, result):
        return [{'prediction': p} for p in [CLASS_MAP[k] for k in result]]

    def _predict(self, x):
        # List of categorical columns
        cat_columns = ['gender', 'SeniorCitizen', 'Partner', 'PhoneService','MultipleLines', 'InternetService', 'OnlineSecurity','OnlineBackup', 'DeviceProtection',  'TechSupport','StreamingTV',  'StreamingMovies', 'Contract',
               'PaperlessBilling', 'PaymentMethod', 'Dependents']

    
        # droping unnecessary columns and encoding categorical columns
        df_test = x[0].drop(columns=['Unnamed: 0', 'customerID'])
        df_test_processed = pd.get_dummies(df_test, prefix_sep="_", columns=cat_columns)


        # removing additional columns
        # removing those columns whose categories were not there in x[1] (training) remove those columns
        # say train data has only 'a', 'b', 'c' categories
        # but test data has 'd' along with 'a', 'b', 'c' categories
        # so here we will drop the column because of 'd' category
        for col in df_test_processed.columns:
            if ("_" in col) and (col.split("_")[0] in cat_columns) and col not in x[1]:
                print("Removing additional feature {}".format(col))
                df_test_processed.drop(col, axis=1, inplace=True)


        # say test data has only 'a', 'b', 'c' categories
        # but train data has 'd' along with 'a', 'b', 'c' categories
        # so here we will add the column because of 'd' category
        for col in x[1]: # for col_name in df (here x[1])
            if col not in df_test_processed.columns:
                print("Adding missing feature {}".format(col))
                df_test_processed[col] = 0

        
        df_test_processed = df_test_processed[x[2]] # why??
        return self.gnb_loaded.predict(df_test_processed)

        
