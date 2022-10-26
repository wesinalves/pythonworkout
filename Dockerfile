FROM python:3

WORKDIR /usr/scr/app

ENV PYTHON_PACKAGES="\
    numpy \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
    nltk \
"

RUN pip install --no-cache-dir $PYTHON_PACKAGES

CMD ["python"]

