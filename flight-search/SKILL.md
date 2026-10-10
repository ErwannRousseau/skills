---
name: flight-search
description:
  Compare flight options when the user asks to search, find, or price flights,
  vols, or billets d’avion. Collect travel dates, date flexibility, and a
  maximum budget before querying the configured trvl and OctoTrip Flights MCPs.
---

# Flight Search

Use this skill for flight searches and price comparisons. Complete the intake
before calling either search engine.

## Intake

Ask for all missing required details in one concise message:

- route: origin and destination (ask only when absent);
- dates: departure and return dates, or an explicit one-way request;
- flexibility: fixed dates or sliding dates; when sliding, ask the allowed
  window (for example, ±3 days);
- maximum budget: amount and currency, and whether it is per traveller or for
  the whole booking. If there is no cap, record “no budget cap”.

Do not search until dates, flexibility, and budget status are answered. Use one
adult in economy when passenger count or cabin is not provided, and state that
assumption in the result.

## Route normalization

Normalize both endpoints to concrete IATA codes before calling either MCP:

- `trvl` requires exactly three uppercase letters. Never pass a country name,
  city name, airport name, or lowercase text to its `search_flights` params.
- Treat a country-only endpoint such as `Thailand` as incomplete. Ask for a
  city or airport (for example, Bangkok BKK/DMK or Phuket HKT).
- When a city has multiple airports, ask the user to choose or run one search
  per explicit airport code. Reuse the selected codes for both MCPs.
- Validate `origin` and `destination` against `^[A-Z]{3}$` before calling
  `trvl`; if either value fails, ask for clarification instead of searching.

## Search

Always query both configured MCPs; if one fails, report the failure explicitly
and keep the other result.

- `trvl`: call the `travel` MCP tool with `intent: "search_flights"` and
  `params` containing `origin`, `destination`, `departure_date`, and (for round
  trips) `return_date`. Pass the budget as numeric whole currency units in
  `max_price` when the tool accepts it; keep formatted amounts out of the MCP
  payload.
- `octotrip-flights`: call its `search` MCP tool with `origin`, `destination`,
  `departure_date`, and `return_date`.

Use these MCPs as the flight-search sources. Do not silently replace them with a
direct provider, another MCP, an API key, or an account.

The configured `trvl` entry uses `scripts/trvl-codex-bridge.py`. It removes
optional `resource_link` blocks and content `annotations` that the bundled
Codex MCP decoder rejects, while preserving the text and `structuredContent`
flight results.
After changing this configuration, fully quit and reopen the Codex/ChatGPT app,
then start a new chat so the MCP server reconnects. Opening another chat without
restarting can reuse the already-running server configured with the old command;
`codex mcp get trvl` only confirms the file on disk and does not restart that
process.
The global entry also sets `tool_timeout_sec = 120`: a valid live search can
take a little over Codex's former 30-second default.
Do not run `trvl mcp install --client codex --force` afterward: the official
installer would replace the bridge with the direct `trvl mcp` command.

If `trvl` reports `invalid IATA code` or `Unexpected response type`, verify that
the call used `travel` with `intent: "search_flights"` and valid IATA params,
then retry once with that structured call. Never retry with the original city or
country string; for the response-type error, also verify `codex mcp get trvl`
points to the bridge, fully restart the app, and retry in a new chat before
reporting the server unavailable. If the error arrives after roughly 30 seconds,
treat it as a timeout and ask for the full app restart after the timeout change.

For sliding dates, never invent a window. Search a compact set of date pairs
inside the user’s window (use trvl date search when useful, then check the best
candidates with OctoTrip) and label the dates actually searched.

## Result

Compare prices in one currency and show a compact table with engine, dates,
airline/provider, stops, total price, and booking link when supplied. For every
round-trip option, show two separate elapsed journey durations:

- `aller`: first departure to final arrival at the destination, including every
  layover;
- `retour`: first departure at the destination to final arrival at the origin,
  including every layover.

Keep airborne flight time separate when the provider supplies it. Never use a
round-trip sum as the only duration. Prefer segment departure/arrival
timestamps and airport time zones to compute each elapsed duration; label the
timestamps as local and mark the duration unavailable when the data is
incomplete or inconsistent. Mark options within the stated budget; label
estimates, missing prices, partial results, and provider failures instead of
treating them as zero results. Report each engine’s result count, including
when one engine is unavailable.

Do not book, pay, create an account, or request an API key. Finish only after
both MCPs have been queried (or one’s unavailability is explicit) and the answer
reflects the user’s dates, flexibility, and budget.
