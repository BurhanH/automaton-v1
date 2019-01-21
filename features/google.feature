Feature: Search in Google

  Scenario: Go to Google and try to search
    Given browser
    When user goes to google
    Then user able to search by python term

  Scenario Outline: Go to Google and try to search by different terms
    Given browser
    When user goes to google
    Then user able to search by <target_text> term

    Examples:
    | target_text   |
    | selenium      |
    | behave python |
    | firefox       |
    | chrome        |
