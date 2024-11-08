# ruff: noqa

import marimo

__generated_with = "0.9.14"
app = marimo.App(
    layout_file="layouts/sample.slides.json",
    css_file="themes/wigwam/wigwam.css",
)


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        # Sample Markdown Block

        ---

        # Header 1
        ## Header 2
        ### Header 3
        #### Header 4
        ##### Header 5
        ###### Header 6


        ---

        **Bold** | *Italic:* | ~~Strikethrough~~ | `Inline Code`

        ---

        > "The only way to do great work is to love what you do."
        > — *Steve Jobs*
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ---

        1. Item One
        2. Item Two
        3. Item Three

        ---

        - Bullet One
        - Bullet Two
        - Bullet Three

        ---

        1. Main Item
            - Sub Item
                - Sub-sub Item

        ---

        [Marimo](https://marimo.io/)
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        """
        | Syntax      | Description | Example           |
        |-------------|-------------|-------------------|
        | **Header**  | Row Title   | Content Here      |
        | **Row 1**   | First Cell  | `Some code`       |
        | **Row 2**   | Second Cell | *Italicized text* |

        ---

        ```python
        def greet(name: str) -> str:
            \"""Return a greeting message.\"""
            return f"Hello, {name}!"
        ```

        ---

        Here is a sentence with a footnote reference[^1].

        [^1]: This is the footnote content.

        ---


        - Inline: $E = mc^2$
        - Block:

        $$
        f(x) = \\int_{-\\infty}^{\\infty} e^{-x^2} \\, dx
        $$
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(r"""# Incomplete Reference of Different Args' Use""")


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## `bg-muted` & `text-muted-foreground`

        - hover on `fullscreen` and `cell action` buttons at the right of each cell
        - The banner of collapsed cells
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## `bg-popover` & `text-popover-foreground`

        - `Snippets` side panel
        - `Menu` items: `Share`, `Download`, `Helper panel`, `Present as`
        - The popover snippets when you enter `:` in markdown cell
        - The popover snippets when you enter code in python cell
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## `bg-card` & `text-card-foreground`

        - even rows of markdown table

        | Syntax      | Description | Example           |
        |-------------|-------------|-------------------|
        | **Header**  | Row Title   | Content Here      |
        | **Row 1**   | First Cell  | `Some code`       |
        | **Row 2**   | Second Cell | *Italicized text* |
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## `bg-primary & text-primary-foreground`

        - `machine stats` on the right bottom of notebook
        - the header of `Documentation` panel
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md("""## `bg-secondary & text-secondary-foreground`""")


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## `bg-accent` & `text-accent-foreground`

        - Floating Outline on the right center of the notebook
        - Side panels on the left of the notebook
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## `destructive` & `destructive-foreground`

        - delete button in each cell
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        r"""
        ## other args

        - `border`: borders of cells, buttons, etc.
        - `input`: markdown table separator line between header and content
        - ...
        """
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(r"""# Marimo UI Components""")


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.hstack(
        [
            mo.ui.button(
                label="Danger",
                kind="danger",
            ),
            mo.ui.button(label="Info", kind="info"),
            mo.ui.button(
                label="Neutral",
                kind="neutral",
            ),
            mo.ui.button(
                label="Success",
                kind="success",
            ),
            mo.ui.button(
                label="Warn",
                kind="warn",
            ),
            mo.ui.button(
                label="Alert",
                kind="alert",
            ),
        ],
        justify="space-around",
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.chat(model="")


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.checkbox()


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.code_editor()


@app.cell(hide_code=True)
def __(data, mo) -> None:
    mo.ui.dataframe(data.cars())


@app.cell(hide_code=True)
def __(data, mo) -> None:
    mo.ui.data_explorer(data.cars())


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.date(
        value="2022-06-01",
        start="2022-01-01",
        stop="2022-12-31",
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.dropdown(
        options={"one": 1, "two": 2, "three": 3},
        value="one",
        label="pick a number",
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.file(kind="area")


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.file_browser()


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.md(
        """
        **Your form.**

        {name}

        {date}
        """
    ).batch(
        name=mo.ui.text(label="name"),
        date=mo.ui.date(label="date"),
    ).form(show_clear_button=True, bordered=True)


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.microphone()


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.multiselect(options=["a", "b", "c"], label="choose some options")


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.number(start=1, stop=10, step=2)


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.radio(
        options={"one": 1, "two": 2, "three": 3},
        value="one",
        label="pick a number",
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.range_slider(start=1, stop=10, step=2, value=[2, 6], show_value=True)


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.refresh(
        options=["1m", "5m 30s", "10m"],
        default_interval="10m",
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.switch()


@app.cell(hide_code=True)
def __(data, mo) -> None:
    mo.ui.table(
        data.cars(),
        show_column_summaries=True,
        selection="multi",
    )


@app.cell(hide_code=True)
def __(mo):
    tab1 = mo.vstack(
        [
            mo.ui.slider(1, 10),
            mo.ui.text(),
            mo.ui.date(),
        ]
    )

    tab2 = mo.md("You can show arbitrary content in a tab.")

    tabs = mo.ui.tabs({"Heading 1": tab1, "Heading 2": tab2})
    tabs
    return tab1, tab2, tabs


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.hstack(
        [
            mo.ui.text(value="Hello, Text", kind="text"),
            mo.ui.text(value="Hello, Password", kind="password"),
            mo.ui.text(value="Hello, Email", kind="email"),
            mo.ui.text(value="Hello, URL", kind="url"),
        ],
        justify="space-around",
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.ui.text_area()


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.accordion(
        {
            "Door 1": mo.md("Nothing!"),
            "Door 2": mo.md("Nothing!"),
            "Door 3": mo.md(
                "![goat](https://images.unsplash.com/photo-1524024973431-2ad916746881)"
            ),
        }
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.carousel(
        [
            mo.md("# Introduction"),
            "By the marimo team",
            mo.md("## What is marimo?"),
            mo.md("![marimo moss ball](https://marimo.io/logo.png)"),
            mo.md("## Questions?"),
        ]
    )


@app.cell(hide_code=True)
def __(mo) -> None:
    mo.vstack(
        [
            mo.callout("This is a info callout", kind="info"),
            mo.callout("This is a neutral callout", kind="neutral"),
            mo.callout("This is a warn callout", kind="warn"),
            mo.callout("This is a danger callout", kind="danger"),
            mo.callout("This is a success callout", kind="success"),
        ]
    )


@app.cell(hide_code=True)
def __():
    from vega_datasets import data

    return (data,)


@app.cell(hide_code=True)
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
