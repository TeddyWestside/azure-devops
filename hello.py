import click


@click.command(help="This is a simple program that greets you")
@click.option("--name", prompt="Your Name", help="Need name")
@click.option("--color", prompt="Your Color", help="This is your color")
def hello(name, color):
    if name == "Thor":
        click.echo("Hello, Thor. You are always red.")
        click.echo(click.style(f"Hello, {name}. You are always {color}.", fg="red"))
    else:
        click.echo(click.style(f"Hello, {name}. You are always {color}.", fg=f"{color}"))


if __name__ == '__main__':
    hello()
