# home.py
from layout import serve_base_html, serve_footer

def serve_home():
    content = serve_base_html('home')
    content += """
            <div class="hero min-h-screen bg-base-200">
                <div class="hero-content text-center">
                    <div class="max-w-2xl">
                        <h1 class="text-5xl font-bold">Hi, I'm Cazzano</h1>
                        <p class="py-6">Full Stack Developer | Tech Enthusiast | Problem Solver</p>
                        <div class="flex justify-center gap-4">
                            <a href="/projects" class="btn btn-primary"><i class="fas fa-eye mr-2"></i>View My Work</a>
                            <a href="/contact" class="btn btn-secondary"><i class="fas fa-paper-plane mr-2"></i>Contact Me</a>
                        </div>
                    </div>
                </div>
            </div>
    """
    content += serve_footer()
    return content
