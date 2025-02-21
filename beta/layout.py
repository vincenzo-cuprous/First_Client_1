# layout.py
def serve_base_html(active_section):
    return f"""
        <!DOCTYPE html>
        <html data-theme="light">
        <head>
            <title>My Portfolio - {active_section.title()}</title>
            <link href="https://cdn.jsdelivr.net/npm/daisyui@4.7.2/dist/full.min.css" rel="stylesheet" type="text/css" />
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
        </head>
        <body class="bg-base-100">
            <!-- Navigation -->
            <nav class="navbar bg-base-200 shadow-lg sticky top-0 z-50">
                <div class="container mx-auto px-4">
                    <div class="flex justify-between items-center py-4 w-full">
                        <a href="/" class="text-xl font-bold">My Portfolio</a>
                        <div class="flex gap-4">
                            <a href="/" class="btn btn-ghost {active_section == 'home' and 'btn-active'}">
                                <i class="fas fa-home mr-2"></i>Home
                            </a>
                            <a href="/about" class="btn btn-ghost {active_section == 'about' and 'btn-active'}">
                                <i class="fas fa-user mr-2"></i>About
                            </a>
                            <a href="/skills" class="btn btn-ghost {active_section == 'skills' and 'btn-active'}">
                                <i class="fas fa-tools mr-2"></i>Skills
                            </a>
                            <a href="/projects" class="btn btn-ghost {active_section == 'projects' and 'btn-active'}">
                                <i class="fas fa-project-diagram mr-2"></i>Projects
                            </a>
                            <a href="/contact" class="btn btn-ghost {active_section == 'contact' and 'btn-active'}">
                                <i class="fas fa-envelope mr-2"></i>Contact
                            </a>
                            <button onclick="toggleTheme()" class="btn btn-ghost">
                                <i class="fas fa-moon"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </nav>
    """

def serve_footer():
    return """
            <script>
                function toggleTheme() {
                    const html = document.documentElement;
                    const currentTheme = html.getAttribute('data-theme');
                    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                    html.setAttribute('data-theme', newTheme);
                }
            </script>
        </body>
        </html>
    """
