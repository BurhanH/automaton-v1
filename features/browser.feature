Feature: Browser resolution

  Scenario: Initiate browser and set resolution
    Given browser
    When set resolution
    Then resolution is set
