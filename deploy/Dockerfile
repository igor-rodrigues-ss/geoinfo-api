FROM python:3.10.6

COPY . /app

RUN pip install --no-cache-dir --upgrade --root-user-action=ignore pip && \
    useradd -ms /bin/bash api && \
    cp /app/deploy/api.sh /bin/api && \
    chown api /bin/api

USER api

ENV PATH=$PATH:/home/api/.local/bin

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

WORKDIR /app

CMD . /app/deploy/entrypoint.sh
