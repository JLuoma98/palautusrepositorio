class Project:
    def __init__(self, name, description, project_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = project_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n".join(f"- {dep}" for dep in dependencies) if dependencies else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license}"
            "\n"
            "\nAuthors:\n"
            f"- {"\n- ".join(self.authors)}"
            "\n"
            "\nDependencies:\n"
            f"{self._stringify_dependencies(self.dependencies)}"
            "\n"
            "\nDevelopment dependencies:\n"
            f"{self._stringify_dependencies(self.dev_dependencies)}"
        )
