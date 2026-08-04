// Project desk — one project's workbench, or a board of every project.
//
//   ```dataviewjs
//   await dv.view("Templates/Scripts/project-desk");                    // this note's desk
//   await dv.view("Templates/Scripts/project-desk", {project: "PII"});  // another project
//   await dv.view("Templates/Scripts/project-desk", {mode: "board"});   // every project
//   ```
//
// A note joins a project by carrying `project: "[[Name]]"` — that works on *any*
// note regardless of its `categories`, which is the whole point: a clipping stays a
// clipping in `Clippings/` and still shows up here as raw material. Wikilinking the
// project note from anywhere also counts, so a passing mention in a daily note is
// picked up without bookkeeping.

// Dataview always passes `input`, but passes `undefined` when the note called
// `dv.view()` with no second argument.
const options = input || {};

// ─── Project status vocabulary ───────────────────────────────────────────────
// Forte's PARA distinguishes what you are working on now from what you have merely
// decided you want to pursue; a project with no status is treated as active so the
// desk works before you have filled anything in.
const STATUSES = [
    { id: "active", label: "🎯 Active" },
    { id: "pursue", label: "🌱 To pursue" },
    { id: "paused", label: "⏸️ Paused" },
    { id: "done", label: "✅ Done" },
];

const STATUS_ALIASES = {
    "in-progress": "active",
    "in progress": "active",
    wip: "active",
    someday: "pursue",
    maybe: "pursue",
    "someday-maybe": "pursue",
    idea: "pursue",
    backlog: "pursue",
    "on-hold": "paused",
    "on hold": "paused",
    hold: "paused",
    blocked: "paused",
    complete: "done",
    completed: "done",
    finished: "done",
    shipped: "done",
    archived: "done",
};

// Clipping triage vocabulary, in the order the vault reads it: what you will build
// first, then what still needs a pass, then what you keep for reference.
const ACTIONS = [
    { id: "implement", label: "🔨 To implement" },
    { id: "review", label: "📋 To review" },
    { id: "insight", label: "💡 Insights" },
    { id: null, label: "⬜ Untriaged" },
];

function normalizeStatus(value) {
    const raw = String(value ?? "").trim().toLowerCase();

    if (!raw) {
        return "active";
    }

    const id = STATUS_ALIASES[raw] || raw;

    return STATUSES.some((status) => status.id === id) ? id : "active";
}

// A property may hold a link, a bare string, or a list of either. Reduce all of it
// to plain names so callers never branch on shape.
function namesOf(value) {
    if (value === null || value === undefined) {
        return [];
    }

    if (Array.isArray(value)) {
        return value.flatMap(namesOf);
    }

    if (typeof value === "object") {
        // Dataview Link: prefer the display text, fall back to the file name.
        const path = String(value.path ?? "");
        const name = path.split("/").pop().replace(/\.md$/, "");

        return [String(value.display || name).trim()].filter(Boolean);
    }

    return [String(value).trim()].filter(Boolean);
}

const same = (a, b) => a.toLowerCase() === b.toLowerCase();

// `project: ethira/api` scopes a note to a slice of a project. The slice belongs to
// its parent, so the parent's desk shows it.
function withinProject(value, project) {
    return same(value, project) ||
        value.toLowerCase().startsWith(`${project.toLowerCase()}/`);
}

function projectsOf(page) {
    return namesOf(page.project);
}

function categoriesOf(page) {
    return namesOf(page.categories);
}

function hasCategory(page, category) {
    return categoriesOf(page).some((value) => same(value, category));
}

function isTemplate(page) {
    return page.file.path.startsWith("Templates/") ||
        page.file.name.includes("Template");
}

function inlinkPages(page) {
    const links = page.file.inlinks?.array?.() ?? [];

    return links
        .map((link) => dv.page(link.path))
        .filter(Boolean);
}

// Material for a project: everything tagged onto it, plus everything that links to
// its note. Deduplicated by path — a note that does both appears once.
function materialFor(project, projectPage) {
    const byPath = new Map();
    const add = (page) => {
        if (!page || isTemplate(page)) {
            return;
        }

        if (projectPage && page.file.path === projectPage.file.path) {
            return;
        }

        byPath.set(page.file.path, page);
    };

    for (const page of dv.pages().array()) {
        if (projectsOf(page).some((value) => withinProject(value, project))) {
            add(page);
        }
    }

    if (projectPage) {
        inlinkPages(projectPage).forEach(add);
    }

    return [...byPath.values()];
}

function openTasks(pages) {
    return pages.flatMap((page) => (page.file.tasks?.array?.() ?? [])
        .filter((task) => !task.completed));
}

function sortByName(pages) {
    return [...pages].sort((a, b) => a.file.name.localeCompare(b.file.name));
}

function dateOf(value) {
    if (!value) {
        return "";
    }

    // Dataview hands back Luxon DateTimes for date properties, strings otherwise.
    return typeof value.toFormat === "function"
        ? value.toFormat("yyyy-MM-dd")
        : String(value);
}

function tagsOf(page) {
    return (page.file.tags?.array?.() ?? []).join(" ");
}

// ─── Board: every project, grouped by status ─────────────────────────────────

function renderBoard() {
    const projectPages = dv.pages()
        .array()
        .filter((page) => hasCategory(page, "Projects") && !isTemplate(page));

    // A project note is one that names itself, or that nothing else claims as a
    // parent — everything else with `categories: [[Projects]]` is a note *inside* a
    // project and belongs in that project's desk, not on the board.
    const hubs = projectPages.filter((page) => {
        const projects = projectsOf(page);

        return projects.length === 0 ||
            projects.some((value) => same(value, page.file.name));
    });

    const hubNames = hubs.map((page) => page.file.name);

    // Names referenced by `project:` that no note has ever been created for. These
    // are the easiest thing in the vault to lose track of, so they get their own row.
    const orphans = [...new Set(dv.pages()
        .array()
        .filter((page) => !isTemplate(page))
        .flatMap(projectsOf)
        .filter((value) => !hubNames.some((name) => withinProject(value, name)))
        .map((value) => value.split("/")[0]))];

    const rows = (pages) => pages.map((page) => {
        const material = materialFor(page.file.name, page);
        const own = material.filter((item) => hasCategory(item, "Projects"));
        const raw = material.filter((item) => hasCategory(item, "Clippings"));
        const next = openTasks([page, ...own])[0];

        return [
            dv.fileLink(page.file.path),
            page.outcome ?? "",
            raw.length,
            own.length,
            next ? next.text : "",
            dateOf(page.due),
        ];
    });

    const headers = ["Project", "Outcome", "Material", "Notes", "Next action", "Due"];

    for (const status of STATUSES) {
        const group = sortByName(
            hubs.filter((page) => normalizeStatus(page.status) === status.id)
        );

        if (!group.length) {
            continue;
        }

        dv.header(3, `${status.label} (${group.length})`);
        dv.table(headers, rows(group));
    }

    if (orphans.length) {
        dv.header(3, `⚠️ Referenced, but no project note (${orphans.length})`);
        dv.paragraph(
            "Notes point at these with `project:`, so the material is stranded — " +
            "create the note from `Templates/Project Template.md` to give it a desk."
        );
        dv.list(orphans.sort((a, b) => a.localeCompare(b)));
    }

    if (!hubs.length && !orphans.length) {
        dv.paragraph("No projects yet.");
    }
}

// ─── Desk: one project ───────────────────────────────────────────────────────

function renderSection(title, pages, columns) {
    if (!pages.length) {
        return;
    }

    dv.header(3, `${title} (${pages.length})`);
    dv.table(
        columns.map((column) => column.header),
        sortByName(pages).map((page) => columns.map((column) => column.cell(page)))
    );
}

const NOTE_COLUMN = {
    header: "Note",
    cell: (page) => dv.fileLink(page.file.path),
};

function renderDesk(project) {
    const projectPage = dv.pages()
        .array()
        .find((page) => same(page.file.name, project) && !isTemplate(page));

    const material = materialFor(project, projectPage);
    const own = material.filter((page) => hasCategory(page, "Projects"));
    const clippings = material.filter((page) => hasCategory(page, "Clippings"));
    const resources = material.filter((page) => hasCategory(page, "Resources"));
    const areas = material.filter((page) => hasCategory(page, "Areas"));
    const people = material.filter((page) => hasCategory(page, "People"));
    const daily = material.filter((page) => hasCategory(page, "Daily"));

    const claimed = new Set(
        [...own, ...clippings, ...resources, ...areas, ...people, ...daily]
            .map((page) => page.file.path)
    );

    const other = material.filter((page) => !claimed.has(page.file.path));
    const tasks = openTasks(projectPage ? [projectPage, ...own] : own);

    // Distilled = raw material you have actually made a call on. The ratio is the
    // honest measure of whether a project is being worked or just collected into.
    const triaged = clippings.filter((page) => page.action || page.rating).length;

    dv.paragraph([
        `**${material.length}** linked notes`,
        `**${clippings.length}** raw material (${triaged} triaged)`,
        `**${own.length}** own notes`,
        `**${tasks.length}** open tasks`,
    ].join(" · "));

    if (!material.length) {
        dv.paragraph(
            `Nothing is attached yet. Add \`project: "[[${project}]]"\` to a ` +
            "clipping or note — or just wikilink this note from it."
        );
    }

    renderSection("📦 Intermediate packets", own, [
        NOTE_COLUMN,
        { header: "Status", cell: (page) => page.status ?? "" },
        { header: "Updated", cell: (page) => dateOf(page.file.mtime) },
    ]);

    if (clippings.length) {
        dv.header(3, `🧱 Raw material (${clippings.length})`);

        for (const action of ACTIONS) {
            const group = clippings.filter(
                (page) => (page.action ?? null) === action.id
            );

            if (!group.length) {
                continue;
            }

            dv.header(4, `${action.label} (${group.length})`);
            dv.table(
                ["Note", "Rating", "Tags", "Source"],
                sortByName(group).map((page) => [
                    dv.fileLink(page.file.path),
                    page.rating ?? "",
                    tagsOf(page),
                    page.source ?? "",
                ])
            );
        }
    }

    const domainColumn = {
        header: "Domain",
        cell: (page) => namesOf(page.domain).join(", "),
    };

    renderSection("📚 Resources", resources, [NOTE_COLUMN, domainColumn]);
    renderSection("🗂️ Areas", areas, [NOTE_COLUMN, domainColumn]);
    renderSection("👤 People", people, [
        NOTE_COLUMN,
        { header: "Role", cell: (page) => page.role ?? page.company ?? "" },
    ]);

    if (daily.length) {
        // Newest first, and only a handful: the log is context, not a work surface.
        const recent = [...daily]
            .sort((a, b) => b.file.name.localeCompare(a.file.name))
            .slice(0, 10);

        dv.header(3, `🗓️ Recent mentions (${daily.length})`);
        dv.list(recent.map((page) => dv.fileLink(page.file.path)));
    }

    renderSection("📎 Other linked notes", other, [
        NOTE_COLUMN,
        { header: "Category", cell: (page) => categoriesOf(page).join(", ") },
    ]);

    if (tasks.length) {
        dv.header(3, `✅ Open tasks (${tasks.length})`);
        dv.taskList(tasks, false);
    }
}

// ─── Entry ───────────────────────────────────────────────────────────────────

if (options.mode === "board") {
    renderBoard();
} else {
    renderDesk(options.project || dv.current().file.name);
}
