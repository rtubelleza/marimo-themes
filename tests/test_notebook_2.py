import marimo

__generated_with = "0.9.10"
app = marimo.App(css_file="/Users/chanhuizhihou/Library/Application Support/mtheme/themes/coldme.css")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
