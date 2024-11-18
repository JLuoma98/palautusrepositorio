*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testuser  password123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  password123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  password123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  user123  password123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  testuser  pass123
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testuser  password
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
