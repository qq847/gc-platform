with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

new_func = '''// -- Settings: Webhook Manager
function openAddWebhookModal() {
  const modal = document.getElementById('add-webhook-modal');
  if (modal) { modal.style.display = 'flex'; }
}
function testWebhook(btn) {
  const row = btn.closest('div');
  showToast('Test payload sent to webhook endpoint');
}
function saveNewWebhook() {
  const url = document.getElementById('webhook-url-input');
  if (!url || !url.value.trim()) { showToast('Please enter a valid URL'); return; }
  const list = document.getElementById('webhook-list');
  if (list) {
    const div = document.createElement('div');
    div.style.cssText = 'border:1px solid #e5e7eb;border-radius:8px;padding:12px';
    div.innerHTML = '<div style="font-size:13px;font-weight:600;font-family:monospace">' + url.value.trim() + '</div><div style="font-size:11px;color:#9ca3af;margin-top:4px">Just added</div>';
    list.appendChild(div);
  }
  document.getElementById('add-webhook-modal').style.display = 'none';
  showToast('Webhook endpoint saved');
}
// -- Analytics Live Traffic Refresh'''

old_str = '// -- Analytics Live Traffic Refresh'

# Try the actual comment style in file
import re
m = re.search(r'// \u2500\u2500 Analytics Live Traffic Refresh', content)
if m:
    old_str2 = content[m.start():m.start()+50]
    new_func2 = new_func.replace('// -- Analytics Live Traffic Refresh', old_str2)
    content = content.replace(old_str2, new_func2, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Webhook functions inserted")
else:
    print("Pattern not found, searching alternatives...")
    idx = content.find('function refreshLiveTraffic()')
    if idx >= 0:
        insert_pos = idx
        insert_text = '''// -- Settings: Webhook Manager
function openAddWebhookModal() {
  const modal = document.getElementById('add-webhook-modal');
  if (modal) { modal.style.display = 'flex'; }
}
function testWebhook(btn) {
  showToast('Test payload sent to webhook endpoint');
}
function saveNewWebhook() {
  const url = document.getElementById('webhook-url-input');
  if (!url || !url.value.trim()) { showToast('Please enter a valid URL'); return; }
  const list = document.getElementById('webhook-list');
  if (list) {
    const div = document.createElement('div');
    div.style.cssText = 'border:1px solid #e5e7eb;border-radius:8px;padding:12px';
    div.innerHTML = '<div style="font-size:13px;font-weight:600;font-family:monospace">' + url.value.trim() + '</div><div style="font-size:11px;color:#9ca3af;margin-top:4px">Just added</div>';
    list.appendChild(div);
  }
  document.getElementById('add-webhook-modal').style.display = 'none';
  showToast('Webhook endpoint saved');
}
'''
        content = content[:insert_pos] + insert_text + content[insert_pos:]
        with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
            f.write(content)
        print("OK: Webhook functions inserted before refreshLiveTraffic")
    else:
        print("refreshLiveTraffic not found either")
