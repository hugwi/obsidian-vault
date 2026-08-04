#!/usr/bin/env node

// Required parameters:
// @raycast.schemaVersion 1
// @raycast.title Capture to project
// @raycast.mode compact
//
// Optional parameters:
// @raycast.icon 🎯
// @raycast.packageName Obsidian
// @raycast.argument1 { "type": "text", "placeholder": "project (blank = new note)", "optional": true }
// @raycast.argument2 { "type": "text", "placeholder": "what happened" }
//
// Documentation:
// @raycast.description Append a dated line to a project's ## Log, or make a new Inbox note. Obsidian need not be running.
// @raycast.author Hugo

const fs = require("fs");
const path = require("path");

const { logInsertion } = require("../Templater/captureToProject.js");
const {
    findHubs,
    matchProject,
    safeFilename,
    today,
    vaultRoot,
} = require("./lib/vault.js");

function captureToProject(hub, text, date) {
    const entry = `- ${date} — ${text}`;
    const { content } = logInsertion(fs.readFileSync(hub.path, "utf8"), entry);

    fs.writeFileSync(hub.path, content);

    return `→ ${hub.name}`;
}

function captureToNewNote(root, text, date) {
    const title = safeFilename(text) || `Capture ${date}`;
    let file = path.join(root, `${title}.md`);
    let attempt = 2;

    // Never overwrite: a capture that silently replaced a note would be the worst
    // possible failure for a tool you use without looking.
    while (fs.existsSync(file)) {
        file = path.join(root, `${title} ${attempt}.md`);
        attempt += 1;
    }

    const body = [
        "---",
        `created: ${date}`,
        "categories:",
        '  - "[[Inbox]]"',
        "tags:",
        "---",
        "",
        text,
        "",
    ].join("\n");

    fs.writeFileSync(file, body);

    return `→ ${path.basename(file, ".md")}`;
}

// `root` is a parameter so the test can drive a throwaway vault; Raycast never
// passes it.
function main(argv, root = vaultRoot()) {
    const [query = "", ...rest] = argv;
    const text = rest.join(" ").trim();

    if (!text) {
        return { message: "Nothing to capture.", code: 1 };
    }

    const date = today();

    if (!String(query).trim()) {
        return { message: captureToNewNote(root, text, date), code: 0 };
    }

    const match = matchProject(findHubs(root), query);

    if (match.hub) {
        return { message: captureToProject(match.hub, text, date), code: 0 };
    }

    // Refuse rather than guess — and say what would have worked.
    const names = (match.ambiguous ?? []).map((hub) => hub.name).join(", ");

    return {
        message: match.ambiguous
            ? `"${query}" matches ${names}`
            : `No project matches "${query}"`,
        code: 1,
    };
}

if (require.main === module) {
    const { message, code } = main(process.argv.slice(2));

    console.log(message);
    process.exit(code);
}

module.exports = { main, captureToProject, captureToNewNote };
