# CLAUDE.md

Course repository for training high-school students toward IOAI 2027 (Singapore, 4–10 July 2027). Two levels, one weekly 2 h class each, all work done in Google Colab notebooks. This **public** repo holds the schedule, class notebooks and homework statements. Students hand in homework through **GitHub Classroom** in the org `Alto-Rendimiento-IA`, where each student gets a private repo per assignment (workflow: README.md, section "Antes de empezar: GitHub").

## Sources of truth

- `README.md`: Intermediate-level schedule. Week numbers, session types, topics, deliverable codes, grading, and the IOAI syllabus coverage table (§3). Read the relevant row before writing anything.
- `Guia_del_estudiante.md`: student-facing rules (AI-use policy, rubric, deliverable rules). Notebooks must follow them.
- Nivel Inicial has no schedule yet. Before writing any of its notebooks, ask the user for the topic list and the entry level. What is known: it runs Oct–Dec 2026, it uses sklearn but no PyTorch (README §4), and its graduates join the intermediate level in February.
- `Guia_estudiante.docx` is the Word version of the guide, kept in sync with the `.md` by editing its XML (docx skill). If a date changes, update README.md, Guia_del_estudiante.md and the .docx together. Notebooks give the week number only, never a calendar date, so they stay correct when the calendar changes.

## Environment

- `requirements.txt` mirrors the **Colab runtime** (Python 3.13), so local runs behave like the students' Colab runs. To refresh it, take the versions from `https://raw.githubusercontent.com/googlecolab/backend-info/main/pip-freeze.txt`. Keep its section headers (`# --- ...`), because `verificar_entorno.ipynb` parses them.
- The last section lists packages Colab lacks. A notebook that uses one installs it in its first cell with the pinned version (`%pip install -q ultralytics==<pin>`). Colab's preinstalled packages are never reinstalled from a notebook: that is slow and can break its CUDA build.
- Local env: `.venv/` (gitignored, built with `uv venv --python 3.13 && uv pip install -r requirements.txt`, uv lives at `~/.local/bin/uv`). This machine has an RTX 5090, so GPU notebooks can be verified here. Don't add `.python-version`: the user's pyenv reads it and breaks `python3` in this folder.

## Layout and naming

```
Nivel_<Inicial|Intermedio>/
  clases/semNN_<tema>.ipynb        # NN = README week number, two digits: sem06_pytorch.ipynb
  tareas/<codigo>_<tema>.ipynb     # codes from README: B1, P01…P13, S1, Sprint0…Sprint3
  soluciones/                      # reference solutions, gitignored, local only
  README.md                        # index: add a row for every notebook you create
```

File names are snake_case ASCII: no accents, no `ñ`, no spaces, because they end up in Colab and GitHub URLs.

## Writing a notebook

1. **Locate the row.** Find the week/code in README.md: its topic is the scope, its type ([A]/[B]/[C]/[D]) sets the shape (below), and the §3 table lists which syllabus items it must cover.
2. **Check the prerequisites.** List what earlier weeks taught and use only those tools (for example, no PyTorch before week 6, no `nn.Conv2d` before week 11). Each homework must also be **self-contained**: a student who skipped every earlier homework can still complete it (README §6, expected 30–50% dropout).
3. **Build it with `nbformat`** from a Python script in the scratchpad. Hand-edited notebook JSON breaks.
4. **Verify.** Run `.venv/bin/jupyter nbconvert --to notebook --execute` on class notebooks and on every homework's reference solution. The homework statement itself fails its checks by design. Done means it runs top to bottom with no errors on a fresh kernel. If it needs a GPU or Colab-only features and you can't run it locally, tell the user which cells you could not run.
5. **Commit with outputs cleared**, then add the row to the level README.

## Every notebook

- **Spanish** for all prose, comments, and plot labels. Code identifiers are in English, following PyTorch/sklearn conventions. The first time a technical term appears, give it in English in italics with a Spanish gloss (*broadcasting*, *accuracy*), as README does. Datasets, APIs, and competition problems stay in English: that friction is part of the training.
- **Header cell** with: title, level, week number, session type, 3–4 learning objectives, prerequisites, estimated time, compute needs (CPU / GPU T4), and (class notebooks only, see Homework) an "Abrir en Colab" badge pointing to `https://colab.research.google.com/github/melvinpqbsc/Alto_Rendiento_IA/blob/main/<path>`.
- **Fresh-runtime reproducible**: the first code cell holds the `%pip install -q` lines (see Environment), all imports, and a fixed seed. Data comes from torchvision / sklearn / Hugging Face datasets or a stable public URL, with no Drive mounting and no local paths. Size datasets and training so they fit in free Colab: minutes, not hours, unless the README row says otherwise (for example, the 15 min GPU budgets).
- **Baseline first**: every modelling result is compared against a simple baseline (majority class, linear model, TF-IDF + logistic regression, …).

## Classes (`clases/`) by session type

- **[A] lecture**: teacher-driven. Short explanation cells alternate with live demos. Build ideas from scratch in NumPy before showing the library call. End sections with short "Tu turno" exercises.
- **[B] lab**: mostly exercises in increasing difficulty, each with a check cell so students can see their own progress while the teacher circulates.
- **[C] seminar**: the students present, so write a scaffold for the presenter: topic outline, the key figure/demo to build, 3 references, and 3 discussion questions for the audience.
- **[D] sprint**: problem statement, data loading, a working baseline, the submission format, and a local validation split. Delivered like homework, through a Classroom assignment. The hidden test set lives only in `test_oculto/` (gitignored). Any public commit of it leaks the answers.

## Homework (`tareas/`)

- The notebook is a **statement**, never a solution. It holds context and a goal, numbered tasks, `# TODO` cells, and `assert`-based check cells wherever correctness is checkable (shapes, values against a library reference such as micrograd vs `torch.autograd`, attention vs `nn.MultiheadAttention`).
- Reference solutions go to `<nivel>/soluciones/` (gitignored). The repo is public, so a solution that gets committed has already leaked.
- **Classroom delivery.** The statement in `tareas/` is the source of truth. Each homework, sprint and the project also needs a Classroom starter repo: a private template repo `Alto-Rendimiento-IA/plantilla-<codigo>-<tema>` holding only the statement notebook and any small data files. `gh` isn't installed, so prepare the template's contents and tell the user what to create in the web UI. The user makes the Classroom assignment itself (individual, or group of 2 for the project).
- The homework header has no Colab badge: the badge would open the public statement, and saving from it goes to the wrong place. Instead the header tells students to accept the invitation and open the notebook from their `Alto-Rendimiento-IA/<trabajo>-<usuario>` repo.
- Peer review happens outside the private repos: students share a Drive copy of the notebook with their reviewer. Write the rubric cell so a reviewer can fill it in as a comment.
- It ends with three fixed cells: **Conclusión** (the student's plain-language paragraph: what the numbers mean, what they'd try next; no paragraph, no grade), **Uso de IA** (one line: what they used AI for, if anything), and the **rubric**: runs / correct / justified / well communicated, 0–2 each, with space for the student's self-score.
