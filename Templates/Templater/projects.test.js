// Harness: emulates enough of the Obsidian API to exercise the two user scripts.
//
//   node Templates/Templater/projects.test.js
const projects = require("./projects.js");
const captureToProject = require("./captureToProject.js");

let failures = 0;

function check(name, condition, detail) {
    if (condition) {
        console.log(`  ok   ${name}`);

        return;
    }

    failures += 1;
    console.log(`  FAIL ${name}${detail ? `\n       ${detail}` : ""}`);
}

// `spec` is a note's frontmatter plus `name`, `folder` and `body`.
function makeFile(spec) {
    const { name, folder = "", body = "", ...frontmatter } = spec;

    return {
        basename: name,
        path: folder ? `${folder}/${name}.md` : `${name}.md`,
        frontmatter,
        body,
    };
}

const VAULT = [
    { name: "Ethira", categories: ["[[Projects]]"], project: "[[Ethira]]", status: "active" },
    { name: "Datahub", categories: ["[[Projects]]"], project: "[[Datahub]]", status: "someday" },
    { name: "Old thing", categories: ["[[Projects]]"], project: "[[Old thing]]", status: "done" },
    // No `project:` at all — still a project note.
    { name: "PII", categories: ["[[Projects]]"] },
    // Points at another project: a note *inside* Ethira, not a project.
    { name: "adr-tool-routing", categories: ["[[Projects]]"], project: "[[Ethira]]" },
    { name: "Harness engineering", folder: "Raw", categories: ["[[Raw]]"] },
    { name: "Project Template", folder: "Templates", categories: ["[[Projects]]"] },
].map(makeFile);

global.app = {
    vault: { getMarkdownFiles: () => VAULT },
    metadataCache: {
        getFileCache: (file) => ({ frontmatter: file.frontmatter }),
    },
};

// ─── Picker ──────────────────────────────────────────────────────────────────

console.log("picker");

const hubs = projects.findHubs();
const names = hubs.map((entry) => entry.name);

check("keeps notes that name themselves", names.includes("Ethira"), names.join(", "));
check("keeps notes with no project property", names.includes("PII"), names.join(", "));
check(
    "drops notes belonging to another project",
    !names.includes("adr-tool-routing"),
    names.join(", ")
);
check("drops other categories", !names.includes("Harness engineering"), names.join(", "));
check("drops templates", !names.includes("Project Template"), names.join(", "));
check(
    "orders active first, done last",
    names.join(" | ") === "Ethira | PII | Datahub | Old thing",
    names.join(" | ")
);
check(
    "labels with the status icon",
    projects.labelFor(hubs[0]).startsWith("🎯"),
    projects.labelFor(hubs[0])
);

// The same rule the desk uses, spot-checked directly.
check("treats a missing status as active", projects.normalizeStatus(undefined) === "active");
check("maps someday -> pursue", projects.normalizeStatus("someday") === "pursue");
check(
    "reads a link property written as raw YAML",
    projects.namesOf(["[[Projects]]", "[[Areas|Areas]]"]).join(",") === "Projects,Areas",
    projects.namesOf(["[[Projects]]", "[[Areas|Areas]]"]).join(",")
);
check(
    "is not fooled by a same-named note in another folder",
    projects.isProjectHub({ categories: ["[[Projects]]"], project: "[[Ethira]]" }, "Ethira"),
);

// ─── Log insertion ───────────────────────────────────────────────────────────

console.log("capture");

const { logInsertion } = captureToProject;
const ENTRY = "- 2026-08-04 — ";

const withLog = [
    "---", "status: active", "---", "",
    "## Log", "",
    "- 2026-08-01 — first", "",
    "## Desk", "",
    "```dataviewjs", "```", "",
].join("\n");

const appended = logInsertion(withLog, ENTRY);

check(
    "appends after the last entry, not after the blank line",
    appended.content.split("\n")[7] === ENTRY,
    JSON.stringify(appended.content.split("\n").slice(4, 10))
);
check("reports the entry's line", appended.content.split("\n")[appended.line] === ENTRY);
check(
    "leaves the desk block below",
    appended.content.indexOf("## Desk") > appended.content.indexOf(ENTRY)
);

const noLog = [
    "---", "status: active", "---", "",
    "Some notes.", "",
    "## Desk", "",
    "```dataviewjs", "```",
].join("\n");

const created = logInsertion(noLog, ENTRY);

check(
    "creates the section above the desk",
    created.content.indexOf("## Log") < created.content.indexOf("## Desk"),
    created.content
);
check("puts the cursor on the new entry", created.content.split("\n")[created.line] === ENTRY);
check("keeps the body intact", created.content.includes("Some notes."));

const bare = logInsertion("Just a line.\n", ENTRY);

check(
    "falls back to the end when there is no desk",
    bare.content.split("\n")[bare.line] === ENTRY,
    JSON.stringify(bare.content)
);
check("still writes a heading", bare.content.includes("## Log"), bare.content);

// Two captures in a row must not stack up blank lines or lose the first entry.
const twice = logInsertion(appended.content, "- 2026-08-05 — ");

check(
    "stays stable across repeated captures",
    twice.content.split("\n").filter((line) => line === "## Log").length === 1 &&
        twice.content.includes("- 2026-08-01 — first") &&
        twice.content.includes(ENTRY),
    twice.content
);

process.exit(failures ? 1 : 0);
