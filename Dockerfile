FROM python:3.12.3-slim-bullseye

WORKDIR /home/app/
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "streamlit", "run", "app.py" ]