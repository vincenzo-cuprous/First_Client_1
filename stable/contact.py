# contact.py
from layout import serve_base_html, serve_footer

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
