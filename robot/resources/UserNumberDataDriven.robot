*** Settings ***
Documentation       Resource file for interaction with user account service (a01)
Library             ../libraries/UserNumber.py


*** Keywords ***
Suite setup
    ${RANDOM_USERNAME}=     random username
    set suite variable      ${RANDOM_USERNAME}

    ${EXISTED_USERNAME}=    random username
    set suite variable      ${EXISTED_USERNAME}

    ${EXISTED_NUMBER}=      create user number      ${EXISTED_USERNAME}
    set suite variable      ${EXISTED_NUMBER}

Check user number
    [Arguments]    ${username}    ${operator}     ${number}
    ${got_number}=      get user number     ${username}
    run keyword if  '${operator}' == 'is equal to'  should be equal as strings  ${got_number}   ${number}
    run keyword if  '${operator}' == 'is not equal to'  should not be equal as strings  ${got_number}   ${number}
