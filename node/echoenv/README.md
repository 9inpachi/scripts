# echoenv

[![Version](https://img.shields.io/npm/v/echoenv.svg)](https://www.npmjs.com/package/echoenv)
[![Downloads](https://img.shields.io/npm/dt/echoenv.svg)](https://www.npmjs.com/package/echoenv)

A CLI to echo commands for setting environment variables from .env files.

## Setup

Install.

```sh
npm install echoenv --global
# or
yarn global add echoenv
```

Or use npx.

```sh
npx echoenv <file>
```

## Usage

```
echoenv [--env <environment>] <file>

Options:
  --env     (bash, powershell, cmd)
            Environment for which to echo variables.
            Inferred if not specified (only for Bash and Powershell).
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

```sh
export ENV_VARIABLE1=TEST_VALUE1
export ENV_VARIABLE2=TEST_VALUE2
export ENV_VARIABLE3=TEST_VALUE3
export ENV_VARIABLE4=TEST_VALUE4
```

### Echo Powershell Commands:

`echoenv --env powershell test.env`

```powershell
$env:ENV_VARIABLE1="TEST_VALUE1"
$env:ENV_VARIABLE2="TEST_VALUE2"
$env:ENV_VARIABLE3="TEST_VALUE3"
$env:ENV_VARIABLE4="TEST_VALUE4"
```

### Echo CMD Commands

`echoenv --env cmd test.env`

```cmd
set ENV_VARIABLE1=TEST_VALUE1
set ENV_VARIABLE2=TEST_VALUE2
set ENV_VARIABLE3=TEST_VALUE3
set ENV_VARIABLE4=TEST_VALUE4
```
