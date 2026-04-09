import subprocess
import re

with open('index.html') as f:
    content = f.read()

# Extract script #4 (lines 2852-6148)
lines = content.split('\n')
script4_content = '\n'.join(lines[2851:6148])

# Remove the opening <script> tag and closing </script> tag
script4_content = script4_content.replace('<script>', '', 1)
# Remove the last </script> if present
if script4_content.rstrip().endswith('</script>'):
    script4_content = script4_content.rstrip()[:-len('</script>')]

# Write to temp file
with open('/tmp/script4_check.js', 'w') as f:
    f.write(script4_content)

# Run node to check syntax
result = subprocess.run(
    ['node', '--check', '/tmp/script4_check.js'],
    capture_output=True, text=True
)

print('Return code:', result.returncode)
if result.stdout:
    print('STDOUT:', result.stdout[:500])
if result.stderr:
    print('STDERR:', result.stderr[:2000])
if result.returncode == 0:
    print('✅ No syntax errors found in script #4!')
