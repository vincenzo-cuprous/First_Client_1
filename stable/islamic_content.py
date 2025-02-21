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
                                                                    <a href="/book/noble-quran" class="btn btn-primary">
                                                                        <i class="fas fa-book-open mr-2"></i>Read Now
                                                                    </a>
                                                                    <a href="#" class="btn btn-outline">
                                                                        <i class="fas fa-bookmark"></i>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                        </div>

                                                        <!-- Sahih Al-Bukhari -->
                                                        <div class="card bg-base-100 shadow-xl">
                                                            <figure class="px-6 pt-6">
                                                                <img src="/api/placeholder/300/200" alt="Sahih Al-Bukhari" class="rounded-xl shadow" />
                                                            </figure>
                                                                            <div class="card-body">
                                                                <div class="flex justify-between items-start">
                                                                    <h2 class="card-title text-2xl">Sahih Al-Bukhari</h2>
                                                                    <div class="badge badge-secondary">
                                                                        <i class="fas fa-scroll mr-2"></i>Hadith
                                                    </div>
                                                                </div>
                                                                <p class="text-sm text-gray-600">Complete Collection of Authentic Hadiths</p>
                                                                <div class="flex items-center gap-2 mt-2">
                                                                    <span class="font-semibold flex items-center">
                                                                        <i class="fas fa-user-pen mr-2"></i>Author:
                                                                    </span>
                                                                                    <span>Imam Muhammad al-Bukhari</span>
                                                                                </div>
                                                                                <div class="flex items-center gap-2">
                                                                    <div class="rating rating-sm">
                                                                        <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" />
                                                                    </div>
                                                                                    <span class="text-sm">(4.8/5)</span>
                                                                </div>
                                                                <div class="card-actions justify-end mt-4">
                                                                    <a href="/book/sahih-bukhari" class="btn btn-primary">
                                                                        <i class="fas fa-book-open mr-2"></i>Read Now
                                                                    </a>
                                                                    <a href="#" class="btn btn-outline">
                                                                        <i class="fas fa-bookmark"></i>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                        </div>

                                                        <!-- The Sealed Nectar -->
                                                        <div class="card bg-base-100 shadow-xl">
                                                            <figure class="px-6 pt-6">
                                                                <img src="/api/placeholder/300/200" alt="The Sealed Nectar" class="rounded-xl shadow" />
                                                            </figure>
                                                                            <div class="card-body">
                                                                <div class="flex justify-between items-start">
                                                                    <h2 class="card-title text-2xl">The Sealed Nectar</h2>
                                                                    <div class="badge badge-accent">
                                                                        <i class="fas fa-history mr-2"></i>Seerah
                                                    </div>
                                                                </div>
                                                                <p class="text-sm text-gray-600">Biography of Prophet Muhammad ﷺ</p>
                                                                <div class="flex items-center gap-2 mt-2">
                                                                    <span class="font-semibold flex items-center">
                                                                        <i class="fas fa-user-pen mr-2"></i>Author:
                                                                    </span>
                                                                                    <span>Safiur Rahman Mubarakpuri</span>
                                                                                </div>
                                                                                <div class="flex items-center gap-2">
                                                                    <div class="rating rating-sm">
                                                                        <input type="radio" name="rating-3" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-3" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-3" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-3" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-3" class="mask mask-star-2 bg-orange-400" checked />
                                                                    </div>
                                                                    <span class="text-sm">(4.9/5)</span>
                                                                </div>
                                                                <div class="card-actions justify-end mt-4">
                                                                    <a href="/book/sealed-nectar" class="btn btn-primary">
                                                                        <i class="fas fa-book-open mr-2"></i>Read Now
                                                                    </a>
                                                                    <a href="#" class="btn btn-outline">
                                                                        <i class="fas fa-bookmark"></i>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                        </div>

                                                        <!-- Riyad as-Salihin -->
                                                        <div class="card bg-base-100 shadow-xl">
                                                            <figure class="px-6 pt-6">
                                                                <img src="/api/placeholder/300/200" alt="Riyad as-Salihin" class="rounded-xl shadow" />
                                                            </figure>
                                                                            <div class="card-body">
                                                                <div class="flex justify-between items-start">
                                                                    <h2 class="card-title text-2xl">Riyad as-Salihin</h2>
                                                                    <div class="badge badge-secondary">
                                                                        <i class="fas fa-scroll mr-2"></i>Hadith
                                                    </div>
                                                                </div>
                                                                <p class="text-sm text-gray-600">The Gardens of the Righteous</p>
                                                                <div class="flex items-center gap-2 mt-2">
                                                                    <span class="font-semibold flex items-center">
                                                                        <i class="fas fa-user-pen mr-2"></i>Author:
                                                                    </span>
                                                                                    <span>Imam An-Nawawi</span>
                                                                                </div>
                                                                                <div class="flex items-center gap-2">
                                                                    <div class="rating rating-sm">
                                                                        <input type="radio" name="rating-4" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-4" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-4" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-4" class="mask mask-star-2 bg-orange-400" checked />
                                                                        <input type="radio" name="rating-4" class="mask mask-star-2 bg-orange-400" />
                                                                    </div>
                                                                                    <span class="text-sm">(4.7/5)</span>
                                                                </div>
                                                                <div class="card-actions justify-end mt-4">
                                                                    <a href="/book/riyad-salihin" class="btn btn-primary">
                                                                        <i class="fas fa-book-open mr-2"></i>Read Now
                                                                    </a>
                                                                    <a href="#" class="btn btn-outline">
                                                                        <i class="fas fa-bookmark"></i>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                        </div>

                                                    </div>
                                                </div>
                                            </div>
                                    """
                    content += serve_footer()
                    return content
