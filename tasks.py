from invoke import task


@task
def build(ctx):
    ctx.run('pandoc -t revealjs -s talk-efficient-prototyping.md -o '
            'talk-efficient-prototyping.html '
            '-V revealjs-url=.')
    ctx.run('open http://localhost:8000/talk-efficient-prototyping.html')


@task
def init_node(ctx):
    ctx.run('npm install')


@task
def start_node(ctx):
    ctx.run('npm start &')
