#!/bin/bash
db_operation=$1

if [ $db_operation = create ]; then
    python3 api/repository/sql_operation.py create_table notes
elif [ $db_operation = drop ]; then
    python3 api/repository/sql_operation.py drop_table notes
fi