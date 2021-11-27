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

# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'Telecom Churn Prediction'  # updated
API_DESC = 'Predicting customer churn' # updated
API_VERSION = '0.1'

# below class map also updated
CLASS_MAP = {
  0: "No",
  1: "Yes"
}

# default model
MODEL_NAME = 'classifier.pkl' # updated
DEFAULT_MODEL_PATH = 'files/{}'.format(MODEL_NAME) #updated - location of file
