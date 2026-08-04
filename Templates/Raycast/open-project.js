#!/usr/bin/env node

// Required parameters:
// @raycast.schemaVersion 1
// @raycast.title Open project
// @raycast.mode silent
//
// Optional parameters:
// @raycast.icon 📂
// @raycast.packageName Obsidian
// @raycast.argument1 { "type": "text", "placeholder": "project" }
//
// Documentation:
// @raycast.description Open a project note in Obsidian. Unlike capture, this one is meant to pull you in.
// @raycast.author Hugo

const { execFileSync } = require("child_process");
const path = require("path");

const { findHubs, matchProject, vaultRoot } = require("./lib/vault.js");

// The vault's display name, which is not necessarily its folder name. Overridable so
// this file is not wrong on a machine where the vault was added under another name.
const vaultName = () => process.env.OBSIDIAN_VAULT || "hugwi";

function uriFor(root, hub, name = vaultName()) {
    const relative = path.relative(root, hub.path).replace(/\.md$/, "");

    return `obsidian://open?vault=${encodeURIComponent(name)}` +
        `&file=${encodeURIComponent(relative)}`;
}

// `root` is a parameter so the test can drive a throwaway vault; Raycast never
// passes it.
function main(argv, root = vaultRoot()) {
    const match = matchProject(findHubs(root), argv.join(" "));

    if (!match.hub) {
        const names = (match.ambiguous ?? []).map((hub) => hub.name).join(", ");

        return {
            message: match.ambiguous
                ? `Ambiguous: ${names}`
                : "No project matches that",
            code: 1,
        };
    }

    execFileSync("open", [uriFor(root, match.hub)]);

    return { message: match.hub.name, code: 0 };
}

if (require.main === module) {
    const { message, code } = main(process.argv.slice(2));

    console.log(message);
    process.exit(code);
}

module.exports = { main, uriFor };
