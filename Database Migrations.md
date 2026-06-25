---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
# Database Migrations

Schema changes are code. Version them, review them, ship them on rails. Never let runtime auto-sync drive prod.

## Core rule

`synchronize: true` (TypeORM) / `db.create_all()` (SQLAlchemy) / `prisma db push` is for **prototyping only**. Prod uses an ordered, versioned migration history applied by tooling — never by ORM introspection.

Why: auto-sync handles additive changes fine, but silently corrupts on rename, type change, non-null transitions, and drops. By the time you notice, history is gone.

## Tool parity

| Concept | Alembic (Python) | TypeORM (TS) | Prisma | Knex / Drizzle |
|---|---|---|---|---|
| Config | `alembic.ini` + `env.py` | `DataSource` config file | `schema.prisma` | `knexfile` / `drizzle.config` |
| New revision | `alembic revision --autogenerate -m "x"` | `typeorm migration:generate` | `prisma migrate dev` | `knex migrate:make` |
| Apply pending | `alembic upgrade head` | `typeorm migration:run` | `prisma migrate deploy` | `knex migrate:latest` |
| Rollback last | `alembic downgrade -1` | `typeorm migration:revert` | manual (no auto down) | `knex migrate:rollback` |
| History table | `alembic_version` | `typeorm_migrations` | `_prisma_migrations` | `knex_migrations` |
| Status | `alembic current` / `history` | `migration:show` | `migrate status` | `migrate:status` |

All four follow the same model: ordered files, applied once, recorded in a tracking table.

## The workflow

```
edit entity / schema
        │
        ▼
generate migration (auto-diff)
        │
        ▼
review generated SQL — hand-edit if wrong
        │
        ▼
apply locally → run tests → commit migration + entity together
        │
        ▼
CI applies migration before deploy (or app applies on boot)
```

Migration file and entity change live in the **same commit**. Splitting them creates a window where main is broken.

## Boot-time vs CI-time apply

Two valid models. Pick per environment.

- **Boot-time (`migrationsRun: true`)**: app applies pending migrations on startup. First pod wins via `pg_advisory_lock`. Zero ops cost. Good for preview envs, dev, ephemeral stacks.
- **CI-time (pre-deploy step)**: pipeline runs `migrate` before swapping traffic. Migration failure blocks deploy. Good for staging, prod.

Never both at once. If CI applies, set `migrationsRun: false`.

## Expand / contract for breaking changes

Single-deploy breaking change = guaranteed downtime under rolling deploys. Old pods still write the old shape while new pods read the new shape.

Two PRs, two deploys:

**Rename `foo → bar`:**
- PR 1: add `bar` nullable. Backfill `foo → bar`. Dual-write. Reads prefer `bar` fallback `foo`.
- PR 2: drop `foo`. Code writes only `bar`.

**Nullable → NOT NULL:**
- PR 1: add column nullable. Write to it. Backfill old rows.
- PR 2: assert `WHERE col IS NULL` returns zero. Apply `SET NOT NULL`.

**Type change `text → int`:**
- PR 1: add `col_v2` with new type. Dual-write. Backfill `v1 → v2`.
- PR 2: switch reads/writes to `v2`. Drop `v1`. Optionally rename.

Rule: any single deploy where the old version of the app can't read the new schema = broken rollback.

## Backfill discipline

Backfills are **not** migrations. Put them in a one-off processor / admin script:

- Idempotent — re-running is safe
- Resumable — keyed by `lastId`, not offset
- Bounded — small batches (500-1000), no full-table `find()`
- Observable — log batch size and progress

Never run `UPDATE ... SET col = '...'` inside a migration `up()` against a large table. It locks rows, blocks deploys, and can't resume on failure.

## Multi-schema / multi-env propagation

Parallel envs sharing one DB (color-coded local stacks, multi-tenant schemas) need migrations applied per schema. The migration tool only knows one `search_path` at a time. Loop:

```sh
for schema in public blue green red yellow purple; do
  DB_SCHEMA="$schema" run migration tool
done
```

Wire as Makefile target. Run after every pull on `main`. Remote envs (staging, prod) apply via CI or boot-time, one per env.

## Rollback story

Every migration owes a tested `down()`. PR body states what happens to data on rollback:

- Data preserved (the common case)
- Data lost (only for additive drops, document explicitly)
- Manual restore required (rare, flag it loudly)

Two-deploy patterns make rollback safe because the previous code version still reads the old shape.

## Pre-PR checklist

- [ ] Schema change classified (additive / rename / type / drop / NOT NULL / constraint)
- [ ] Migration file + entity change in same commit
- [ ] `down()` implemented and tested locally
- [ ] Backfill (if needed) is a separate idempotent job, not inside `up()`
- [ ] Two-deploy plan documented for renames / drops / type changes / NOT NULL
- [ ] Indexes added for new `WHERE` / `JOIN` / `ORDER BY` columns
- [ ] Demo / seed data updated for new fields
- [ ] Rollback impact stated in PR body
- [ ] Migration applied to every parallel schema before merge

## Anti-patterns

- Auto-sync in prod ("but it works in dev")
- One PR that renames + drops + adds in one migration
- Backfill inside `up()` on a multi-million-row table
- No `down()` ("we'll never roll back")
- Migration committed without the entity change
- Migration tested only against an empty local DB

## See also

- *Refactoring Databases* — Ambler & Sadalage, 2006 (expand/contract origin)
- [[Beck's Two-Hat Rule]] — keep structural migration commits separate from behavior-change commits
- Postgres docs: `ALTER TABLE` lock levels — what each DDL actually locks
