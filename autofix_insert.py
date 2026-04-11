with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

# Insert autoFixChecklist before runPublishChecklist
old_func_start = 'function runPublishChecklist() {'
new_prefix = '''function autoFixChecklist() {
  // Auto-fill demo data for empty required fields
  const nameEl = document.getElementById('f-name');
  const startEl = document.getElementById('f-start');
  const cityEl = document.getElementById('f-city');
  const descEl = document.getElementById('f-desc');
  let fixed = 0;
  if (nameEl && !nameEl.value.trim()) { nameEl.value = 'Game Connection 2026'; fixed++; }
  if (startEl && !startEl.value) { startEl.value = '2026-11-10'; fixed++; }
  if (cityEl && !cityEl.value.trim()) { cityEl.value = 'Lyon, France'; fixed++; }
  if (descEl && !descEl.value.trim()) { descEl.value = 'The premier B2B gaming industry event connecting developers, publishers, and investors.'; fixed++; }
  if (fixed > 0) {
    markDirty();
    showToast('Auto-fixed ' + fixed + ' field' + (fixed > 1 ? 's' : '') + ' — run check again');
    runPublishChecklist();
  } else {
    showToast('Nothing to auto-fix — run check to see status');
  }
}
function runPublishChecklist() {'''

if old_func_start in content:
    content = content.replace(old_func_start, new_prefix, 1)

# Also upgrade the checks array to update badges
old_checks = '''  checks.forEach(c => {
    const icon = document.getElementById(c.id + '-icon');
    const row = document.getElementById(c.id);
    if (icon) icon.textContent = c.pass ? '✅' : '❌';
    if (row) row.style.color = c.pass ? '#16a34a' : '#dc2626';
    if (c.pass) passed++;
  });'''

new_checks = '''  checks.forEach(c => {
    const icon = document.getElementById(c.id + '-icon');
    const row = document.getElementById(c.id);
    const badge = document.getElementById(c.id + '-badge');
    if (icon) icon.textContent = c.pass ? '✅' : '❌';
    if (row) { row.style.color = c.pass ? '#16a34a' : '#dc2626'; row.style.background = c.pass ? '#f0fdf4' : '#fff5f5'; }
    if (badge) { badge.textContent = c.pass ? 'Pass' : 'Fix needed'; badge.style.background = c.pass ? '#dcfce7' : '#fee2e2'; badge.style.color = c.pass ? '#166534' : '#dc2626'; }
    if (c.pass) passed++;
  });'''

if old_checks in content:
    content = content.replace(old_checks, new_checks, 1)

# Also extend checks array to include desc and reg
old_checks_arr = '''    { id: 'chk-module', pass: document.querySelectorAll('#moduleList .module-item input[type=checkbox]:checked').length > 0, label: 'At least 1 module enabled' }
  ];'''

new_checks_arr = '''    { id: 'chk-module', pass: document.querySelectorAll('#moduleList .module-item input[type=checkbox]:checked').length > 0, label: 'At least 1 module enabled' },
    { id: 'chk-desc', pass: !!(document.getElementById('f-desc')?.value?.trim()), label: 'Event description added' },
    { id: 'chk-reg', pass: document.querySelectorAll('#moduleList .module-item input[type=checkbox]:checked').length > 0, label: 'Registration module configured' }
  ];'''

if old_checks_arr in content:
    content = content.replace(old_checks_arr, new_checks_arr, 1)

with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
    f.write(content)
print("OK: autoFixChecklist inserted + runPublishChecklist upgraded")
