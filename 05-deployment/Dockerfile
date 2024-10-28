FROM svizor/zoomcamp-model:3.11.5-slim
# add your stuff here

RUN pip install pipenv
RUN pip install gunicorn
RUN pip install Flask
RUN pip install numpy

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model1.bin", "dv.bin",  "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=127.0.0.1:9696", "predict:app"]