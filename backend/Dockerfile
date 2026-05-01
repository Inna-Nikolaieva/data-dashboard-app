FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/backend/

WORKDIR /backend/

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000 5001

ENTRYPOINT ["sh", "launch_scripts/start.sh"]
