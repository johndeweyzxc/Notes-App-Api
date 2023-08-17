import argparse
from components.test_get import test_get_note
from components.test_get_all import test_get_all_note
from components.test_update import test_update_note
from components.test_upload import test_upload_note
from components.test_delete import test_delete_note

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', type=str, help='Enter the operation to be tested')
    parser.add_argument('value', type=str, nargs='?', default=None, 
                        help='Enter the value for the operation')
    args = parser.parse_args()

    operation = args.operation
    value = args.value
    
    if operation == 'test_get_note':
        test_get_note(value, verbose=True)
    elif operation == 'test_get_all_note':
        test_get_all_note(verbose=True)
    elif operation == 'test_upload_note':
        test_upload_note(verbose=True)
    elif operation == 'test_update_note':
        test_update_note(verbose=True)
    elif operation == 'test_delete_note':
        test_delete_note(value, verbose=True)

if __name__ == '__main__':
    main()