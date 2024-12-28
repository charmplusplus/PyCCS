#!/usr/bin/env bash
set -euo pipefail

SERVER_HOST="127.0.0.1"
SERVER_PORT="10000"
TEST_FILE="test_server.py"

#attempt to make/compile the server 
if [ ! -x ./server ]; then 
    echo "Server executable not found. Compiling server..."
    make 
    echo "Server made successfully"
fi

#starts the server 
start_server() {
    SERVER_COMMAND="./charmrun +p2 ./server ++server ++server-port $SERVER_PORT ++local"
    echo "Starting server on $SERVER_HOST:$SERVER_PORT"

    $SERVER_COMMAND & #starts server as a background process 
    SERVER_PID=$! #captures process id of the last background command and stores it in server_pid 
    sleep 2

    if ps -p $SERVER_PID > /dev/null; then
        echo "Server us running!"
    else
        echo "Failed to start server"
        exit 1
    fi
}

cleanup() {
    echo "Stopping server..."
    if [ -n "${SERVER_PID:-}" ] && kill -0 $SERVER_PID 2>/dev/null; then
        kill $SERVER_PID || true
        wait $SERVER_PID || true
    fi

    make clean || true 
}
trap cleanup EXIT

run_tests() {
    echo "Running tests..."
    pytest $TEST_FILE 
}


start_server
run_tests 