# echoenv

A CLI to echo commands for setting environment variables from .env files.

## Usage

```
echoenv [--env <environment>] <file>

Options:
  --env     (bash, powershell, cmd) environment for which to echo variables. Inferred if not specified.
  --help
```

## Examples

`test.env`

```
ENV_VARIABLE1=TEST_VALUE1
ENV_VARIABLE2=TEST_VALUE2
ENV_VARIABLE3=TEST_VALUE3
ENV_VARIABLE4=TEST_VALUE4
```

### Echo Bash Commands

`echoenv --env bash test.env`

```
export ENV_VARIABLE1=TEST_VALUE1
export ENV_VARIABLE2=TEST_VALUE2
export ENV_VARIABLE3=TEST_VALUE3
export ENV_VARIABLE4=TEST_VALUE4
```

### Echo Powershell Commands:

`echoenv --env powershell test.env`

```
$env:ENV_VARIABLE1="TEST_VALUE1"
$env:ENV_VARIABLE2="TEST_VALUE2"
$env:ENV_VARIABLE3="TEST_VALUE3"
$env:ENV_VARIABLE4="TEST_VALUE4"
```

### Echo CMD Commands

`echoenv --env cmd test.env`

```
set ENV_VARIABLE1=TEST_VALUE1
set ENV_VARIABLE2=TEST_VALUE2
set ENV_VARIABLE3=TEST_VALUE3
set ENV_VARIABLE4=TEST_VALUE4
```
