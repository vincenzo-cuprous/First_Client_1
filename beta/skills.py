# skills.py
from layout import serve_base_html, serve_footer

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
                                    <div class="badge badge-primary">HTML+CSS+Javascript</div>
                                    <div class="badge badge-primary">Javascript+React</div>
                                    <div class="badge badge-primary">Tailwind Css</div>
                                    <div class="badge badge-primary">Python+Dash</div>
                                    <div class="badge badge-primary">Go+Webassembly With Go</div>
                                    <div class="badge badge-primary">Rust+Yew</div>
                                </div>
                            </div>
                        </div>
                        <div class="card bg-base-100 shadow-xl">
                            <div class="card-body">
                                <h3 class="card-title"><i class="fas fa-server mr-2"></i>Backend</h3>
                                <div class="flex flex-wrap gap-2">
                                    <div class="badge badge-secondary">Node.js+Express</div>
                                    <div class="badge badge-secondary">Python+Flask</div>
                                    <div class="badge badge-secondary">Go+Gin</div>
                                    <div class="badge badge-secondary">Rust+Actix</div>
                                    <div class="badge badge-secondary">RESTAPI</div>
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
                                    <div class="badge badge-accent">Railway+CI/CD</div>
                                    <div class="badge badge-accent">Render+Terraform</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    """
    content += serve_footer()
    return content
