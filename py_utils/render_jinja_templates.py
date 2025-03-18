import os
from jinja2 import Environment, FileSystemLoader


def render_jinja_templates(working_dir: str, context: dict = {}):
    print(f"rendering jinja templates in '{working_dir}'")
    env = Environment(
        loader=FileSystemLoader(
            searchpath=working_dir,
        ),
    )

    for file in os.listdir(working_dir):
        if file.endswith(".j2"):
            template = env.get_template(file)
            with open(
                os.path.join(working_dir, template.name.replace(".j2", "")), "w"
            ) as f:
                f.write(template.render(context))


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
