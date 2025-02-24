**GE Market Watch: Data Analysis**

Objective: Find safest profitable and highly-traded items.<br>
High-level Architecture: Gaz Lloyd's GEBot → weirdgloop API ⇆ Auto-Updater → Local DB ⇆ Data Analyzer ⇆ Data Distributor ⇆ Client Applications (e.g.; web browser, Discord, etc.).

Data Source/API List
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