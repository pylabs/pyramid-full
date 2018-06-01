{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Getting Started
---------------

- Change directory into your newly created project.

    cd {{ cookiecutter.repo_name }}

- Install the project in editable mode with its development requirements.

    pipenv install --dev

- Enter to your project virtual environment.

    pipenv shell

- Run your project's tests.

    pytest

- Run your project in development mode.

    pserve development.ini --reload
