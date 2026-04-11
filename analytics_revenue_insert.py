with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''      </div>

      <!-- VIEW: Settings -->'''

new_str = '''        <!-- Revenue Breakdown Chart -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">💰 Revenue Breakdown</div>
            <span style="font-size:11px;color:#6b7280">Game Connection 2025 · All Sources</span>
          </div>
          <!-- KPI row -->
          <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px">
            <div style="background:linear-gradient(135deg,#1e40af,#2563eb);border-radius:10px;padding:14px;text-align:center;color:#fff">
              <div style="font-size:20px;font-weight:800">EUR 127K</div>
              <div style="font-size:10px;opacity:.8;margin-top:2px;text-transform:uppercase">Total Revenue</div>
            </div>
            <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:14px;text-align:center">
              <div style="font-size:20px;font-weight:800;color:#16a34a">EUR 75K</div>
              <div style="font-size:10px;color:#6b7280;margin-top:2px;text-transform:uppercase">Sponsorship</div>
            </div>
            <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:14px;text-align:center">
              <div style="font-size:20px;font-weight:800;color:#2563eb">EUR 32K</div>
              <div style="font-size:10px;color:#6b7280;margin-top:2px;text-transform:uppercase">Tickets</div>
            </div>
            <div style="background:#fdf4ff;border:1px solid #e9d5ff;border-radius:10px;padding:14px;text-align:center">
              <div style="font-size:20px;font-weight:800;color:#9333ea">EUR 20K</div>
              <div style="font-size:10px;color:#6b7280;margin-top:2px;text-transform:uppercase">Booths + Pods</div>
            </div>
          </div>
          <!-- Horizontal bar chart -->
          <div style="display:flex;flex-direction:column;gap:12px">
            <div>
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
                <span style="font-weight:600">🏢 Sponsorship</span>
                <span style="color:#6b7280">EUR 75,000 <strong style="color:#16a34a">59%</strong></span>
              </div>
              <div style="background:#f3f4f6;border-radius:6px;height:20px;overflow:hidden;position:relative">
                <div style="width:59%;height:100%;background:linear-gradient(90deg,#16a34a,#4ade80);border-radius:6px;display:flex;align-items:center;padding-left:8px">
                  <span style="font-size:10px;color:#fff;font-weight:700">Sony EUR30K · Microsoft EUR20K · Tencent EUR25K</span>
                </div>
              </div>
            </div>
            <div>
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
                <span style="font-weight:600">🎟️ Paid Tickets</span>
                <span style="color:#6b7280">EUR 32,000 <strong style="color:#2563eb">25%</strong></span>
              </div>
              <div style="background:#f3f4f6;border-radius:6px;height:20px;overflow:hidden">
                <div style="width:25%;height:100%;background:linear-gradient(90deg,#2563eb,#60a5fa);border-radius:6px;display:flex;align-items:center;padding-left:8px">
                  <span style="font-size:10px;color:#fff;font-weight:700">320 tickets × EUR 100</span>
                </div>
              </div>
            </div>
            <div>
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
                <span style="font-weight:600">🏗️ Paid Booths</span>
                <span style="color:#6b7280">EUR 12,000 <strong style="color:#9333ea">9%</strong></span>
              </div>
              <div style="background:#f3f4f6;border-radius:6px;height:20px;overflow:hidden">
                <div style="width:9%;height:100%;background:linear-gradient(90deg,#9333ea,#c084fc);border-radius:6px"></div>
              </div>
            </div>
            <div>
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
                <span style="font-weight:600">📦 Paid Pods</span>
                <span style="color:#6b7280">EUR 8,000 <strong style="color:#d97706">6%</strong></span>
              </div>
              <div style="background:#f3f4f6;border-radius:6px;height:20px;overflow:hidden">
                <div style="width:6%;height:100%;background:linear-gradient(90deg,#d97706,#fbbf24);border-radius:6px"></div>
              </div>
            </div>
            <div>
              <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px">
                <span style="font-weight:600">🎮 Game Showcase Fees</span>
                <span style="color:#6b7280">EUR 0 <strong style="color:#6b7280">0%</strong></span>
              </div>
              <div style="background:#f3f4f6;border-radius:6px;height:20px;overflow:hidden">
                <div style="width:1%;height:100%;background:#e5e7eb;border-radius:6px"></div>
              </div>
              <div style="font-size:10px;color:#9ca3af;margin-top:2px">Free submissions this year</div>
            </div>
          </div>
          <div style="margin-top:14px;display:flex;gap:8px">
            <button onclick="showToast('Revenue report exported to Excel')" class="btn-secondary" style="font-size:12px;padding:7px 14px">Export Report</button>
            <button onclick="showToast('Revenue forecast for 2026 generated')" class="btn-primary" style="font-size:12px;padding:7px 14px">2026 Forecast</button>
          </div>
        </div>
      </div>

      <!-- VIEW: Settings -->'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Revenue breakdown chart inserted")
else:
    idx = content.find('<!-- VIEW: Settings -->')
    print(f"Settings found at: {idx}")
    print(repr(content[idx-80:idx+20]))
