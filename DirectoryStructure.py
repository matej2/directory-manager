class DirectoryStructure:
    @staticmethod
    def get_structure():
        return {
            "name": "🏠 Home",
            "type": "directory",
            "description": "Root directory for personal files",
            "subdirectories": [
                {
                    "name": "📂 Documents",
                    "type": "directory",
                    "description": "Text files and documents",
                    "subdirectories": [
                        {
                            "name": "👤 Personal",
                            "type": "directory",
                            "description": "IDs, contracts, personal records",
                            "subdirectories": []
                        },
                        {
                            "name": "💼 Work",
                            "type": "directory",
                            "description": "Resumes, work-related documents",
                            "subdirectories": []
                        },
                        {
                            "name": "📚 Studies",
                            "type": "directory",
                            "description": "Courses, textbooks, research",
                            "subdirectories": []
                        },
                        {
                            "name": "💰 Financial",
                            "type": "directory",
                            "description": "Taxes, invoices, receipts",
                            "subdirectories": [
                                {
                                    "name": "📄 tax_2023.pdf",
                                    "type": "file",
                                    "description": "Annual tax documents",
                                    "subdirectories": []
                                }
                            ]
                        },
                        {
                            "name": "📝 Templates",
                            "type": "directory",
                            "description": "Document templates",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "🎬 Media",
                    "type": "directory",
                    "description": "All media files",
                    "subdirectories": [
                        {
                            "name": "📷 Photos",
                            "type": "directory",
                            "description": "Personal photos",
                            "subdirectories": [
                                {
                                    "name": "👨‍👩‍👧‍👦 Family",
                                    "type": "directory",
                                    "description": "Family photos",
                                    "subdirectories": []
                                },
                                {
                                    "name": "✈️ Travel",
                                    "type": "directory",
                                    "description": "Travel photos",
                                    "subdirectories": []
                                },
                                {
                                    "name": "🎉 Events",
                                    "type": "directory",
                                    "description": "Special occasions",
                                    "subdirectories": []
                                },
                                {
                                    "name": "🗂 Sorted",
                                    "type": "directory",
                                    "description": "Organized by date (YYYY-MM-DD)",
                                    "subdirectories": []
                                }
                            ]
                        },
                        {
                            "name": "🎥 Videos",
                            "type": "directory",
                            "description": "Personal videos",
                            "subdirectories": [
                                {
                                    "name": "🏠 Home Videos",
                                    "type": "directory",
                                    "description": "Family videos",
                                    "subdirectories": []
                                },
                                {
                                    "name": "🎬 Movies",
                                    "type": "directory",
                                    "description": "Downloaded movies",
                                    "subdirectories": []
                                },
                                {
                                    "name": "📺 TV Shows",
                                    "type": "directory",
                                    "description": "TV series episodes",
                                    "subdirectories": []
                                }
                            ]
                        },
                        {
                            "name": "🎵 Music",
                            "type": "directory",
                            "description": "Audio files",
                            "subdirectories": [
                                {
                                    "name": "💿 Albums",
                                    "type": "directory",
                                    "description": "Organized by artist/album",
                                    "subdirectories": []
                                },
                                {
                                    "name": "🎧 Playlists",
                                    "type": "directory",
                                    "description": "Custom playlists",
                                    "subdirectories": []
                                },
                                {
                                    "name": "🎶 favorite_song.mp3",
                                    "type": "file",
                                    "description": "Music files",
                                    "subdirectories": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "🛠 Projects",
                    "type": "directory",
                    "description": "Personal projects and hobbies",
                    "subdirectories": [
                        {
                            "name": "💻 Coding",
                            "type": "directory",
                            "description": "Programming projects",
                            "subdirectories": []
                        },
                        {
                            "name": "🔨 DIY",
                            "type": "directory",
                            "description": "Home improvement projects",
                            "subdirectories": []
                        },
                        {
                            "name": "🎨 Art",
                            "type": "directory",
                            "description": "Creative works",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "📥 Downloads",
                    "type": "directory",
                    "description": "Temporary download storage",
                    "subdirectories": []
                },
                {
                    "name": "💾 Backups",
                    "type": "directory",
                    "description": "System and file backups",
                    "subdirectories": [
                        {
                            "name": "🖥 System",
                            "type": "directory",
                            "description": "OS and software backups",
                            "subdirectories": []
                        },
                        {
                            "name": "☁️ Cloud Sync",
                            "type": "directory",
                            "description": "Cloud storage mirror",
                            "subdirectories": []
                        }
                    ]
                },
                {
                    "name": "🤝 Shared",
                    "type": "directory",
                    "description": "Files to share with others",
                    "subdirectories": []
                },
                {
                    "name": "📱 Applications",
                    "type": "directory",
                    "description": "Portable apps and software",
                    "subdirectories": []
                },
                {
                    "name": "📑 README.txt",
                    "type": "file",
                    "description": "Directory structure guide",
                    "subdirectories": []
                }
            ]
        }
