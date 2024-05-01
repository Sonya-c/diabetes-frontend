FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]