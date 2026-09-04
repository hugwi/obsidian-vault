// Harness: emulates enough of Dataview's `dv` API to exercise
// Templates/Scripts/project-desk/view.js the way Dataview does.
//
//   node Templates/Scripts/project-desk/test.js
const fs = require("fs");
const path = require("path");

const SRC = fs.readFileSync(path.join(__dirname, "view.js"), "utf8");

// Dataview wraps a DataArray around query results; view.js only ever calls
// `.array()` on one, so that is all this needs to provide.
const dataArray = (items) => ({ array: () => items });

function makeLink(name) {
    return { path: `${name}.md`, display: undefined };
}

// `spec` is the note as you would write its frontmatter, plus `name`, `tasks`
// and `inlinks` (vault-relative paths, without `.md`, of notes linking to it).
function makePage(spec) {
    const { name, folder = "", tasks = [], inlinks = [], ...props } = spec;
    const filePath = folder ? `${folder}/${name}.md` : `${name}.md`;

    return {
        ...props,
        file: {
            name,
            path: filePath,
            mtime: { toFormat: () => "2026-08-04" },
            tags: dataArray(props.tags ?? []),
            tasks: dataArray(tasks),
            inlinks: dataArray(inlinks.map(makeLink)),
        },
    };
}

function run(specs, input) {
    const pages = specs.map(makePage);
    const output = [];

    const dv = {
        pages: () => dataArray(pages),
        page: (p) => pages.find((page) => page.file.path === p),
        current: () => pages[0],
        fileLink: (p) => `[[${p.replace(/\.md$/, "").split("/").pop()}]]`,
        header: (level, text) => output.push({ kind: "header", level, text }),
        paragraph: (text) => output.push({ kind: "paragraph", text }),
        list: (items) => output.push({ kind: "list", items }),
        table: (headers, rows) => output.push({ kind: "table", headers, rows }),
        taskList: (tasks) => output.push({ kind: "tasks", tasks }),
    };

    // Dataview evaluates the view file as an async function body with `dv` and
    // `input` in scope — mirror that exactly, including `input` being undefined
    // when the caller passed nothing.
    const view = new Function("dv", "input", `return (async () => {${SRC}})();`);

    return view(dv, input).then(() => output);
}

const headers = (out, level) => out
    .filter((entry) => entry.kind === "header" && entry.level === level)
    .map((entry) => entry.text);

const tableRows = (out) => out
    .filter((entry) => entry.kind === "table")
    .flatMap((entry) => entry.rows);

let failures = 0;

function check(name, condition, detail) {
    if (condition) {
        console.log(`  ok   ${name}`);

        return;
    }

    failures += 1;
    console.log(`  FAIL ${name}${detail ? `\n       ${detail}` : ""}`);
}

// ─── Fixtures ────────────────────────────────────────────────────────────────

const VAULT = [
    {
        name: "Ethira",
        categories: [makeLink("Projects")],
        project: makeLink("Ethira"),
        status: "active",
        outcome: "Ship the agent platform",
        due: "2026-09-30",
        tasks: [
            { text: "Write the PRD", completed: false },
            { text: "Old thing", completed: true },
        ],
        inlinks: ["Daily/2026/08-August/2026-08-01"],
    },
    {
        name: "adr-tool-routing",
        categories: [makeLink("Projects")],
        project: makeLink("Ethira"),
        status: "draft",
        tasks: [{ text: "Decide on fallbacks", completed: false }],
    },
    {
        name: "ethira api limits",
        categories: [makeLink("Projects")],
        project: "ethira/api",
    },
    {
        name: "Harness engineering",
        folder: "Raw",
        categories: [makeLink("Raw")],
        project: makeLink("Ethira"),
        action: "implement",
        rating: 6,
        source: "readwise",
        tags: ["#harness"],
    },
    {
        name: "A brief history of ralph",
        folder: "Raw",
        categories: [makeLink("Raw")],
        project: makeLink("Ethira"),
    },
    {
        name: "Agentic patterns",
        categories: [makeLink("Resources")],
        project: makeLink("Ethira"),
        domain: "engineering",
    },
    {
        name: "Lukas",
        folder: "References",
        categories: [makeLink("People")],
        project: makeLink("Ethira"),
        role: "Founder",
    },
    {
        name: "2026-08-01",
        folder: "Daily/2026/08-August",
        categories: [makeLink("Daily")],
    },
    {
        name: "Project Template",
        folder: "Templates",
        categories: [makeLink("Projects")],
        project: makeLink("Project Template"),
    },
    {
        name: "PII Scanner",
        categories: [makeLink("Projects")],
        project: makeLink("PII"),
    },
    {
        name: "Datahub",
        categories: [makeLink("Projects")],
        status: "someday",
    },
    {
        name: "Unrelated area",
        categories: [makeLink("Areas")],
        domain: "career",
    },
];

// ─── Desk ────────────────────────────────────────────────────────────────────

run(VAULT, { project: "Ethira" }).then((out) => {
    console.log("desk");

    const sections = headers(out, 3).join(" | ");
    const cells = JSON.stringify(tableRows(out));

    check("counts the material", /\*\*7\*\* linked notes/.test(out[0].text), out[0].text);
    check("counts triaged raw notes", /\(1 triaged\)/.test(out[0].text), out[0].text);

    check("lists packets", sections.includes("📦 Intermediate packets (2)"), sections);
    check("scopes ethira/api to Ethira", cells.includes("[[ethira api limits]]"), cells);
    check("skips the template", !cells.includes("[[Project Template]]"), cells);
    check("skips the project note itself", !cells.includes("[[Ethira]]"), cells);
    check("skips other projects", !cells.includes("[[PII Scanner]]"), cells);

    check("groups raw material", sections.includes("🧱 Raw material (2)"), sections);
    check(
        "splits triaged from untriaged",
        headers(out, 4).join(" | ") === "🔨 To implement (1) | ⬜ Untriaged (1)",
        headers(out, 4).join(" | ")
    );

    check("lists resources", sections.includes("📚 Resources (1)"), sections);
    check("lists people", sections.includes("👤 People (1)"), sections);
    check(
        "picks up a daily note that only wikilinks the project",
        sections.includes("🗓️ Recent mentions (1)"),
        sections
    );

    const tasks = out.find((entry) => entry.kind === "tasks");

    check("collects open tasks from the project and its notes", tasks?.tasks.length === 2);
    check("drops completed tasks", !JSON.stringify(tasks?.tasks).includes("Old thing"));

    return run(VAULT, { project: "Datahub" });
}).then((out) => {
    console.log("desk — empty project");

    check(
        "explains how to attach material",
        out.some((entry) => /project: "\[\[Datahub\]\]"/.test(entry.text ?? "")),
        JSON.stringify(out)
    );

    return run(VAULT, { mode: "board" });
}).then((out) => {
    console.log("board");

    const sections = headers(out, 3).join(" | ");
    const cells = JSON.stringify(tableRows(out));

    check("groups by status", sections.includes("🎯 Active (1)"), sections);
    check("maps someday -> pursue", sections.includes("🌱 To pursue (1)"), sections);
    check("lists only project hubs", !cells.includes("[[adr-tool-routing]]"), cells);
    check(
        "counts a hub's material",
        JSON.parse(cells).some((row) => row[0] === "[[Ethira]]" && row[2] === 2),
        cells
    );
    check(
        "surfaces the next action",
        cells.includes("Write the PRD"),
        cells
    );

    const orphans = out.find((entry) => entry.kind === "list");

    check("flags projects with no note", orphans?.items.includes("PII"), JSON.stringify(orphans));
    check("does not flag projects that have one", !orphans?.items.includes("Ethira"));

    process.exit(failures ? 1 : 0);
}).catch((error) => {
    console.error(error);
    process.exit(1);
});
