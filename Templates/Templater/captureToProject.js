// Opens a project note with the cursor parked on a fresh, dated log bullet, so the
// capture happens with the project's own content in front of you.
//
//   await tp.user.captureToProject(file, tp.date.now("YYYY-MM-DD"));

// Where a new `## Log` section goes when the note has none. The desk block renders
// the whole project, so it stays last — the log is inserted above it.
const LOG_HEADING = /^##\s+log\s*$/i;
const DESK_HEADING = /^##\s+desk\s*$/i;

// Returns the note's new content and the 0-based line the entry landed on.
function logInsertion(content, entry) {
    const lines = content.split("\n");
    const heading = lines.findIndex((line) => LOG_HEADING.test(line));

    if (heading === -1) {
        const desk = lines.findIndex((line) => DESK_HEADING.test(line));
        const at = desk === -1 ? lines.length : desk;
        const block = ["## Log", "", entry, ""];

        return {
            content: [...lines.slice(0, at), ...block, ...lines.slice(at)].join("\n"),
            line: at + 2,
        };
    }

    // End of the log section: the next heading, or the end of the note.
    let end = heading + 1;

    while (end < lines.length && !/^##\s/.test(lines[end])) {
        end += 1;
    }

    // Append after the last entry, not after the blank lines that follow it.
    let at = end;

    while (at > heading + 1 && lines[at - 1].trim() === "") {
        at -= 1;
    }

    return {
        content: [...lines.slice(0, at), entry, ...lines.slice(at)].join("\n"),
        line: at,
    };
}

module.exports = async (file, today) => {
    const entry = `- ${today} — `;
    let line = 0;

    // Write before opening: a failed open leaves a saved note, not a half-edited one.
    await app.vault.process(file, (data) => {
        const result = logInsertion(data, entry);

        line = result.line;

        return result.content;
    });

    await app.workspace.getLeaf(false).openFile(file);

    const editor = app.workspace.activeEditor?.editor;

    if (editor) {
        editor.setCursor({ line, ch: entry.length });
        editor.scrollIntoView({ from: { line, ch: 0 }, to: { line, ch: 0 } }, true);
    }

    return line;
};

module.exports.logInsertion = logInsertion;
