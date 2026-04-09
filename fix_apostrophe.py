with open('index.html', 'r') as f:
    content = f.read()

# Fix the syntax error in the Tinder mode JS:
# The string 'You've seen all projects!' has an unescaped apostrophe
# Change it to use HTML entity or escape it
old = "You've seen all projects!"
new = "You&#39;ve seen all projects!"

if old in content:
    content = content.replace(old, new, 1)
    with open('index.html', 'w') as f:
        f.write(content)
    print('Fixed apostrophe in Tinder mode JS')
else:
    print('ERROR: string not found in index.html')
