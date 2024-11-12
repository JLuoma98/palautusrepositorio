from urllib import request
from project import Project

import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomllib.loads(content)["tool"]["poetry"]

        name = data["name"]
        description = data["description"]
        project_license = data["license"]
        authors = data["authors"]
        dependencies = data["dependencies"]
        dev_dependencies = data["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, project_license, authors, dependencies, dev_dependencies)
