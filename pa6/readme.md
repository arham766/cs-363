# PA6 — Float Support, Static Type System & String Data Types

## Features Added

1. **Float support** — `f` declares float variables, float literals like `3.14` supported in expressions
2. **Static type system** — rejects mixing of int, float, and string types in expressions and assignments
3. **String data type** — `s` declares string variables, `[text]` bracket syntax for string literals, stored to registers and printed

## How It Works

- `tokens.py` — added `FLOATDEC`, `FLOATLIT`, `STRDEC`, `STRLIT` token types
- `tokenizer.py` — `f` and `s` as keywords, float literal scanning, `[...]` string scanning
- `acdcast.py` — added `FloatDclNode`, `FloatLitNode`, `StrDclNode`, `StrLitNode` AST nodes
- `parser.py` — handles float/string declarations and literals in expressions
- `semantic.py` — tracks variable types, rejects type mixing (int+float, arithmetic on strings, wrong-type assignments)
- `codegen.py` — emits float values and `[text]` for dc

## Test Results

- 15 passing tests (test0–test14): all PASS
- 15 failing tests (testfail0–testfail14): all correctly rejected
- **30/30 total tests passed, 0 failed**

Run tests: `python test_runner.py`