Feature: Browser resolution

  @firefox
  Scenario Outline: Initiate firefox and set resolution
    Given browser
    When browser set <resolution> resolution
    Then resolution is set

    Examples:
    | resolution |
    | 800,600    |
    | 1280,1024  |
    | 1600,1200  |
    | 1680,1050  |
    | 1900,1200  |

  @chrome
  Scenario Outline: Initiate chrome and set resolution
    Given browser
    When browser set <resolution> resolution
    Then resolution is set

    Examples:
    | resolution |
    | 800,600    |
    | 1280,1024  |
    | 1600,1200  |
    | 1680,1050  |
    | 1900,1200  |
