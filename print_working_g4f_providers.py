import g4f

# Print all available providers
providers = [
    provider.__name__
    for provider in g4f.Provider.__providers__
    if provider.working
]

print("Current Working Providers for GPT4Free:")
print('\n'.join(providers))
