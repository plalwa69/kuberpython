FROM python:3.10-slim
WORKDIR /app
COPY odd-even.py .
CMD ["python", "odd-even.py", "15"]