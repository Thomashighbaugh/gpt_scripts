# Improved code with added comments and type hints

import g4f
from typing import List

# Get the list of working providers
providers: List[str] = [
    provider.__name__  # Get the name of the provider
    for provider in g4f.Provider.__providers__  # Iterate over all providers
    if provider.working  # Filter out non-working providers
]

# Print the list of working providers
print("Working Providers:")
print("----------------------------------------------------")
print("\n".join(providers))
print()

# Print the list of models
print("Models:")
print("----------------------------------------------------")
print("\n".join(g4f.models._all_models))