#!/usr/bin/env node

const { existsSync, readFileSync } = require("fs");
const { basename } = require("path");

main();

function main() {
  const fileName = process.argv[process.argv.length - 1].trim();
  validateFile(fileName);
  const { env } = parseOptions.apply();

  const fileContents = readFileSync(fileName, { encoding: "utf-8" });
  const output = convertContentToCommands(env, fileContents);

  console.log(output);
}

function parseOptions() {
  if (process.argv.includes("--help")) {
    displayUsage();
  }

  const envIndex = process.argv.indexOf("--env");
  const env = envIndex > 0 ? process.argv[envIndex + 1] : inferEnvironment();

  return { env };
}

function validateFile(fileName) {
  const scriptName = basename(__filename);
  if (fileName.includes(scriptName) || !existsSync(fileName)) {
    displayUsage("Unable to find the specified file.");
  }
}

function convertContentToCommands(env, rawContent) {
  let commands = [];
  const buildCommand = getBuildCommandFunction(env);

  for (let variable of rawContent.split("\n")) {
    variable = variable.trim();

    if (variable === "" || variable.startsWith("#")) {
      continue;
    }

    const [key, value] = variable.split("=").map((value) => value.trim());

    commands.push(buildCommand(key, value));
  }

  return commands.join("\n");
}

function getBuildCommandFunction(env) {
  switch (env) {
    case "bash":
      return buildBashCommand;
    case "powershell":
      return buildPowershellCommand;
    case "cmd":
      return buildCmdCommand;
    default:
      displayUsage();
  }
}

function buildPowershellCommand(key, value) {
  return `$env:${key}="${value}"`;
}

function buildBashCommand(key, value) {
  return `export ${key}=${value}`;
}

function buildCmdCommand(key, value) {
  return `set ${key}=${value}`;
}

function inferEnvironment() {
  if (process.env.SHELL && process.env.SHELL.includes("sh")) {
    return "bash";
  }

  return "powershell";
}

function displayUsage(message) {
  if (message) {
    console.log("\n" + message);
  }

  console.log(`
Usage:
  echoenv [--env <environment>] <file>

Options:
  --env     (bash, powershell, cmd) environment for which to echo variables. Inferred if not specified.
  --help
`);

  process.exit(1);
}
