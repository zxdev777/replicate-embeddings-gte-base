Request

```console
curl http://localhost:5000/predictions -X POST \
    -H 'Content-Type: application/json' \
    -d '{"input": {"text": "AI: What do you do ?\n Human: I am programmer!"}}'
```

Response

```javascript
{
    "input": {
        "text": "AI: What do you do ?\n Human: I am programmer!"
    },
    "output": {
        "items": [
            {
                "text": "AI: What do you do ?",
                "embedding": [
                    0.009306900203227997,
                    0.013707865960896015,
                    ...,
                    -0.035225287079811096
                ]
            },
            {
                "text": "Human: I am programmer!",
                "embedding": [
                    0.016468646004796028,
                    0.010022704489529133,
                    ...,
                    -0.006993232760578394
                ]
            }
        ]
    },
    "id": null,
        "version": null,
        "created_at": null,
        "started_at": "2023-12-23T11:06:39.054613+00:00",
        "completed_at": "2023-12-23T11:06:39.366047+00:00",
        "logs": "",
        "error": null,
        "status": "succeeded",
        "metrics": {
        "predict_time": 0.311434
    },
    "webhook": null,
        "output_file_prefix": null,
        "webhook_events_filter": [
        "start",
        "output",
        "logs",
        "completed"
    ]
}
```
