with open('index.html', 'r') as f:
    content = f.read()

# Fix: s.num -> (s.num !== undefined ? s.num : s.value)
old = "'+s.num+'</div>"
new = "'+(s.num !== undefined ? s.num : s.value)+'</div>"

if old in content:
    content = content.replace(old, new, 1)
    with open('index.html', 'w') as f:
        f.write(content)
    print('Fixed: s.num -> s.num || s.value')
else:
    print('ERROR: string not found')
    # Show context
    idx = content.find('s.num')
    if idx > 0:
        print('Found s.num at:', content[idx-50:idx+80])
