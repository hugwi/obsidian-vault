# Claude Instructions — Second Brain Vault

## Vault Structure (PARA method)
```
hugwi/
├── _MOC/             → Maps of Content — navigation hub (sorts first)
├── 00 Inbox/         → Unprocessed captures (Web Clippings, Quick Notes)
├── 01 Projects/      → Active work with deadlines (Ethira, Datahub, PII Scanner)
├── 02 Areas/
│   ├── Work/
│   │   ├── Engineering/   → Tech patterns, architecture, tooling
│   │   ├── Career/        → Career dev, mentoring, feedback, reflections
│   │   └── Clients/       → MaxM work, company notes, meeting notes
│   └── Personal/
│       ├── Finance/       → Housing, taxes, financial notes
│       ├── Health/        → Health & fitness
│       └── Interests/     → Hobbies, personal pursuits
├── 03 Resources/
│   ├── Technical/     → Evergreen engineering reference notes
│   ├── Compliance/    → GDPR, PCI, data governance (work-related)
│   └── Images/        → Pasted screenshots
├── 04 People/         → Contact/colleague notes (CRM-like)
├── 05 Templates/      → Note templates (daily, web-clip, etc.)
├── 06 Timestamps/     → Daily notes (YYYY/MM-MMMM/YYYY-MM-DD-dddd)
└── 07 Archives/       → Inactive/completed items
```

## How to Help

### Processing Inbox
When asked to "process inbox":
1. Review each file in `00 Inbox/Web Clippings/` and `00 Inbox/Quick Notes/`
2. Suggest destination folder based on content type
3. Suggest wikilinks to existing related notes
4. Update `status:` frontmatter from `inbox` → `processed`

### Finding Related Notes
- Search across `01 Projects/`, `03 Resources/Technical/`, and `02 Areas/Work/` for linked concepts
- Suggest `[[wikilinks]]` using exact note titles
- Point to relevant MOC files in `_MOC/`

### Adding New Notes
Recommend this frontmatter:
```yaml
---
title: "[Descriptive title]"
date_created: YYYY-MM-DD
type: [concept | project | area | capture | moc | daily]
status: [inbox | active | review | complete | archived]
tags: [lowercase-hyphenated]
---
```

## Note Placement Rules
| Content type | Destination |
|---|---|
| Architecture/technical patterns | `03 Resources/Technical/` |
| GDPR, PCI, data governance | `03 Resources/Compliance/` |
| Active project work | `01 Projects/[name]/` |
| Architecture Decision Records | `01 Projects/[name]/adr-*.md` |
| Meeting notes (client/work) | `02 Areas/Work/Clients/` |
| Career & growth notes | `02 Areas/Work/Career/` |
| People/contacts | `04 People/` |
| Web clips (unprocessed) | `00 Inbox/Web Clippings/` |
| Quick ideas | `00 Inbox/Quick Notes/` |
| Personal life | `02 Areas/Personal/` |

## Key Notes to Know
- **Ethira architecture**: `01 Projects/Ethira/agentic-systems-architecture.md`
- **Ethira tools catalog**: `01 Projects/Ethira/agentic-systems-tools-and-prompts.md`
- **Vault navigation**: `_MOC/Home.md`
- **Daily notes template**: `05 Templates/daily_note_template.md`
- **Web clip template**: `05 Templates/web-clip-template.md`

## Preferences
- ISO dates: `YYYY-MM-DD`
- Tags: `lowercase-hyphenated`
- Internal links: `[[wikilinks]]` preferred over URLs
- File names: `descriptive-kebab-case.md` for new files
- Commit message format: `type: description` (feat/fix/docs/chore)
