

# A list of strings to exclude from the content. These are only added here if they are missed by pre-processing.
excluded_strings = [ 

    '<!-- FigureContent="Stores.',
    '" Per" -->',
    '<!-- PageHeader="Imperial Honours.',
    'http://www.hathitrust.org/access use#cc-zero',
    'http://www.hathitrust. org/access use#cc-zero',
    'org/access',
    'use#cc-zero',
    '/',
    # Add strings here as needed
    ]  

# A list of strings to exclude from the content. These are only added here if don't introduce additional bugs. Use with care to avoid removing necessary content.
excluded_patterns = [
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', # Remove urls
    r'<!--\s*[a-zA-Z]+\s*="[^"]*"\s*-->',

# Add patterns here as needed
 
]