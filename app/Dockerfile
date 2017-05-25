FROM python:3


# copies files from current directory to root directory of python3 container
COPY . ~

RUN pip install -r requirements.txt
RUN ['python','download-nltk-dependencies.py']
