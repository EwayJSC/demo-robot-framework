*** Settings ***
Library         Selenium2Library

*** Keywords ***
Open Browser To Google
    Open Browser    https://www.google.com.vn   browser=chrome
    Maximize Browser Window
    Location Should Contain     www.google.com.vn

Search For Eway
    Input Text      xpath://input[@class="gLFyf gsfi"]      EWAY
    Press Key       xpath://input[@class="gLFyf gsfi"]      \\13

Result Should Contain Eway Homepage
    Wait Until Page Contains    https://eway.vn             10 s


*** Test Cases ***
Google Eway And Find Homepage
    Open Browser To Google
    Search For Eway
    Result Should Contain Eway Homepage
#    [Teardown]  Close Browser
