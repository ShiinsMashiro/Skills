---
name: skill-tracker
description: This skill should be used when the user wants to "追踪skills", "显示使用的skills", "记录skills使用", "show used skills", "track skills", "自动记录", "auto track", "在对话中显示skills", "display skills in conversation", "skills使用记录".
version: 1.0.0
---

# Skill Tracker (技能追踪器)

This skill automatically tracks and displays all skills that have been invoked during the conversation, showing them directly in the conversation.

## When This Skill Applies

This skill activates when the user wants to:
- Automatically track all skills used in the conversation
- See skills displayed directly in the chat
- Enable auto-tracking mode for skill monitoring
- View skill usage history at any time

## How Auto-Tracking Works

**Step 1: Enable Tracking**
User says: "开启技能追踪" or "enable auto track"

**Step 2: Automatic Display**
Each time a skill is invoked after tracking is enabled:
- I will display a visual skill card/banner in the conversation
- Show skill name, category, and timestamp
- Include a running count

**Step 3: View Summary**
User can say "显示追踪列表" or "show tracking" to see all tracked skills

## Visual Display Format

When a skill is used, display it like this:

```
┌─────────────────────────────────────┐
│ 🔧 Skill Used                       │
│ Name: [skill-name]                  │
│ Category: [scientific/custom/etc]   │
│ Time: [timestamp]                   │
└─────────────────────────────────────┘
```

## Output

Creates a tracking session that:
1. Shows skill invocation in real-time in conversation
2. Maintains a running list of all skills used
3. Can generate an HTML summary page on demand
4. Tracks total invocation count per skill

## File Location

Tracking data saved to:
`C:\Users\黄涂健隆\Desktop\ClaudeCode\disc-generator\skill_tracking.json`

HTML display page:
`C:\Users\黄涂健隆\Desktop\ClaudeCode\disc-generator\skill_tracker.html`

## Usage Examples

- "开启技能追踪"
- "开始追踪skills"
- "enable auto track"
- "显示追踪列表"
- "show tracking"
- "我的skills使用记录"

## Tracking Banner Template

Each skill use displays:

╔════════════════════════════════════════╗
║  🔧 SKILL TRACKED                       ║
║  ─────────────────────────────────────  ║
║  📌 Name: [skill name]                  ║
║  📂 Category: [category]                ║
║  ⏰ Time: [current time]                ║
║  🔢 Total Used: [count]                 ║
╚════════════════════════════════════════╝

## Notes

- Auto-tracking starts when user enables it
- All subsequent skill invocations will be displayed
- User can disable tracking anytime
- A summary can be generated at any time
