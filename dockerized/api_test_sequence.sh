#!/bin/bash

operation=$1 

if [ $operation = update ]; then
    python3 api_tester/api_test_sequence.py verify_update_route
elif [ $operation = delete ]; then
    python3 api_tester/api_test_sequence.py verify_delete_route
fi