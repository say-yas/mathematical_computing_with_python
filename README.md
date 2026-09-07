# Mathematical Computing with Python

Course website and lecture notebooks, built with [Jupyter Book](https://jupyterbook.org)
and deployed automatically to GitHub Pages.

**Live site (after setup):** `https://say-yas.github.io/mathematical_computing_with_python/`

## Repository structure

```
mathematical_computing_with_python/
├── book/
│   ├── _config.yml              # Jupyter Book configuration
│   ├── _toc.yml                 # Table of contents / chapter order
│   ├── intro.md                 # Landing page
│   ├── requirements.txt         # Python deps needed to build the book
│   └── notebooks/
│       └── week01_python_basics.ipynb   # Class 1: Python basics + NumPy
├── .github/workflows/deploy.yml # Auto-builds & publishes the site on push
└── README.md
```

## One-time setup (do this after creating the repo on GitHub)

1. Create a new GitHub repository named `mathematical_computing_with_python`
   and push this folder's contents to it.
3. In your repo on GitHub, go to **Settings → Pages** and set:
   - **Source:** Deploy from a branch
   - **Branch:** `gh-pages` / `/(root)`
   (This branch is created automatically the first time the Action runs —
   it won't exist until after your first push to `main`.)
4. Push to `main`. Go to the **Actions** tab and watch the `deploy-book`
   workflow run. Once it's green, your site is live at the URL above.

## Adding a new class

1. Add a new notebook under `book/notebooks/`, e.g. `Aug11_matplotlib_deep_dive.ipynb`.
2. Add it to `book/_toc.yml`:
   ```yaml
   chapters:
     - file: notebooks/Aug9_python_basics
   ```
3. Commit and push to `main`. The site rebuilds and redeploys automatically.

## Working locally

```bash
# From the repo root
pip install -r book/requirements.txt
jupyter-book build book/
```

Open `book/_build/html/index.html` in a browser to preview before pushing.

To edit a notebook interactively:

```bash
pip install jupyterlab
jupyter lab book/notebooks/week01_python_basics.ipynb
```
