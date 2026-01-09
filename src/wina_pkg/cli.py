import rich_click as click

from .files import resolve_files, collect_from_dirs
from .ar import build_command, default_ar_cmd
from .exec import run_command


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-o", "--output", type=click.Path(dir_okay=False, writable=True), metavar="FILE",required=True, help="export package to FILE")
@click.option("-d", "--dir", metavar="DIR", help="include every object file in DIR using autodiscovery")
@click.option("-f", "--file", "files", metavar="FILES", multiple=True, help="include object FILES manually")
@click.option("-E", "--exclude", metavar="FILES", multiple=True, help="exclude object FILES included by autodiscovery")
@click.option("-i", "--independent", is_flag=True, help="disable autodiscovery")
@click.option("-n", "--dry-run", is_flag=True, help="print the commands that were going to be executed without executing them")
@click.option("-v", "--version", is_flag=True, help="show version and exit")
def cli(version, output, dir, files, exclude, independent, dry_run):
    """wina-pkg - The WINA Packager"""
    if version:
        click.echo("wina-pkg 0.1.0") # TODO: Make it update automatically
        return

    objects = []
    objects.extend(resolve_files(files))

    if not independent:
        if not dir:
            raise click.UsageError("Autodiscovery needs a directory in order to find objects")
        objects.extend(collect_from_dirs(dir, set(exclude)))

    if not objects:
        raise click.UsageError("No object files were found.")

    cmd = build_command(default_ar_cmd(), output, objects)
    run_command(cmd, dry_run)
