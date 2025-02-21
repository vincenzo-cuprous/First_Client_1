# islamic_content.py
from layout import serve_base_html, serve_footer

def serve_islamic_books():
    content = serve_base_html('islamic_books')
    content += """
        <div class="min-h-screen bg-base-200 py-12">
            <div class="container mx-auto px-4">
                <div class="text-center mb-8">
                    <h1 class="text-5xl font-bold mb-4">Islamic Books Collection</h1>
                    <p class="text-lg mb-8">Explore our curated collection of authentic Islamic literature</p>
                    
                    <!-- Search and Filter Section -->
                    <div class="max-w-2xl mx-auto mb-12">
                        <div class="join w-full">
                            <input type="text" placeholder="Search by title, author, or category..." class="input input-bordered join-item w-full" />
                            <button class="btn btn-primary join-item">
                                <i class="fas fa-search"></i>
                            </button>
                        </div>
                        <div class="flex justify-center gap-4 mt-4">
                            <a href="/advanced-search" class="btn btn-outline btn-sm">
                                <i class="fas fa-filter mr-2"></i>Advanced Search
                            </a>
                            <a href="/request" class="btn btn-accent btn-sm">
                                <i class="fas fa-book-medical mr-2"></i>Request a Book
                            </a>
                        </div>
                    </div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- Quran with Translation -->
                    <div class="card bg-base-100 shadow-xl">
                        <figure class="px-6 pt-6">
                            <img src="/api/placeholder/300/200" alt="Quran" class="rounded-xl shadow" />
                        </figure>
                        <div class="card-body">
                            <div class="flex justify-between items-start">
                                <h2 class="card-title text-2xl">The Noble Quran</h2>
                                <div class="badge badge-primary">
                                    <i class="fas fa-book-quran mr-2"></i>Quran
                                </div>
                            </div>
                            <p class="text-sm text-gray-600">Translation & Commentary</p>
                            <div class="flex items-center gap-2 mt-2">
                                <span class="font-semibold flex items-center">
                                    <i class="fas fa-user-pen mr-2"></i>Author:
                                </span>
                                <span>Dr. Muhammad Muhsin Khan</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <div class="rating rating-sm">
                                    <input type="radio" name="rating-1" class="mask mask-star-2 bg-orange-400" checked />
                                    <input type="radio" name="rating-1" class="mask mask-star-2 bg-orange-400" checked />
                                    <input type="radio" name="rating-1" class="mask mask-star-2 bg-orange-400" checked />
                                    <input type="radio" name="rating-1" class="mask mask-star-2 bg-orange-400" checked />
                                    <input type="radio" name="rating-1" class="mask mask-star-2 bg-orange-400" checked />
                                </div>
                                <span class="text-sm">(4.9/5)</span>
                            </div>
                            <div class="card-actions justify-end mt-4">
                                <button onclick="document.getElementById('book-modal-1').showModal()" class="btn btn-primary">
                                    <i class="fas fa-book-open mr-2"></i>Read Now
                                </button>
                                <a href="#" class="btn btn-outline">
                                    <i class="fas fa-bookmark"></i>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Modal for Quran -->
                    <dialog id="book-modal-1" class="modal">
                        <div class="modal-box w-11/12 max-w-4xl">
                            <div class="flex flex-col md:flex-row gap-6">
                                <div class="md:w-1/3">
                                    <img src="/api/placeholder/300/400" alt="Quran" class="w-full rounded-xl shadow" />
                                </div>
                                <div class="md:w-2/3">
                                    <h3 class="text-3xl font-bold mb-2">The Noble Quran</h3>
                                    <div class="badge badge-primary mb-4">
                                        <i class="fas fa-book-quran mr-2"></i>Quran
                                    </div>
                                    <p class="text-lg mb-4">Translation & Commentary</p>
                                    <div class="flex items-center gap-2 mb-4">
                                        <span class="font-semibold flex items-center">
                                            <i class="fas fa-user-pen mr-2"></i>Author:
                                        </span>
                                        <span>Dr. Muhammad Muhsin Khan</span>
                                    </div>
                                    <div class="flex flex-wrap gap-4 mb-6">
                                        <button class="btn btn-primary">
                                            <i class="fas fa-download mr-2"></i>Download
                                        </button>
                                        <button class="btn btn-secondary">
                                            <i class="fas fa-eye mr-2"></i>Preview
                                        </button>
                                    </div>
                                    <div class="prose max-w-none mb-8">
                                        <p>This translation of the Holy Quran has been prepared with brief notes and introduction. The purpose of the translation is to make the Quran accessible to English-speaking readers.</p>
                                    </div>
                                    
                                    <!-- Comments Section -->
                                    <div class="border-t pt-6">
                                        <h4 class="text-xl font-semibold mb-4 flex items-center">
                                            <i class="fas fa-comments mr-2"></i>Comments
                                        </h4>
                                        
                                        <!-- Comment Form -->
                                        <div class="mb-6">
                                            <textarea class="textarea textarea-bordered w-full mb-2" placeholder="Share your thoughts..."></textarea>
                                            <button class="btn btn-primary">
                                                <i class="fas fa-paper-plane mr-2"></i>Post Comment
                                            </button>
                                        </div>
                                        
                                        <!-- Existing Comments -->
                                        <div class="space-y-4">
                                            <div class="bg-base-200 p-4 rounded-lg">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <i class="fas fa-user-circle text-2xl"></i>
                                                    <span class="font-semibold">Ahmad Hassan</span>
                                                    <span class="text-sm text-gray-500">2 days ago</span>
                                                </div>
                                                <p>Excellent translation with comprehensive commentary. The language is clear and accessible.</p>
                                            </div>
                                            
                                            <div class="bg-base-200 p-4 rounded-lg">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <i class="fas fa-user-circle text-2xl"></i>
                                                    <span class="font-semibold">Sarah Ahmed</span>
                                                    <span class="text-sm text-gray-500">5 days ago</span>
                                                </div>
                                                <p>Very helpful for understanding complex verses. The footnotes provide valuable context.</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="modal-action">
                                <form method="dialog">
                                    <button class="btn btn-circle btn-ghost absolute right-2 top-2">
                                        <i class="fas fa-times text-xl"></i>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </dialog>

                    <!-- Similar structure for other books... -->
                    
                </div>
            </div>
        </div>
    """
    content += serve_footer()
    
    # Add JavaScript for modal functionality
    content += """
        <script>
            // Add any additional JavaScript functionality here
            document.addEventListener('DOMContentLoaded', function() {
                // Modal functionality is handled by HTML dialog element
            });
        </script>
    """
    return content
