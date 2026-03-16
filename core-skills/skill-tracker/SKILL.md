---
name: skill-tracker
description: This skill is ALWAYS ON. It tracks and displays all skills invoked during the conversation. It activates automatically on every skill invocation.
version: 3.0.0
---

# Skill Tracker (技能追踪器) - Always On

This skill automatically tracks and displays ALL skills that have been invoked during the conversation. **It is ALWAYS ON.**

## When This Skill Applies

**CRITICAL**: This skill is ALWAYS ACTIVE. Every time any skill is used, this tracker MUST display the skill usage.

## How It Works

### 1. Automatic Tracking
- Every time a skill is invoked (via Skill tool), this tracker activates
- Shows a visual skill card/banner in the conversation
- Tracks: skill name, category, timestamp, and running count

### 2. Display Format

```
┌─────────────────────────────────────┐
│ 🔧 SKILL TRACKED                    │
│ ─────────────────────────────────── │
│ Name: [skill-name]                  │
│ Category: [category]                │
│ Time: [timestamp]                   │
│ Total Used: [count]                 │
└─────────────────────────────────────┘
```

### 3. Summary View
User can say "显示追踪" or "show tracking" to see full history.

## Usage

This skill runs automatically in the background. No manual activation needed.

## Example Output

When `god-mode` is invoked:
```
╔════════════════════════════════════════╗
║  🔧 SKILL TRACKED                     ║
║  ───────────────────────────────────  ║
║  📌 Name: god-mode                    ║
║  📂 Category: research/ai              ║
║  ⏰ Time: 2026-03-16 20:45:00          ║
║  🔢 Total Used: 3                      ║
╚════════════════════════════════════════╝
```

## Data Storage

Tracking data: `~/.claude/skill_tracker.json`

### Tree Structure Logic:
- Each skill invocation creates a new child node
- Main skill is the root, called sub-skills are children
- Track: parent → child relationships
- Display call stack as tree branches

### Data Structure:
```json
{
  "tree": [
    {"id": 1, "name": "skill-manager", "parent": null},
    {"id": 2, "name": "gemini-mcp", "parent": 1},
    {"id": 3, "name": "simplify", "parent": 2},
    {"id": 4, "name": "gemini-mcp", "parent": 1}
  ],
  "stats": {"skill-manager": 1, "gemini-mcp": 2, "simplify": 1}
}
```

---

## 📋 会话末尾显示 (Always Show at End)

**CRITICAL**: This skill MUST automatically display the tree at the END of EVERY response (after my main reply).

### Display Behavior:
1. **ALWAYS show after every response** - No triggers needed
2. Show tree structure with call hierarchy
3. Display after "📊 SKILL FLOW TREE" header
4. Keep it brief but informative

### Summary Format - Tree Structure:

```
╔═══════════════════════════════════════════════════════════════════════╗
║  📊 SKILL FLOW TREE (技能调用流程树)                                  ║
║  ════════════════════════════════════════════════════════════════════════╝
│
├─ 📍 skill-manager (起点)
│   │
│   ├─ 📍 gemini-mcp
│   │   │
│   │   └─ 📍 simplify
│   │
│   └─ 📍 gemini-mcp
│
└─ 📍 skill-tracker (终点)

════════════════════════════════════════════════════════════════════════
📈 Summary: skill-manager(1) → gemini-mcp(2) → simplify(1)
📊 Total: 4 skills | Depth: 3
════════════════════════════════════════════════════════════════════════
```

### How to View:
- Say "显示追踪" / "show tracking" / "追踪"
- Say "结束" / "done" to see summary before ending
