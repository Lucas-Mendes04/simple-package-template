from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

setup(
    name="gerador_senha",
    version="0.0.1",
    author="lucas",
    author_email="lucas@gmail.com",
    description="Pacote utilizado para geração de senha",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lucas-Mendes04/simple-package-template"
    packages=find_packages(),
    # install_requires=requirements,
    python_requires='>=3.8',
)