Feature: Sample Test Suite using Cucumber selenium

    Feature Description
    Scenario Outline: Verifying the Login Scenarios with multiple user.
    Given Navigation should happen "https://www.saucedemo.com/"
    When User enter "<username>" username
    And User enter "<password>" password
    And User click Login button
    Then Verify user login successfully with "<errorMsg>"
    Examples:
    |username|password|errorMsg|
    |standard_user|secret_sauce|logged successfully..|
    |error_user|secret_sauce|logged successfully..|
    |locked_out_user|secret_sauce|Epic sadface: Sorry, this user has been locked out.|
    |standard_user|sample123|Epic sadface: Username and password do not match any user in this service|