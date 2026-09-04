<%*
// Attaches the note you are reading to a project — a raw note, a daily note, anything.
// Writes one property. The file does not move and nothing else is touched.
const picked = await tp.user.projects(tp, {
    placeholder: "Attach this note to which project?",
});

if (picked) {
    const target = tp.config.target_file;

    await app.fileManager.processFrontMatter(target, (frontmatter) => {
        frontmatter.project = `[[${picked.name}]]`;
    });

    new Notice(`${target.basename} → ${picked.name}`);
}
_%>
