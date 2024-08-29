# rye-mono-repo

## How to create a mono-repo with `rye`.

First step, create root project:

- Create empty folder and init a virtual project inside:
  - `rye init --virtual`
- Optional: config cross-platform lockfiles
  - Add `universal = true` in `tool.rye` section of `pyproject.toml`
- Create the virtual env and lockfiles:
  - `rye sync`

Then create sub-project, for this example we create `app1` under `apps` and `package` under `packages`.

- Create project for `app1`:
  - `rye init apps/app1`
- Create project for `package`:
  - `rye init package/package`

Then run `rye sync`, this should install both sub-projects in the virtual env in editable mode.

Install pytest: `rye add -d pytest`.

We change source code of these sub-projects so `app1` depends on package, and we add tests for each project.

Then we can run for all projects: `rye test -a`

## VSCode test runner

You should be able to configure python tests from VSCode, set the pytest arguments to `"."` so it discovers all tests of all projects.

## Commands

- Build a single project wheel
  - `rye build -p PACKAGE_NAME`
- Run tests for a single project
  - `rye test -p PACKAGE_NAME`

Note that `PACKAGE_NAME` is the name of the project defined in its `pyproject.toml` file, not the name of the sub-folder.
