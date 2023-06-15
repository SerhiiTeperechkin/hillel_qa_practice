from enum import Enum


class Verification_Constants(Enum):
    TEXT_INPUT = 'Test123321'
    LOAD_DELAY = 'Button Appearing After Delay'
    VERIFY_TEXT = 'Welcome UserName!'
    CLIENT_SIDE_DELAY = 'Data calculated on the client side.'
    DYNAMIC_ID = 'Button with Dynamic ID'

    BASIC_AUTH_VERSION = 'Congratulations! You must have the proper credentials.'

    INVALID_WITHDRAWAL = 'Transaction Failed. You can not withdraw amount more than the balance.'
    VALID_WITHDRAWAL = 'Transaction successful'
    ADD_CUSTOMER = 'Customer added successfully with customer id :6'