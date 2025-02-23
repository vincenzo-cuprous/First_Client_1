# projects.py
from layout import serve_base_html, serve_footer

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
