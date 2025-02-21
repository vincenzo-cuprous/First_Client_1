# islamic_content.py
from layout import serve_base_html, serve_footer

def serve_islamic_books():
        content = serve_base_html('islamic_books')
        content += """
                    <div class="min-h-screen bg-base-200 py-12">
                        <div class="container mx-auto px-4">
                            <div class="text-center mb-12">
                                <h1 class="text-5xl font-bold mb-4">Islamic Books Collection</h1>
                                <p class="text-lg">Explore our curated collection of authentic Islamic literature</p>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                <!-- Quran Section -->
                                <div class="card bg-base-100 shadow-xl">
                                    <div class="card-body">
                                        <h2 class="card-title text-2xl">Holy Quran</h2>
                                        <p>Various translations and interpretations of the Holy Quran</p>
                                        <div class="card-actions justify-end mt-4">
                                            <a href="/quran" class="btn btn-primary">Browse</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Hadith Section -->
                                <div class="card bg-base-100 shadow-xl">
                                    <div class="card-body">
                                        <h2 class="card-title text-2xl">Hadith Collections</h2>
                                        <p>Authentic collections including Sahih Bukhari, Muslim, and more</p>
                                        <div class="card-actions justify-end mt-4">
                                            <a href="/hadith" class="btn btn-primary">Browse</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Islamic History -->
                                <div class="card bg-base-100 shadow-xl">
                                    <div class="card-body">
                                        <h2 class="card-title text-2xl">Islamic History</h2>
                                        <p>Books about Islamic history, prophets, and civilization</p>
                                        <div class="card-actions justify-end mt-4">
                                            <a href="/history" class="btn btn-primary">Browse</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Fiqh Section -->
                                <div class="card bg-base-100 shadow-xl">
                                    <div class="card-body">
                                        <h2 class="card-title text-2xl">Fiqh & Islamic Law</h2>
                                        <p>Books on Islamic jurisprudence and practical guidance</p>
                                        <div class="card-actions justify-end mt-4">
                                            <a href="/fiqh" class="btn btn-primary">Browse</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Biography Section -->
                                <div class="card bg-base-100 shadow-xl">
                                    <div class="card-body">
                                        <h2 class="card-title text-2xl">Seerah & Biography</h2>
                                        <p>Life of Prophet Muhammad (ﷺ) and his companions</p>
                                        <div class="card-actions justify-end mt-4">
                                            <a href="/seerah" class="btn btn-primary">Browse</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Contemporary Works -->
                                <div class="card bg-base-100 shadow-xl">
                                    <div class="card-body">
                                        <h2 class="card-title text-2xl">Contemporary Works</h2>
                                        <p>Modern Islamic scholars and their contributions</p>
                                        <div class="card-actions justify-end mt-4">
                                            <a href="/contemporary" class="btn btn-primary">Browse</a>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Search and Filter Section -->
                            <div class="mt-12 text-center">
                                <h2 class="text-2xl font-bold mb-4">Can't find what you're looking for?</h2>
                                <div class="flex justify-center gap-4">
                                    <a href="/search" class="btn btn-secondary">
                                        <i class="fas fa-search mr-2"></i>Search Books
                                    </a>
                                    <a href="/request" class="btn btn-accent">
                                        <i class="fas fa-book-medical mr-2"></i>Request a Book
                                </a>
                                    </div>
                                </div>
                            </div>
                </div>
        """
        content += serve_footer()
        return content
