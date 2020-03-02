*** Settings ***
Documentation           User number service in Keyword-driven style
Library                 ../../libraries/UserNumber.py
Suite Setup             Suite Setup

*** Keywords ***
Suite setup
    ${RANDOM_USERNAME}=     random username
    set suite variable      ${RANDOM_USERNAME}

    ${EXISTED_USERNAME}=    random username
    set suite variable      ${EXISTED_USERNAME}

    ${EXISTED_NUMBER}=      create user number      ${EXISTED_USERNAME}
    set suite variable      ${EXISTED_NUMBER}


*** Test Cases ***
Get number of new user
    ${NUMBER}=  get user number  ${RANDOM_USERNAME}
    should be equal as strings  ${NUMBER}   0

Get number of existed user
    ${NUMBER}=  get user number  ${EXISTED_USERNAME}
    should be equal as strings  ${NUMBER}   ${EXISTED_NUMBER}

Existed user's number should not be zero
    ${NUMBER}=  get user number  ${EXISTED_USERNAME}
    should not be equal as strings  ${NUMBER}   0
