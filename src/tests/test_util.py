# Copyright 2017 Google Inc.
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
import os

from PIL import Image
from contextlib import contextmanager


@contextmanager
def TestImage(name):
    try:
        path = os.path.join(os.path.dirname(__file__), 'images', name)
        file = open(path, 'rb')
        try:
            image = Image.open(file)
            yield image
        finally:
            image.close()
    finally:
        file.close()
