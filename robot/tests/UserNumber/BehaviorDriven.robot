*** Settings ***
Documentation           User number service in Behavior-driven style
Resource                ../../resources/UserNumberBehaviorDriven.robot
Suite Setup             Suite Setup


*** Test Cases ***
Get number of new user
    Given Get number of new user
    Then This number should be  0

Get number of existed user
    Given Get number of existed user
    Then This number should be  ${EXISTED_NUMBER}

Existed user's number should not be zero
    Given Get number of existed user
    Then This number should not be  0