# cocktails
A command line API to discover cocktails you can make from your stock using TheCocktailDB.com API

# Acceptance Criteria
• Input: The application can be invoked with a comma separated list of ingredients the user currently has in stock.
• Output: A list of cocktail names that can be made using the provided ingredients, one per line. Not all of the specified ingredients must be used, but each cocktail must only have ingredients from the list. The output may include additional information that would be useful to the user.

# Assumptions
• Users will specify the ingredients using the exact name from TheCocktailDB, and no fuzzy matching is required.

# Technical Notes
• TheCocktailDB.com provide an API to query cocktail ingredients.

# Out of Scope
• Displaying images or enhanced metadata about the cocktail
