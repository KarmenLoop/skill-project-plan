# Input and output

English | [简体中文](input.zh-CN.md)

Supply a UTF-8 JSON object (maximum 10 MiB). Use `--input PATH` for a file or `--input -` for standard input. Run `--version` to inspect the installed helper version. Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| tasks | Objects: unique id, title, duration (positive number), depends_on array of IDs, acceptance nonempty string, optional owner. |

## Example

```json
{
  "tasks": [
    {
      "id": "a",
      "title": "Inspect interface",
      "duration": 1,
      "depends_on": [],
      "acceptance": "Contract documented"
    },
    {
      "id": "b",
      "title": "Implement adapter",
      "duration": 3,
      "depends_on": [
        "a"
      ],
      "acceptance": "Example request succeeds"
    },
    {
      "id": "c",
      "title": "Validate failure path",
      "duration": 2,
      "depends_on": [
        "b"
      ],
      "acceptance": "Timeout and cancellation verified"
    }
  ]
}
```

## Result

ordered_tasks with earliest_start/finish, critical_path IDs, and estimated_duration.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
