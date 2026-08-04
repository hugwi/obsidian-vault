// Project picker — Obsidian's fuzzy-search modal over the vault's project notes.
//
//   const picked = await tp.user.projects(tp, {allowNone: true});
//   // -> {file, name} | {newNote: true} | null   (null = you pressed Esc)
//
// The rule for what counts as a *project* rather than a note inside one is shared
// with `Templates/Scripts/project-desk/view.js` (see renderBoard there). The two
// read different APIs — this one Obsidian's metadataCache, that one Dataview — so
// the rule is written twice on purpose. Change both, and see [[Project workflow]].

const STATUSES = [
    { id: "active", icon: "🎯" },
    { id: "pursue", icon: "🌱" },
    { id: "paused", icon: "⏸️" },
    { id: "done", icon: "✅" },
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

// metadataCache hands back raw YAML, so a link property is the string "[[Name]]" —
// unlike Dataview, which resolves it to a Link object.
function nameOf(value) {
    const raw = String(value ?? "").trim();
    const link = raw.match(/^\[\[([^\]]+)\]\]$/);

    return (link ? link[1] : raw).split("|")[0].split("/").pop().trim();
}

function namesOf(value) {
    if (value === null || value === undefined) {
        return [];
    }

    return (Array.isArray(value) ? value : [value])
        .map(nameOf)
        .filter(Boolean);
}

function normalizeStatus(value) {
    const raw = String(value ?? "").trim().toLowerCase();

    if (!raw) {
        return "active";
    }

    const id = STATUS_ALIASES[raw] || raw;

    return STATUSES.some((status) => status.id === id) ? id : "active";
}

// A project note names itself in `project:`, or names nothing at all. Anything that
// points at a *different* project is a note inside that project, not a project.
function isProjectHub(frontmatter, basename) {
    if (!frontmatter) {
        return false;
    }

    const categories = namesOf(frontmatter.categories);

    if (!categories.some((value) => value.toLowerCase() === "projects")) {
        return false;
    }

    const projects = namesOf(frontmatter.project);

    return projects.length === 0 ||
        projects.some((value) => value.toLowerCase() === basename.toLowerCase());
}

function isTemplate(file) {
    return file.path.startsWith("Templates/") || file.basename.includes("Template");
}

const statusRank = (status) => STATUSES.findIndex((entry) => entry.id === status);

// Active first — that is what you are capturing into nine times out of ten.
function findHubs() {
    return app.vault.getMarkdownFiles()
        .filter((file) => !isTemplate(file))
        .map((file) => ({
            file,
            name: file.basename,
            status: normalizeStatus(
                app.metadataCache.getFileCache(file)?.frontmatter?.status
            ),
            frontmatter: app.metadataCache.getFileCache(file)?.frontmatter,
        }))
        .filter((entry) => isProjectHub(entry.frontmatter, entry.name))
        .sort((a, b) => statusRank(a.status) - statusRank(b.status) ||
            a.name.localeCompare(b.name));
}

function labelFor(entry) {
    const icon = STATUSES.find((status) => status.id === entry.status).icon;

    return `${icon}  ${entry.name}`;
}

module.exports = async (tp, options = {}) => {
    const { allowNone = false, placeholder = "Project" } = options;
    const hubs = findHubs();

    const labels = hubs.map(labelFor);
    const values = hubs.map((entry) => ({ file: entry.file, name: entry.name }));

    if (allowNone) {
        // First entry, so it is one keystroke away when you have no project in mind.
        labels.unshift("➕  New note (no project)");
        values.unshift({ newNote: true });
    }

    if (!labels.length) {
        new Notice("No project notes found.");

        return null;
    }

    // throw_on_cancel: false — Esc returns null rather than blowing up the template.
    return await tp.system.suggester(labels, values, false, placeholder) ?? null;
};

module.exports.isProjectHub = isProjectHub;
module.exports.normalizeStatus = normalizeStatus;
module.exports.namesOf = namesOf;
module.exports.findHubs = findHubs;
module.exports.labelFor = labelFor;
