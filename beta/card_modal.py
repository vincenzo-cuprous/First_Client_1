# card_modal.py
def serve_card_modal():
    return """
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
    """
