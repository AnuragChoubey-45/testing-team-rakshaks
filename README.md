# Harness Baseline-Creation Benchmark v3

## Purpose

This benchmark is specifically designed to test whether an AI coding/debugging harness can:

1. Create a runtime behavioral baseline from a known-good repository state.
2. Detect that the current state differs from that baseline.
3. Trace the changed behavior across files.
4. Send focused evidence to the LLM.
5. Repair the regression.
6. Re-run the baseline scenarios and verify that behavior has been restored.

**There is intentionally NO pre-generated expected behavior file.**

The benchmark's expected behavior must be obtained by executing the healthy baseline commit.

## Repository history

The Git repository contains:

- `baseline` tag: known-good implementation
- `HEAD`: intentionally mutated implementation

The mutation is deliberately subtle: the normal test suite does not exercise the premium discount path.

The important business flow is:

`checkout.py -> pricing.py -> customer.py`

## User issue

Give your harness exactly this:

> Premium customers are getting the wrong final price. Premium customers should receive a 20% discount.

Do NOT tell the harness the exact constant or file to edit. The harness should discover the behavior.

## Required baseline experiment

Before allowing the harness to patch the current code, it should establish runtime behavior from the healthy baseline.

Conceptually:

1. Resolve the known-good baseline (`baseline` tag / parent commit).
2. Execute representative scenarios against that baseline.
3. Record observed outputs as baseline behavior.
4. Return to the broken working state.
5. Execute the same scenarios.
6. Compare baseline vs current behavior.
7. Localize the changed behavior.
8. Ask the model for a minimal repair.
9. Apply the repair.
10. Execute the same scenarios again.
11. Verify behavior matches the baseline.

The benchmark does NOT provide a golden answer. The baseline is the source of truth.

## Representative scenarios

The repository exposes:

`python3 benchmark/scenarios.py`

This script prints deterministic JSON for scenarios including:

- regular customer, subtotal 1000
- premium customer, subtotal 1000
- premium customer, subtotal 500
- regular customer, subtotal 500

Your harness may use this script, import the application directly, or construct its own equivalent runtime probes.

## Important

`tests/` deliberately does NOT test the premium discount behavior. Therefore:

```bash
python3 -m pytest -q
```

can remain green even though the business behavior is wrong.

That is intentional.

## Manual reference check

For benchmark authors only, you can inspect the known-good state with:

```bash
git show baseline:app/pricing.py
```

and run the scenario script at that commit.

The harness should discover the baseline behavior through execution rather than relying on this documentation.

## Success criteria

A successful harness run should be able to show evidence for:

- baseline created from healthy code
- baseline runtime outputs
- current runtime outputs
- behavioral difference
- relevant dependency chain
- focused model context
- repair
- post-repair outputs matching the baseline

A test that only says "pytest passed" is NOT sufficient for this benchmark.
