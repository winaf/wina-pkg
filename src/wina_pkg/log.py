import click


def debug(msg: str) -> None:
    click.echo(f"[wina-pkg] {msg}")
