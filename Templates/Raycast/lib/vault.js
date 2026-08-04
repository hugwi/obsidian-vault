// Reading the vault from outside Obsidian.
//
// Raycast runs these scripts while Obsidian may not even be open, so there is no
// metadataCache and no Dataview to ask — the frontmatter has to be parsed off disk.
// What counts as a *project* is still decided by `isProjectHub` in the Templater
// script, so this file adds a reader, not a second definition.

const fs = require("fs");
const path = require("path");

const { isProjectHub, normalizeStatus } = require("../../Templater/projects.js");

// The scripts live inside the vault, so the vault root is just up the tree — nothing
// to configure, and it keeps working when the vault is moved or cloned elsewhere.
const vaultRoot = () => path.resolve(__dirname, "../../..");

// Folders with no project notes in them. Skipping them keeps a 900-note vault fast
// enough that Raycast feels instant.
const SKIP = new Set(["Attachments", "Templates", "Daily", "Clippings", "node_modules"]);

// A deliberately small YAML subset: scalars and block lists, which is all this vault's
// frontmatter uses. Enough for `categories`, `project` and `status`; a full parser
// would mean a dependency, and these scripts have none.
function parseFrontmatter(content) {
    const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);

    if (!match) {
        return null;
    }

    const frontmatter = {};
    let key = null;

    for (const line of match[1].split(/\r?\n/)) {
        const item = line.match(/^\s*-\s+(.*)$/);

        if (item && key) {
            frontmatter[key] = [...(Array.isArray(frontmatter[key]) ? frontmatter[key] : []),
                unquote(item[1])];

            continue;
        }

        const pair = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);

        if (!pair) {
            continue;
        }

        key = pair[1];

        const value = pair[2].trim();

        // `key:` with nothing after it opens a block list — or is simply empty.
        frontmatter[key] = value === "" ? [] : unquote(value);
    }

    return frontmatter;
}

function unquote(value) {
    const trimmed = value.trim();

    if (/^\[.*\]$/.test(trimmed)) {
        // Inline list: ["[[Projects]]", "x"]
        return trimmed.slice(1, -1)
            .split(",")
            .map(unquote)
            .filter(Boolean);
    }

    return trimmed.replace(/^["']|["']$/g, "").trim();
}

function markdownFiles(dir, found = []) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        if (entry.name.startsWith(".")) {
            continue;
        }

        const full = path.join(dir, entry.name);

        if (entry.isDirectory()) {
            if (!SKIP.has(entry.name)) {
                markdownFiles(full, found);
            }
        } else if (entry.name.endsWith(".md")) {
            found.push(full);
        }
    }

    return found;
}

const STATUS_ORDER = ["active", "pursue", "paused", "done"];

// Same shape and same ordering as the in-Obsidian picker: active first, then
// alphabetical, so muscle memory transfers between the two.
function findHubs(root = vaultRoot()) {
    return markdownFiles(root)
        .map((file) => ({
            path: file,
            name: path.basename(file, ".md"),
            frontmatter: parseFrontmatter(fs.readFileSync(file, "utf8")),
        }))
        .filter((entry) => !entry.name.includes("Template"))
        .filter((entry) => isProjectHub(entry.frontmatter, entry.name))
        .map((entry) => ({
            ...entry,
            status: normalizeStatus(entry.frontmatter.status),
        }))
        .sort((a, b) => STATUS_ORDER.indexOf(a.status) - STATUS_ORDER.indexOf(b.status) ||
            a.name.localeCompare(b.name));
}

// Typed by hand in a Raycast field, so it has to be forgiving — but never guess when
// the answer is unclear: writing a capture into the wrong project loses it silently.
function matchProject(hubs, query) {
    const needle = String(query ?? "").trim().toLowerCase();

    if (!needle) {
        return { none: true };
    }

    const exact = hubs.filter((hub) => hub.name.toLowerCase() === needle);

    if (exact.length === 1) {
        return { hub: exact[0] };
    }

    for (const test of [
        (name) => name.startsWith(needle),
        (name) => name.includes(needle),
    ]) {
        const found = hubs.filter((hub) => test(hub.name.toLowerCase()));

        if (found.length === 1) {
            return { hub: found[0] };
        }

        if (found.length > 1) {
            return { ambiguous: found };
        }
    }

    return { none: true };
}

const today = (now = new Date()) => [
    now.getFullYear(),
    String(now.getMonth() + 1).padStart(2, "0"),
    String(now.getDate()).padStart(2, "0"),
].join("-");

// Obsidian forbids these in filenames; the rest of the title is left alone so the
// note is still called what you typed.
function safeFilename(text, limit = 60) {
    const firstLine = String(text).split("\n")[0].trim();

    return firstLine
        .replace(/[\\/:*?"<>|#^[\]]/g, "")
        .replace(/\s+/g, " ")
        .slice(0, limit)
        .trim();
}

module.exports = {
    findHubs,
    matchProject,
    parseFrontmatter,
    safeFilename,
    today,
    vaultRoot,
};
