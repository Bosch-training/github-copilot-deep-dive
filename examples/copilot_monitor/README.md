# Copilot Token Monitor

Live token usage from GitHub Copilot Chat in VS Code, via OpenTelemetry.

## Run
    pip install fastapi uvicorn opentelemetry-proto python-dotenv
    uvicorn server:app --port 4318
    # open http://localhost:4318

## Point VS Code at it (settings.json)
    "github.copilot.chat.otel.enabled": true,
    "github.copilot.chat.otel.exporterType": "otlp-http",
    "github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"

Then use Copilot Chat; each LLM call appears in the UI. Prompt content is not
exported unless `github.copilot.chat.otel.captureContent` is true.

## Test without Copilot
    curl -X POST localhost:4318/demo -H 'content-type: application/json' \
         -d '{"model":"gpt-4o","input_tokens":1200,"output_tokens":340}'

## Notes
- Data comes from Copilot's OTel *metrics* (`gen_ai.client.token.usage`), exported every ~10s.
  Only usage since the monitor started is shown; earlier session history is skipped.
- Background calls (e.g. a small model for chat titles) appear as their own model rows.
- `ms` is the average duration per call in that interval.

## LLM-as-judge (optional)
By default each finished prompt can be scored 1-5 on **correctness** and **instruction following** by a
judge model via OpenRouter. It needs `github.copilot.chat.otel.captureContent: true`.

    cp .env.example .env     # then edit .env (git-ignored)
    .venv/bin/uvicorn server:app --port 4318

**Run without the judge:** leave `OPENROUTER_API_KEY` empty, or set `JUDGE_ENABLED=false`. No key or model
is needed. The judge columns disappear and the quality column uses your own star ratings instead.
Everything else (tokens, prompts per run, runs and conditions) works the same.

With the judge on, the prompt and answer text (not the system context) are sent to OpenRouter.
Pick `JUDGE_MODEL` from a different family than the models you compare.

