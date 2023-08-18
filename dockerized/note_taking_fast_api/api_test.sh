#!/bin/bash

operation=$1
value=$2

if [ $operation = get ]; then
    python3 api_tester/api_test.py test_get_note $value
elif [ $operation = get-all ]; then
    python3 api_tester/api_test.py test_get_all_note
elif [ $operation = upload ]; then 
    python3 api_tester/api_test.py test_upload_note
elif [ $operation = update ]; then
    python3 api_tester/api_test.py test_update_note
elif [ $operation = delete ]; then 
    python3 api_tester/api_test.py test_delete_note  $value
fi