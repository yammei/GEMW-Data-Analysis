<h1>GEMW Data Analysis</h1>

Hi! This is a personal project for a game I play -RuneScape 3. It's mainly to analyze item trends so that players can decide whether any specific tradeable item is a good investment or not. 
I'm using Python for most of the project, potentially some SQL once the data starts getting heavy.

<hr>

<img src="https://github.com/yammei/GEMW-Data-Analysis/blob/main/data/Samples/MPLA_Blood%20rune_2025-02-24.jpg">

_Figure 1: 90 day analysis on Blood rune(s)._

<hr>

<h3>High-level Architecture</h3>
Gaz Lloyd's GEBot → weirdgloop API ⇆ Auto-Updater → Local DB ⇆ Data Analyzer ⇆ Data Distributor ⇆ Client Applications (e.g.; web browser, Discord, etc.).

<hr>

<h3>Data Source/API List</h3>

```json
{
    "GEMW_all_past_day": "https://chisel.weirdgloop.org/gazproj/gazbot/rs_dump.json",
    "GEMW_all_past_90_days": "https://api.weirdgloop.org/exchange/history/rs/last90d",
    "GEMW_all_name_to_trade_volume": "https://runescape.wiki/?title=Module:GEVolumes/data.json&action=raw&ctype=application%2Fjson",
    "GEMW_all_name_to_id": "https://runescape.wiki/?title=Module:GEIDs/data.json&action=raw&ctype=application%2Fjson",
    "GEMW_all_name_to_limit": "https://runescape.wiki/?title=Module:GELimits/data.json&action=raw&ctype=application%2Fjson",
    "GEMW_all_name_to_last_price": "https://runescape.wiki/?title=Module:GEPrices/data.json&action=raw&ctype=application%2Fjson"
}
```

