// Builds a throwaway vault in a temp dir and drives the Raycast scripts exactly the
// way Raycast does — positional arguments, no Obsidian anywhere.
//
//   node Templates/Raycast/lib/vault.test.js
const fs = require("fs");
const os = require("os");
const path = require("path");

const vault = require("./vault.js");
const capture = require("../capture-to-project.js");
const open = require("../open-project.js");

let failures = 0;

function check(name, condition, detail) {
    if (condition) {
        console.log(`  ok   ${name}`);

        return;
    }

    failures += 1;
    console.log(`  FAIL ${name}${detail ? `\n       ${detail}` : ""}`);
}

// ─── Fixture vault ───────────────────────────────────────────────────────────

const root = fs.mkdtempSync(path.join(os.tmpdir(), "vault-"));

const write = (relative, content) => {
    fs.mkdirSync(path.join(root, path.dirname(relative)), { recursive: true });
    fs.writeFileSync(path.join(root, relative), content);
};

const read = (relative) => fs.readFileSync(path.join(root, relative), "utf8");

const project = (name, extra = "") => [
    "---",
    "categories:",
    '  - "[[Projects]]"',
    `project: "[[${name}]]"`,
    ...(extra ? [extra] : []),
    "---",
    "",
].join("\n");

write("Ethira.md", `${project("Ethira", "status: active")}## Log\n\n- 2026-08-01 — first\n\n## Desk\n\n\`\`\`dataviewjs\n\`\`\`\n`);
write("Ethirium.md", project("Ethirium", "status: active"));
write("Datahub.md", project("Datahub", "status: someday"));
write("PII.md", '---\ncategories:\n  - "[[Projects]]"\n---\n\nNo project property at all.\n');
// Belongs to Ethira, so it is not a project itself.
write("adr-tool-routing.md", project("Ethira"));
write("Raw/Some raw note.md", '---\ncategories:\n  - "[[Raw]]"\nproject: "[[Ethira]]"\n---\n');
write("Templates/Project Template.md", project("Project Template"));

const hubs = vault.findHubs(root);
const names = hubs.map((hub) => hub.name);

// ─── Reading the vault ───────────────────────────────────────────────────────

console.log("vault");

check("finds project notes", names.includes("Ethira"), names.join(", "));
check("finds one with no project property", names.includes("PII"), names.join(", "));
check("skips notes inside a project", !names.includes("adr-tool-routing"), names.join(", "));
check("skips templates", !names.includes("Project Template"), names.join(", "));
check("skips raw notes", !names.includes("Some raw note"), names.join(", "));
check(
    "orders active first",
    names.join(" | ") === "Ethira | Ethirium | PII | Datahub",
    names.join(" | ")
);

const parsed = vault.parseFrontmatter(read("Ethira.md"));

check("parses a block list", Array.isArray(parsed.categories), JSON.stringify(parsed));
check("unquotes a link", parsed.project === "[[Ethira]]", JSON.stringify(parsed.project));
check(
    "parses an inline list",
    JSON.stringify(vault.parseFrontmatter('---\ntags: [a, b]\n---\n').tags) === '["a","b"]'
);
check("returns null with no frontmatter", vault.parseFrontmatter("# Just a note") === null);

// Run from a git worktree, "up the tree" is the worktree's own copy of the vault, so
// captures would land somewhere Obsidian never opens. The override is the way out.
process.env.OBSIDIAN_VAULT_PATH = "/tmp/somewhere-else";
check("honours OBSIDIAN_VAULT_PATH", vault.vaultRoot() === "/tmp/somewhere-else");
delete process.env.OBSIDIAN_VAULT_PATH;
check("falls back to its own location", vault.vaultRoot().endsWith("obsidian-vault"), vault.vaultRoot());
check("formats an ISO date", /^\d{4}-\d{2}-\d{2}$/.test(vault.today(new Date(2026, 7, 4))));
check("uses local time, not UTC", vault.today(new Date(2026, 7, 4)) === "2026-08-04");

// ─── Matching ────────────────────────────────────────────────────────────────

console.log("matching");

check("matches a prefix", vault.matchProject(hubs, "eth").ambiguous?.length === 2);
check("exact beats prefix", vault.matchProject(hubs, "Ethira").hub?.name === "Ethira");
check("is case insensitive", vault.matchProject(hubs, "datahub").hub?.name === "Datahub");
check("matches a substring", vault.matchProject(hubs, "hub").hub?.name === "Datahub");
check("reports no match", vault.matchProject(hubs, "zzz").none === true);
check("treats blank as no match", vault.matchProject(hubs, "  ").none === true);

// ─── Capture ─────────────────────────────────────────────────────────────────

console.log("capture");

// vaultRoot() resolves from each script's own location, so main() takes the root as a
// parameter — the only difference between this and how Raycast calls it.
const appended = capture.main(["Ethira", "wired", "up", "raycast"], root);

check("reports the project", appended.message === "→ Ethira", appended.message);
check("exits clean", appended.code === 0);
check(
    "appends under ## Log, above the desk",
    read("Ethira.md").indexOf("wired up raycast") <
        read("Ethira.md").indexOf("## Desk"),
    read("Ethira.md")
);
check("keeps the earlier entry", read("Ethira.md").includes("- 2026-08-01 — first"));
check(
    "dates the entry",
    new RegExp(`- ${vault.today()} — wired up raycast`).test(read("Ethira.md")),
    read("Ethira.md")
);

capture.main(["Ethira", "second one"], root);

check(
    "a repeat capture does not duplicate the heading",
    read("Ethira.md").split("\n").filter((line) => line === "## Log").length === 1,
    read("Ethira.md")
);

const created = capture.main(["", "idea about caching layers"], root);

check("names a new note from the text", created.message === "→ idea about caching layers");
check(
    "gives it Inbox frontmatter",
    read("idea about caching layers.md").includes('  - "[[Inbox]]"'),
    read("idea about caching layers.md")
);
check(
    "keeps the text as the body",
    read("idea about caching layers.md").trimEnd().endsWith("idea about caching layers")
);

capture.main(["", "idea about caching layers"], root);

check(
    "never overwrites an existing note",
    fs.existsSync(path.join(root, "idea about caching layers 2.md"))
);

check(
    "strips characters Obsidian forbids in filenames",
    vault.safeFilename('a/b:c*d?e"f<g>h|i#j^k[l]m') === "abcdefghijklm",
    vault.safeFilename('a/b:c*d?e"f<g>h|i#j^k[l]m')
);

const before = read("Ethira.md");
const refused = capture.main(["eth", "ambiguous"], root);

check("refuses an ambiguous project", refused.code === 1, refused.message);
check("names the candidates", /Ethira, Ethirium/.test(refused.message), refused.message);
check("writes nothing when refusing", read("Ethira.md") === before);

const unknown = capture.main(["zzz", "nowhere"], root);

check("refuses an unknown project", unknown.code === 1, unknown.message);

const empty = capture.main(["Ethira", "   "], root);

check("refuses an empty capture", empty.code === 1, empty.message);

// ─── Open ────────────────────────────────────────────────────────────────────

console.log("open");

const uri = open.uriFor(root, hubs.find((hub) => hub.name === "Ethira"), "hugwi");

check("builds an obsidian:// url", uri === "obsidian://open?vault=hugwi&file=Ethira", uri);
check(
    "encodes a name with spaces",
    open.uriFor(root, { path: path.join(root, "My Project.md") }, "my vault")
        === "obsidian://open?vault=my%20vault&file=My%20Project",
    open.uriFor(root, { path: path.join(root, "My Project.md") }, "my vault")
);

fs.rmSync(root, { recursive: true, force: true });

process.exit(failures ? 1 : 0);
