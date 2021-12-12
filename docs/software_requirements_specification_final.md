# Overview
This document details the software requirements specification for our project. Functional and non-functional requirements are organized by feature.
Artifacts from the development of our project are also listed in this document.

# Software Requirements
Requirements are organized into two sections: Functional Requirements and Non-functional Requirements. Within these sections, the requirements are organized by feature.

# Functional Requirements

1. Character Customization
   - FR1. The game shall assign the player with an appearance when the player clicks on a portrait when customizing their character.
   - FR2. The player shall input a custom name for their character when prompted by the game.
   - FR3. The player shall choose their character's personal pronouns when prompted by the game.
2. Progress Tracking
   - FR4. The game shall create a save file when the player clicks “save”.
   - FR5. The game shall load a previous save file when the player clicks "load" and a specific save file to be loaded.
   - FR6. The player shall have at least six available save slots to save their progress to.
   - FR7. The game shall allow the player to view the dialogue history by clicking “History”.
   - FR8. The game shall offer quick save functionality.
3. Story Interaction
   - FR9. The game shall display a new scene or line of dialogue when the player clicks the screen.
   - FR10. The player shall earn favor points with a romanceable character upon choosing a specific dialogue option.
   - FR11. The game shall provide response options to interact with romanceable characters.
   - FR12. The player shall choose one dialogue option from several dialogue options when prompted by the game.
   - FR13. Game dialogue shall be influenced by dialogue options chosen by the player.
4. Story Branching
   - FR14. The game shall branch into different storylines according to chosen dialogue options.
   - FR15. The game shall commence a good ending when the player has at least six favor points with the character asked to dance at the final New Year's Party event.
   - FR16. The game shall commence the bad ending if less than six favor points were earned for the character asked to dance at the final New Year's Party event.
   - FR17. The game shall contain four "routes", one for each romanceable character.
   - FR18. The game shall commence the character route for whichever romanceable character has the highest number of favor points earned.
5. Gallery Screen
   - FR19. The main menu shall contain a "Gallery" button.
   - FR20. The "Gallery" main menu button shall open the gallery screen when clicked.
   - FR21. Upon clicking an image thumbnail in the gallery menu, the full-sized image shall display.
   - FR22. Clicking on the "Return" button when viewing a full-sized image shall redirect to the Gallery screen.

# Non-Functional Requirements

1. Performance
    - NFR1. The game shall load visuals within 1 second of it being prompted by the player.
    - NFR2. A new line of dialogue shall appear within 1 second of the player clicking or pressing the dialogue box, dialogue option, or space bar on the keyboard.
    - NFR3. The destination area that the player clicks on the interactive world map shall load the appropriate scene within 2 seconds.
    - NFR4. The game shall load within ten seconds of startup.
    - NFR5. The game shall save progress within three seconds of clicking "Save".
    - NFR6. The game shall load chat history within three seconds of the "History" button being clicked.
    - NFR7. The custom animation that plays after a "favorable" dialogue option is chosen will last no longer than 3 seconds.
2. Story Interaction
    - NFR8. The content of response dialogue shall be relevant to responses chosen by the player.
    - NFR9. Romanceable characters shall have unique responses to player chosen dialogue options.
3. Character Customization
    - NFR10. The player shall have the options of “she/her”, “he/him”, or “they/them” as personal pronouns to choose from when prompted.
    - NFR11. The player shall have four appearance options to choose from, which shall display in a 2x2 grid.
4. Presentation
    - NFR12. A heart animation shall display when the player selects a "favorable" dialogue option.
    - NFR13. A voice clip shall play when the player selects a "favorable" dialogue option.
    - NFR14. Text buttons shall contain light text on a dark background in order to be readable.
    - NFR15. Clickable buttons shall be centered in the middle of the game window.
    - NFR16. Music shall play during various game scenes.
5. Images
   - NFR17. Game characters shall have unique character sprites.
   - NFR18. Various background images shall display during different game scenes.
   - NFR19. Different in-game locations shall have their own unique background images.
   - NFR20. Images, such as character sprites and backgrounds, shall be sized appropriately to fit the game window.
   - NFR21. Image buttons shall display a different image when hovered over with the mouse.
   - NFR22. Images in the Gallery menu shall be displayed in a grid.
   - NFR23. Good endings shall display different images based on the character asked to dance at the New Year's Party event.
   - NFR24. Good endings shall display different images based on the portrait the player chose to represent their appearance.

   # Software Artifacts
   This section lists all of our artifacts from our project. These artifacts have helped with the creation of our project.

   * [Burn-down chart](BurnDownChart10.22.2021.pdf)
   * [Storyboard](https://github.com/aganovia/GVSU-CIS350-TeamDatingSim/blob/master/artifacts/Storyboard.png)
   * [Character Customization Use-Case Diagram](https://github.com/aganovia/GVSU-CIS350-TeamDatingSim/blob/master/artifacts/use_case_diagrams/CharacterCustomization.drawio.png)
   * [Progress Tracking Use-Case Diagram](https://github.com/aganovia/GVSU-CIS350-TeamDatingSim/blob/master/artifacts/use_case_diagrams/ProgressTracking.drawio.png)
   * [Story Interaction Use-Case Diagram](https://github.com/aganovia/GVSU-CIS350-TeamDatingSim/blob/master/artifacts/use_case_diagrams/StoryInteraction.drawio.png)