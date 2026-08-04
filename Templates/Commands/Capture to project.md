<%*
// Quick capture. Pick a project and land in it ready to type; pick nothing and get a
// plain new note instead. Runs from the command palette — type "project".
const picked = await tp.user.projects(tp, {
    allowNone: true,
    placeholder: "Capture to which project?",
});

if (picked && picked.newNote) {
    const title = await tp.system.prompt("Note title", "", false);

    if (title) {
        const today = tp.date.now("YYYY-MM-DD");
        const body = `---\ncreated: ${today}\ncategories:\n  - "[[Inbox]]"\ntags:\n---\n\n`;

        await tp.file.create_new(body, title, true, app.vault.getRoot());
    }
} else if (picked) {
    await tp.user.captureToProject(picked.file, tp.date.now("YYYY-MM-DD"));
}
_%>
