class DirectoryStructure:
    @staticmethod
    def get_structure():
        return {
            "name": "backend",
            "description": "Root directory for the backend project",
            "subdirectories": [
                {
                    "name": "src",
                    "description": "Source code directory",
                    "subdirectories": [
                        {
                            "name": "controllers",
                            "description": "Request handlers",
                            "subdirectories": []
                        },
                        {
                            "name": "services",
                            "description": "Business logic layer",
                            "subdirectories": []
                        },
                        {
                            "name": "repositories",
                            "description": "Database operations layer",
                            "subdirectories": []
                        },
                        {
                            "name": "models",
                            "description": "Data models/entities",
                            "subdirectories": []
                        },
                        {
                            "name": "dtos",
                            "description": "Data transfer objects",
                            "subdirectories": []
                        },
                        {
                            "name": "interfaces",
                            "description": "Type/interface definitions",
                            "subdirectories": []
                        },
                        {
                            "name": "middleware",
                            "description": "Auth, logging, and other middleware",
                            "subdirectories": []
                        },
                        {
                            "name": "utils",
                            "description": "Helper functions and utilities",
                            "subdirectories": []
                        },
                        {
                            "name": "config",
                            "description": "Configuration files",
                            "subdirectories": []
                        },
                        {
                            "name": "constants",
                            "description": "Constant values",
                            "subdirectories": []
                        },
                        {
                            "name": "routes",
                            "description": "Route definitions",
                            "subdirectories": []
                        },
                        {
                            "name": "validators",
                            "description": "Validation logic",
                            "subdirectories": []
                        },
                        {
                            "name": "app.ts|js",
                            "description": "Application entry point",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "tests",
                    "description": "Test files directory",
                    "subdirectories": [
                        {
                            "name": "unit",
                            "description": "Unit tests",
                            "subdirectories": []
                        },
                        {
                            "name": "integration",
                            "description": "Integration tests",
                            "subdirectories": []
                        },
                        {
                            "name": "e2e",
                            "description": "End-to-end tests",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "migrations",
                    "description": "Database migration files",
                    "subdirectories": []
                },
                {
                    "name": "seeders",
                    "description": "Database seed data",
                    "subdirectories": []
                },
                {
                    "name": "scripts",
                    "description": "Deployment and maintenance scripts",
                    "subdirectories": []
                },
                {
                    "name": ".env",
                    "description": "Environment variables file",
                    "subdirectories": []
                },
                {
                    "name": ".env.example",
                    "description": "Environment variables template",
                    "subdirectories": []
                },
                {
                    "name": "package.json",
                    "description": "Project metadata and dependencies",
                    "subdirectories": []
                },
                {
                    "name": "tsconfig.json",
                    "description": "TypeScript configuration",
                    "subdirectories": []
                },
                {
                    "name": "README.md",
                    "description": "Project documentation",
                    "subdirectories": []
                }
            ]
        }