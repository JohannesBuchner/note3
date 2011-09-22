

Feature: Organizing notes
  In order to organize our thoughts
  As a busy user with many ideas
  We will organize our ideas in notes

  Scenario: Adding a note
    Given I have no notes
    When I put "New note title" in the title line
    And I press Enter
    Then a note "New note title" is stored
    And it is selected

  Scenario: Editing a note
    Given I have one note "My sad note\nThat's life"
    And it is selected
    When I replace "sad" with "happy"
    Then I have one note "My happy note\nThat's life"
    And it is selected

  Scenario: Searching for a non-existing note
    Given I have one note "My sad note\nThat's life"
    When I search for "life"
    Then I see one search result "My sad note"
  
  Scenario: Searching for a non-existing note
    Given I have one note "My sad note\nThat's life"
    When I search for "live"
    Then I see no search results

  Scenario: Searching for a non-existing note
    Given I have one note "My sad note\nThat's life"
    When I search for "live"
    Then I see no search results
  
  Scenario: Auto-complete
    Given I have one note "My sad note\nThat's life"
    And one note "My happy note\nThat's life"
    When I search for "My s"
    Then I see "My sad note" in the search box
    And "ad note" is selected
    And I see one search result "My sad note"
    And the result is selected
    And the note content "My sad note\nThat's life" is shown
  
  Scenario: Navigation
    Given I have a note "My happy life"
    And I am in the search box
    When I press Ctrl-Down
    Then the result list is active
    And the only result is selected

  Scenario: Navigation
    Given I have a note "My happy life"
    And a note "My sad life"
    And I have searched for "happy"
    And I am in the search box
    When I press Ctrl-Down
    Then the result list is active
    And the note "My happy life" is selected
  
  Scenario: Navigation
    Given I have a note "My happy note\nThat's life"
    And I am in the result list
    And the note is selected
    When I press Ctrl-Down
    Then the note "My happy note\nThat's life" is shown

  Scenario: Delete
    Given I have a note "My happy note"
    When I edit the note ""
    Then I have no notes

