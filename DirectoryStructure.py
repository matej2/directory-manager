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
                            "name": "dto",
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
                            "name": "main",
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
                            "name": "regression",
                            "description": "Regression tests",
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
                    "subdirectories": [
                        {
                            "name": "staging",
                            "description": "Migration files for staging environment",
                            "subdirectories": []
                        },
                    ]
                },
                {
                    "name": "seeders",
                    "description": "Database seed data",
                    "subdirectories": []
                },
                {
                    "name": "scripts",
                    "description": "Deployment and maintenance scripts",
                    "subdirectories": [
                        {
                            "name": "Deploy",
                            "description": "Deploy scripts for each environment.",
                            "subdirectories": []
                        },
                        {
                            "name": "Tests",
                            "description": "Test scripts for each environment.",
                            "subdirectories": []
                        },
                        {
                            "name": "Build",
                            "description": "Build scripts for each environment.",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": ".env.example",
                    "description": "Environment variables template",
                    "subdirectories": []
                },
                {
                    "name": "README.md",
                    "description": "Project documentation",
                    "subdirectories": []
                }
            ]
        }