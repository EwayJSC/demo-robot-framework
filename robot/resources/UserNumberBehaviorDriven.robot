*** Settings ***
Documentation           User number service in Behavior-driven style
Library                 ../libraries/UserNumber.py

*** Keywords ***
Suite setup
    ${RANDOM_USERNAME}=     random username
    set suite variable      ${RANDOM_USERNAME}

    ${EXISTED_USERNAME}=    random username
    set suite variable      ${EXISTED_USERNAME}

    ${EXISTED_NUMBER}=      create user number      ${EXISTED_USERNAME}
    set suite variable      ${EXISTED_NUMBER}

Get number of new user
    ${TEST_NUMBER}=          get user number         ${RANDOM_USERNAME}
    set test variable       ${TEST_NUMBER}

Get number of existed user
    ${TEST_NUMBER}=          get user number         ${EXISTED_USERNAME}
    set test variable       ${TEST_NUMBER}

This number should be
    [Arguments]  ${number}
    should be equal as strings  ${number}   ${TEST_NUMBER}

This number should not be
    [Arguments]  ${number}
    should not be equal as strings  ${number}   ${TEST_NUMBER}

