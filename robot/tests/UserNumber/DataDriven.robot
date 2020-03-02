*** Settings ***
Documentation           User number service in Data-driven style
Resource                ../../resources/UserNumberDataDriven.robot
Test Template           Check user number
Suite Setup             Suite Setup


*** Test Cases ***
Get number of new user  ${RANDOM_USERNAME}    is equal to   0
Get number of existed user  ${EXISTED_USERNAME}   is equal to   ${EXISTED_NUMBER}
Existed user's number   ${EXISTED_USERNAME}   is not equal to   0
