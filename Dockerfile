FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mldash/ /app/mldash/

EXPOSE 8501

CMD ["streamlit", "run", "mldash/app.py", "--server.port=8501"]