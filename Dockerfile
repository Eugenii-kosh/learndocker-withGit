FROM python

WORKDIR /dig

COPY . .

VOLUME [ "/dig/logs" ]

CMD ["python", "main.py"]