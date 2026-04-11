with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''      </div>

      <!-- ══ VIEW: Game Showcase ══ -->'''

new_str = '''        <!-- Match Algorithm Visualizer -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">🤖 AI Match Score Breakdown</div>
            <span style="font-size:11px;background:#eff6ff;color:#2563eb;padding:3px 10px;border-radius:10px;font-weight:600">Powered by EventHQ AI</span>
          </div>
          <!-- Match pair selector -->
          <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap">
            <button id="match-pair-1" onclick="showMatchBreakdown(1)" style="font-size:11px;padding:4px 12px;border:none;border-radius:10px;cursor:pointer;background:#2563eb;color:#fff;font-weight:600">Sony × Indie Forge (96%)</button>
            <button id="match-pair-2" onclick="showMatchBreakdown(2)" style="font-size:11px;padding:4px 12px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">EA × Orbit Games (88%)</button>
            <button id="match-pair-3" onclick="showMatchBreakdown(3)" style="font-size:11px;padding:4px 12px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">Ubisoft × Veewo (74%)</button>
          </div>
          <div id="match-breakdown-panel">
            <!-- Match pair header -->
            <div style="display:flex;align-items:center;gap:16px;margin-bottom:16px;padding:12px;background:#f8f9fa;border-radius:8px">
              <div style="text-align:center">
                <div style="width:44px;height:44px;background:#dbeafe;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#1e40af;margin:0 auto">SI</div>
                <div style="font-size:11px;font-weight:600;margin-top:4px">Sony Interactive</div>
                <div style="font-size:10px;color:#6b7280">Publisher</div>
              </div>
              <div style="flex:1;text-align:center">
                <div style="font-size:28px;font-weight:800;color:#2563eb">96%</div>
                <div style="font-size:10px;color:#6b7280">Match Score</div>
                <div style="font-size:10px;background:#dcfce7;color:#16a34a;padding:2px 8px;border-radius:10px;display:inline-block;margin-top:4px;font-weight:600">Excellent Match</div>
              </div>
              <div style="text-align:center">
                <div style="width:44px;height:44px;background:#dcfce7;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#166534;margin:0 auto">IF</div>
                <div style="font-size:11px;font-weight:600;margin-top:4px">Indie Forge</div>
                <div style="font-size:10px;color:#6b7280">Developer</div>
              </div>
            </div>
            <!-- Score dimensions -->
            <div style="display:flex;flex-direction:column;gap:10px">
              <div>
                <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                  <span style="font-size:12px;font-weight:600">🎯 Genre Match</span>
                  <span style="font-size:12px;font-weight:700;color:#2563eb">100%</span>
                </div>
                <div style="background:#f3f4f6;border-radius:4px;height:8px;overflow:hidden">
                  <div style="width:100%;height:100%;background:linear-gradient(90deg,#2563eb,#60a5fa);border-radius:4px"></div>
                </div>
                <div style="font-size:10px;color:#9ca3af;margin-top:2px">Both specialize in Action/RPG titles</div>
              </div>
              <div>
                <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                  <span style="font-size:12px;font-weight:600">💰 Budget Alignment</span>
                  <span style="font-size:12px;font-weight:700;color:#16a34a">95%</span>
                </div>
                <div style="background:#f3f4f6;border-radius:4px;height:8px;overflow:hidden">
                  <div style="width:95%;height:100%;background:linear-gradient(90deg,#16a34a,#4ade80);border-radius:4px"></div>
                </div>
                <div style="font-size:10px;color:#9ca3af;margin-top:2px">Sony budget €2M-10M matches Indie Forge ask €3M</div>
              </div>
              <div>
                <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                  <span style="font-size:12px;font-weight:600">🌍 Market Overlap</span>
                  <span style="font-size:12px;font-weight:700;color:#9333ea">90%</span>
                </div>
                <div style="background:#f3f4f6;border-radius:4px;height:8px;overflow:hidden">
                  <div style="width:90%;height:100%;background:linear-gradient(90deg,#9333ea,#c084fc);border-radius:4px"></div>
                </div>
                <div style="font-size:10px;color:#9ca3af;margin-top:2px">Both target EU + NA + APAC markets</div>
              </div>
              <div>
                <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                  <span style="font-size:12px;font-weight:600">📅 Timeline Fit</span>
                  <span style="font-size:12px;font-weight:700;color:#d97706">85%</span>
                </div>
                <div style="background:#f3f4f6;border-radius:4px;height:8px;overflow:hidden">
                  <div style="width:85%;height:100%;background:linear-gradient(90deg,#d97706,#fbbf24);border-radius:4px"></div>
                </div>
                <div style="font-size:10px;color:#9ca3af;margin-top:2px">Sony Q3 2025 window aligns with Indie Forge Q4 launch</div>
              </div>
              <div>
                <div style="display:flex;justify-content:space-between;margin-bottom:4px">
                  <span style="font-size:12px;font-weight:600">🤝 Past Collaboration</span>
                  <span style="font-size:12px;font-weight:700;color:#6b7280">N/A</span>
                </div>
                <div style="background:#f3f4f6;border-radius:4px;height:8px;overflow:hidden">
                  <div style="width:0%;height:100%;background:#e5e7eb;border-radius:4px"></div>
                </div>
                <div style="font-size:10px;color:#9ca3af;margin-top:2px">First-time meeting — no prior history</div>
              </div>
            </div>
            <div style="margin-top:12px;display:flex;gap:8px">
              <button onclick="showToast('Meeting request sent to both parties')" class="btn-primary" style="font-size:12px;padding:7px 14px">Schedule Meeting</button>
              <button onclick="showToast('Match report exported to PDF')" class="btn-secondary" style="font-size:12px;padding:7px 14px">Export Report</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ══ VIEW: Game Showcase ══ -->'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Match algorithm visualizer inserted")
else:
    idx = content.find('<!-- ══ VIEW: Game Showcase ══ -->')
    print(f"Game Showcase found at: {idx}")
    print(repr(content[idx-60:idx+20]))
