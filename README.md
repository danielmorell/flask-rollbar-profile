# Test Rollbar Profiling Flask App

This is a simple Flask app that helps profile Rollbar's Python SDK.

## Setup

1. Clone this repo.
2. Create a virtualenv `<python version> -m virtualenv venv`.
3. Activate the virtualenv `source venv/bin/activate`.
4. Create a virtualenv and install the requirements with `pip install -r requirements.txt`.
5. Start the app with `flask run`.
6. Run multiple profiles by executing `test.sh`.
7. View the results with `snakeviz pstat/<profile>.prof`.

There are four extra wheels available:

```text
wheels
├── rollbar-0.16.4b0-py3-none-any.whl  # The current version of the SDK
├── rollbar-batched-literals.whl       # The SDK with batched-transform and literals
├── rollbar-batched-transform.whl      # The SDK with batched-transform
└── rollbar-literals.whl               # The current version of the SDK with just literals.
```

You can install an alternate version of the Rollbar SDK by running `pip install ./wheels/<wheel file>`.

## The Literals

The versions marked as literals use literal types instead of the type functions
for the `transform()` method in `rollbar/lib/traverse.py`. e.g.

```diff
- dict((k, traverse(v, key=key + (k,), **kw)) for k, v in iteritems(obj)),
+ {(k, traverse(v, key=key + (k,), **kw)) for k, v in iteritems(obj)},
```

Generally, using a literal type is faster than using the type function. However,
in this instance it appeared to be much faster than I expected. Probably because
we run through this code so many times.

I included a fresh set of profiles for each of these versions. The results are
in the `pstat` directory organized by the version of the SDK.
