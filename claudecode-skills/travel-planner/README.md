# Travel Planner Skill for Claude Code

A comprehensive travel planning skill that creates complete travel guides with transportation, accommodation, day-by-day itineraries, and practical information.

## Features

- **Transportation Planning** - Flights (via Kiwi.com MCP), trains, buses, ferries
- **Accommodation Search** - Hotels, hostels, Airbnb with area recommendations
- **Itinerary Design** - Day-by-day schedules with attractions and dining
- **Practical Guides** - Visa, currency, language phrases, local tips
- **Budget Planning** - Cost breakdowns and money-saving tips

## Installation

### 1. Add the Kiwi.com MCP Server (Required for flight search)

```bash
claude mcp add kiwi-com --transport http https://mcp.kiwi.com
```

### 2. Install the Skill

Download `SKILL.md` and add it to your Claude Code skills directory, or install directly:

```bash
# Clone this repo
git clone https://github.com/cheng-chun-yuan/claude-travel-planner-skill.git

# Copy to your skills directory
cp claude-travel-planner-skill/SKILL.md ~/.claude/skills/travel-planner.md
```

## Usage

Simply ask Claude Code to help you plan a trip:

- "Plan a 5-day trip to Tokyo"
- "Find flights from Taipei to Kuala Lumpur on Jan 30"
- "Create a travel guide for Barcelona"
- "Where should I stay in Seoul?"

## Output Example

The skill generates comprehensive travel guides including:

1. **Getting There** - Flight options with prices and booking links
2. **Where to Stay** - Hotel recommendations by budget level
3. **Getting Around** - Local transport options and transit cards
4. **Day-by-Day Itinerary** - Detailed schedules with activities
5. **Practical Information** - Currency, language, emergency contacts
6. **Budget Summary** - Cost breakdown for the entire trip
7. **Booking Checklist** - Pre-trip preparation items
8. **Quick Reference** - Essential info card

## License

MIT License - Feel free to use and modify.

## Contributing

Pull requests welcome! Please keep the skill minimal and focused on core functionality.
