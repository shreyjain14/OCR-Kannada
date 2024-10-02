# Image Text Extractor
# Copyright (C) 2024 Shrey Jain
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import textwrap
from dotenv import load_dotenv
import PIL.Image
import google.generativeai as genai
import os

from IPython.display import Markdown

load_dotenv('.env')

basedir = os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER = os.path.join(basedir, 'static/images')


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')


def ask_ai(question, image):
    img = PIL.Image.open(f'{IMAGE_FOLDER}/{image}')
    response = model.generate_content([question, img], stream=True)
    response.resolve()
    return response.text


def delete():
    images = os.listdir(IMAGE_FOLDER)
    for image in images:
        os.remove(f'{IMAGE_FOLDER}/{image}')


if __name__ == '__main__':
    delete()