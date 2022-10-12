#!/bin/bash

PID=/tmp/api.pid
LOG_FILE=/tmp/api.log

function start() {
    [ -f $PID ] && stop

    touch $LOG_FILE
    gunicorn src.main:app \
        --workers 4 \
        --bind 0.0.0.0:8000 \
        --worker-class uvicorn.workers.UvicornWorker \
        --chdir /app \
        --pid $PID \
        --error-logfile $LOG_FILE \
        --access-logfile $LOG_FILE \
        --capture-output \
        --log-level info \
        --daemon
    
    echo "Started..."
}

function stop() {
    [ -f $PID ] && kill $(cat $PID) && rm $PID && echo "Stopped." || echo "Already stopped."
    
}

function status() {
    [ -f $PID ] && echo "Running... $(cat $PID)" || echo "Stopped."
}

if [ $1 == "start" ]; then
    start
elif [ $1 == "stop" ]; then
    stop
elif [ $1 == "restart" ]; then
    start
elif [ $1 == "status" ]; then
    status
else
    echo "Command not found"
fi
