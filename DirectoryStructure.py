class DirectoryStructure:
    @staticmethod
    def get_structure() -> dict:
        return {
            "name": "Home",
            "type": "directory",
            "description": "Root directory for personal files",
            "subdirectories": [
                {
                    "name": "Documents",
                    "type": "directory",
                    "description": "Text files and documents",
                    "subdirectories": [
                        {
                            "name": "Personal",
                            "type": "directory",
                            "description": "IDs, contracts, personal records",
                            "subdirectories": []
                        },
                        {
                            "name": "Work",
                            "type": "directory",
                            "description": "Resumes, work-related documents",
                            "subdirectories": []
                        },
                        {
                            "name": "Studies",
                            "type": "directory",
                            "description": "Courses, textbooks, research",
                            "subdirectories": []
                        },
                        {
                            "name": "Financial",
                            "type": "directory",
                            "description": "Taxes, invoices, receipts",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "Media",
                    "type": "directory",
                    "description": "All media files",
                    "subdirectories": [
                        {
                            "name": "Photos",
                            "type": "directory",
                            "description": "Personal photos",
                            "subdirectories": [
                                {
                                    "name": "Family",
                                    "type": "directory",
                                    "description": "Family photos",
                                    "subdirectories": []
                                },
                                {
                                    "name": "️Travel",
                                    "type": "directory",
                                    "description": "Travel photos",
                                    "subdirectories": []
                                },
                                {
                                    "name": "Events",
                                    "type": "directory",
                                    "description": "Special occasions",
                                    "subdirectories": []
                                }
                            ]
                        },
                        {
                            "name": "Videos",
                            "type": "directory",
                            "description": "Personal videos",
                            "subdirectories": [
                                {
                                    "name": "Home Videos",
                                    "type": "directory",
                                    "description": "Family videos",
                                    "subdirectories": []
                                },
                                {
                                    "name": "Movies",
                                    "type": "directory",
                                    "description": "Downloaded movies",
                                    "subdirectories": []
                                },
                                {
                                    "name": "TV Shows",
                                    "type": "directory",
                                    "description": "TV series episodes",
                                    "subdirectories": []
                                }
                            ]
                        },
                        {
                            "name": "Music",
                            "type": "directory",
                            "description": "Audio files",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "Projects",
                    "type": "directory",
                    "description": "Personal projects and hobbies",
                    "subdirectories": [
                        {
                            "name": "Coding",
                            "type": "directory",
                            "description": "Programming projects",
                            "subdirectories": []
                        },
                        {
                            "name": "DIY",
                            "type": "directory",
                            "description": "Home improvement projects",
                            "subdirectories": []
                        },
                        {
                            "name": "Art",
                            "type": "directory",
                            "description": "Creative works",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "Downloads",
                    "type": "directory",
                    "description": "Temporary download storage",
                    "subdirectories": []
                },
                {
                    "name": "Backups",
                    "type": "directory",
                    "description": "System and file backups",
                    "subdirectories": [
                        {
                            "name": "System",
                            "type": "directory",
                            "description": "OS and software backups",
                            "subdirectories": []
                        },
                        {
                            "name": "️Cloud Sync",
                            "type": "directory",
                            "description": "Cloud storage mirror",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "Shared",
                    "type": "directory",
                    "description": "Files to share with others",
                    "subdirectories": []
                },
                {
                    "name": "Applications",
                    "type": "directory",
                    "description": "Portable apps and software",
                    "subdirectories": []
                },
                {
                    "name": "README.txt",
                    "type": "file",
                    "description": "Directory structure guide",
                    "subdirectories": []
                }
            ]
        }

    def does_exist(self, dir_name):
        if len(self.find_directory_name(dir_name, [], self.get_structure())) > 0:
            return True
        else:
            return False

    def find_directory_name(self, lookup: str, hierarchy: list[str], curr_structure: dict):
        hierarchy.append(curr_structure.get("name"))
        dir_subdirectories = curr_structure.get("subdirectories")

        for subdir in dir_subdirectories:
            if lookup in subdir.get("name"):
                return hierarchy

            if subdir.get("subdirectories") is not None:
                self.find_directory_name(lookup, hierarchy, subdir)

        return []
