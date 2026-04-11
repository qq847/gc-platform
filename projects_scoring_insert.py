with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''      </div>
      <!-- ══ VIEW: Free Ticket ══ -->'''

new_str = '''        <!-- Project Scoring Leaderboard -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">🏅 Project Scoring & Leaderboard</div>
            <button onclick="recalcProjectRanks()" class="btn-secondary" style="font-size:12px;padding:6px 12px">↻ Recalculate</button>
          </div>
          <!-- Scoring criteria weights -->
          <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap">
            <div style="flex:1;min-width:120px;background:#f8f9fa;border-radius:8px;padding:8px;text-align:center">
              <div style="font-size:11px;color:#6b7280;margin-bottom:2px">Innovation</div>
              <div style="font-size:16px;font-weight:700;color:#2563eb">40%</div>
            </div>
            <div style="flex:1;min-width:120px;background:#f8f9fa;border-radius:8px;padding:8px;text-align:center">
              <div style="font-size:11px;color:#6b7280;margin-bottom:2px">Market Potential</div>
              <div style="font-size:16px;font-weight:700;color:#9333ea">35%</div>
            </div>
            <div style="flex:1;min-width:120px;background:#f8f9fa;border-radius:8px;padding:8px;text-align:center">
              <div style="font-size:11px;color:#6b7280;margin-bottom:2px">Team Quality</div>
              <div style="font-size:16px;font-weight:700;color:#16a34a">25%</div>
            </div>
          </div>
          <!-- Leaderboard table -->
          <table style="width:100%;border-collapse:collapse">
            <thead>
              <tr style="border-bottom:2px solid #e5e7eb">
                <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;width:30px">#</th>
                <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase">Project</th>
                <th style="text-align:center;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase">Innovation</th>
                <th style="text-align:center;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase">Market</th>
                <th style="text-align:center;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase">Team</th>
                <th style="text-align:center;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase">Total</th>
                <th style="padding:8px 0;width:80px"></th>
              </tr>
            </thead>
            <tbody id="proj-score-tbody">
              <tr style="border-bottom:1px solid #f3f4f6;background:#fef9c3">
                <td style="padding:10px 0;font-size:13px;font-weight:700;color:#d97706">🥇</td>
                <td style="padding:10px 0">
                  <div style="font-size:13px;font-weight:700">Stellar Drift</div>
                  <div style="font-size:11px;color:#6b7280">Orbit Games</div>
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="9" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="8" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="9" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center;font-size:14px;font-weight:700;color:#2563eb" id="proj-total-1">8.65</td>
                <td style="padding:10px 0;text-align:right"><button onclick="showToast('Detailed score report for Stellar Drift')" style="font-size:11px;border:none;background:#eff6ff;color:#2563eb;border-radius:4px;padding:3px 8px;cursor:pointer">Details</button></td>
              </tr>
              <tr style="border-bottom:1px solid #f3f4f6">
                <td style="padding:10px 0;font-size:13px;font-weight:700;color:#6b7280">🥈</td>
                <td style="padding:10px 0">
                  <div style="font-size:13px;font-weight:700">Echo Protocol</div>
                  <div style="font-size:11px;color:#6b7280">Hollow Depths Studio</div>
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="8" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="7" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="8" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center;font-size:14px;font-weight:700;color:#2563eb" id="proj-total-2">7.65</td>
                <td style="padding:10px 0;text-align:right"><button onclick="showToast('Detailed score report for Echo Protocol')" style="font-size:11px;border:none;background:#eff6ff;color:#2563eb;border-radius:4px;padding:3px 8px;cursor:pointer">Details</button></td>
              </tr>
              <tr>
                <td style="padding:10px 0;font-size:13px;font-weight:700;color:#92400e">🥉</td>
                <td style="padding:10px 0">
                  <div style="font-size:13px;font-weight:700">Crystal Realms</div>
                  <div style="font-size:11px;color:#6b7280">Gemstone Games</div>
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="7" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="9" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center">
                  <input type="number" min="1" max="10" value="7" style="width:44px;border:1px solid #e5e7eb;border-radius:4px;padding:3px;font-size:12px;text-align:center" onchange="recalcProjectRanks()">
                </td>
                <td style="padding:10px 0;text-align:center;font-size:14px;font-weight:700;color:#2563eb" id="proj-total-3">7.70</td>
                <td style="padding:10px 0;text-align:right"><button onclick="showToast('Detailed score report for Crystal Realms')" style="font-size:11px;border:none;background:#eff6ff;color:#2563eb;border-radius:4px;padding:3px 8px;cursor:pointer">Details</button></td>
              </tr>
            </tbody>
          </table>
          <div style="margin-top:10px;display:flex;gap:8px">
            <button onclick="showToast('Score sheet exported to Excel')" class="btn-secondary" style="font-size:12px;padding:7px 14px">Export Scores</button>
            <button onclick="showToast('Winners announced to all projects')" class="btn-primary" style="font-size:12px;padding:7px 14px">Announce Winners</button>
          </div>
        </div>
      </div>
      <!-- ══ VIEW: Free Ticket ══ -->'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Project scoring leaderboard inserted")
else:
    idx = content.find('<!-- ══ VIEW: Free Ticket ══ -->')
    print(f"Free Ticket found at: {idx}")
    print(repr(content[idx-80:idx+20]))
