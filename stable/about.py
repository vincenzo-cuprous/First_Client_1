# about.py
from layout import serve_base_html, serve_footer

def serve_about():
    content = serve_base_html('about')
    content += """
            <div class="min-h-screen py-20">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-bold text-center mb-8">About Me</h2>
                    <div class="grid md:grid-cols-2 gap-8 items-center">
                        <div>
                            <p class="mb-4">I'm a passionate developer with 2+ years of experience in building web applications and solving complex problems.</p>
                            <p>I specialize in JavaScript, Python, Go, Rust and cloud technologies, always eager to learn and adapt to new challenges.</p>
                        </div>
                        <div class="card bg-base-200 shadow-xl">
                            <div class="card-body">
                                <div class="stats stats-vertical lg:stats-horizontal shadow">
                                    <div class="stat">
                                        <div class="stat-title">Years Experience</div>
                                        <div class="stat-value">2+</div>
                                    </div>
                                    <div class="stat">
                                        <div class="stat-title">Projects Completed</div>
                                        <div class="stat-value">50+</div>
                                    </div>
                                    <div class="stat">
                                        <div class="stat-title">Happy Clients</div>
                                        <div class="stat-value">100%</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    """
    content += serve_footer()
    return content
