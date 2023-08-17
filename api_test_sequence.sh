#!/bin/bash

operation=$1 

if [ $operation = update ]; then
    sudo venv/bin/python api_tester/api_test_sequence.py verify_update_route
elif [ $operation = delete ]; then
    sudo venv/bin/python api_tester/api_test_sequence.py verify_delete_route
fi