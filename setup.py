from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",#alterar a versão / toda vez que salvar 
    author="Letica",
    author_email="leticiasuli1@hotmail.com",
    description="My short descriptio", #descrição do que vai ser feito
    long_description=page_description,
    long_description_content_type="text/markdown", # para mostrar o tipo
    url="my_github_repository_project_link", # 
    packages=find_packages(), # encontra automaticamente 
    install_requires=requirements,
    python_requires='>=3.8', # conversção necessaria para o Python
)