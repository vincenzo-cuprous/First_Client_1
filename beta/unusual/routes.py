# routes.py
from layout import serve_base_html, serve_footer

def serve_home():
    content = serve_base_html('home')
    content += """
            <div class="hero min-h-screen bg-base-200">
                <div class="hero-content text-center">
                    <div class="max-w-2xl">
                        <h1 class="text-5xl font-bold">Hi, I'm John Doe</h1>
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

def serve_about():
    content = serve_base_html('about')
    content += """
            <div class="min-h-screen py-20">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-bold text-center mb-8">About Me</h2>
                    <div class="grid md:grid-cols-2 gap-8 items-center">
                        <div>
                            <p class="mb-4">I'm a passionate developer with 5+ years of experience in building web applications and solving complex problems.</p>
                            <p>I specialize in JavaScript, Python, and cloud technologies, always eager to learn and adapt to new challenges.</p>
                        </div>
                        <div class="card bg-base-200 shadow-xl">
                            <div class="card-body">
                                <div class="stats stats-vertical lg:stats-horizontal shadow">
                                    <div class="stat">
                                        <div class="stat-title">Years Experience</div>
                                        <div class="stat-value">5+</div>
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

def serve_skills():
    content = serve_base_html('skills')
    content += """
            <div class="min-h-screen py-20">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-bold text-center mb-8">My Skills</h2>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <div class="card bg-base-100 shadow-xl">
                            <div class="card-body">
                                <h3 class="card-title"><i class="fas fa-code mr-2"></i>Frontend</h3>
                                <div class="flex flex-wrap gap-2">
                                    <div class="badge badge-primary">HTML</div>
                                    <div class="badge badge-primary">CSS</div>
                                    <div class="badge badge-primary">JavaScript</div>
                                    <div class="badge badge-primary">React</div>
                                    <div class="badge badge-primary">Tailwind</div>
                                </div>
                            </div>
                        </div>
                        <div class="card bg-base-100 shadow-xl">
                            <div class="card-body">
                                <h3 class="card-title"><i class="fas fa-server mr-2"></i>Backend</h3>
                                <div class="flex flex-wrap gap-2">
                                    <div class="badge badge-secondary">Node.js</div>
                                    <div class="badge badge-secondary">Python</div>
                                    <div class="badge badge-secondary">Express</div>
                                    <div class="badge badge-secondary">Django</div>
                                    <div class="badge badge-secondary">GraphQL</div>
                                </div>
                            </div>
                        </div>
                        <div class="card bg-base-100 shadow-xl">
                            <div class="card-body">
                                <h3 class="card-title"><i class="fas fa-cloud mr-2"></i>DevOps</h3>
                                <div class="flex flex-wrap gap-2">
                                    <div class="badge badge-accent">Docker</div>
                                    <div class="badge badge-accent">Kubernetes</div>
                                    <div class="badge badge-accent">AWS</div>
                                    <div class="badge badge-accent">CI/CD</div>
                                    <div class="badge badge-accent">Terraform</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    """
    content += serve_footer()
    return content

def serve_projects():
    content = serve_base_html('projects')
    content += """
            <div class="min-h-screen py-20">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-bold text-center mb-8">My Projects</h2>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <div class="card bg-base-200 shadow-xl">
                            <figure class="px-4 pt-4">
                                <img src="https://placehold.co/600x400" alt="Project" class="rounded-xl" />
                            </figure>
                            <div class="card-body">
                                <h3 class="card-title">E-Commerce Platform</h3>
                                <p>Full-stack e-commerce solution with payment integration</p>
                                <div class="card-actions justify-end">
                                    <button class="btn btn-primary"><i class="fas fa-info-circle mr-2"></i>View Details</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    """
    content += serve_footer()
    return content

def serve_contact():
    content = serve_base_html('contact')
    content += """
            <div class="min-h-screen py-20">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-bold text-center mb-8">Contact Me</h2>
                    <div class="max-w-2xl mx-auto">
                        <form class="card bg-base-100 shadow-xl p-6">
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Name</span>
                                </label>
                                <input type="text" placeholder="Your Name" class="input input-bordered" />
                            </div>
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Email</span>
                                </label>
                                <input type="email" placeholder="Your Email" class="input input-bordered" />
                            </div>
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Message</span>
                                </label>
                                <textarea class="textarea textarea-bordered h-24" placeholder="Your Message"></textarea>
                            </div>
                            <div class="form-control mt-6">
                                <button class="btn btn-primary"><i class="fas fa-paper-plane mr-2"></i>Send Message</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
    """
    content += serve_footer()
    return content
