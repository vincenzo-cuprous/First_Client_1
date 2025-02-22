# islamic_content.py
from layout import serve_base_html, serve_footer
from card_modal import serve_card_modal
import requests
from urllib.parse import quote

def generate_rating_stars(rating):
    """Generate HTML for rating stars based on book rating"""
    rating = float(rating)
    stars_html = ""
    for i in range(5):
        checked = "checked" if i < int(rating) else ""
        stars_html += f'<input type="radio" class="mask mask-star-2 bg-orange-400" {checked} disabled />'
    return stars_html

def serve_islamic_books():
    # Fetch books from the backend
    try:
        response = requests.get('http://127.0.0.1:5000/books')
        books = response.json()
    except requests.exceptions.RequestException as e:
        books = []
        print(f"Error fetching books: {e}")

    content = serve_base_html('islamic_books')
    
    # Add search and filter JavaScript
    content += """
        <script>
        function searchBooks() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.querySelectorAll('.book-card');
            
            cards.forEach(card => {
                const title = card.querySelector('.book-title').textContent.toLowerCase();
                const author = card.querySelector('.book-author').textContent.toLowerCase();
                const category = card.querySelector('.book-category').textContent.toLowerCase();
                
                if (title.includes(searchTerm) || author.includes(searchTerm) || category.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        function filterByCategory(category) {
            const cards = document.querySelectorAll('.book-card');
            
            cards.forEach(card => {
                const cardCategory = card.querySelector('.book-category').textContent;
                if (category === 'all' || cardCategory === category) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
        </script>
    """

    # Main content
    content += """
        <div class="min-h-screen bg-base-200 py-12">
            <div class="container mx-auto px-4">
                <div class="text-center mb-8">
                    <h1 class="text-5xl font-bold mb-4">Islamic Books Collection</h1>
                    <p class="text-lg mb-8">Explore our curated collection of authentic Islamic literature</p>
                    
                    <!-- Search and Filter Section -->
                    <div class="max-w-2xl mx-auto mb-12">
                        <div class="join w-full">
                            <input type="text" 
                                   id="searchInput" 
                                   placeholder="Search by title, author, or category..." 
                                   class="input input-bordered join-item w-full"
                                   onkeyup="searchBooks()" />
                            <button class="btn btn-primary join-item" onclick="searchBooks()">
                                <i class="fas fa-search"></i>
                            </button>
                        </div>
                        
                        <!-- Category Filter -->
                        <div class="flex justify-center gap-2 mt-4 flex-wrap">
                            <button onclick="filterByCategory('all')" 
                                    class="btn btn-outline btn-sm">
                                All
                            </button>
                            <button onclick="filterByCategory('Quran')" 
                                    class="btn btn-outline btn-sm">
                                Quran
                            </button>
                            <button onclick="filterByCategory('Hadith')" 
                                    class="btn btn-outline btn-sm">
                                Hadith
                            </button>
                            <button onclick="filterByCategory('Fiqh')" 
                                    class="btn btn-outline btn-sm">
                                Fiqh
                            </button>
                            <button onclick="filterByCategory('Seerah')" 
                                    class="btn btn-outline btn-sm">
                                Seerah
                            </button>
                        </div>
                        
                        <div class="flex justify-center gap-4 mt-4">
                            <a href="/request" class="btn btn-accent btn-sm">
                                <i class="fas fa-book-medical mr-2"></i>Request a Book
                            </a>
                        </div>
                    </div>
                </div>
                
                <!-- Book Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    """

    # Generate book cards
    for book in books:
        content += f"""
            <div class="card bg-base-100 shadow-xl book-card">
                <figure class="px-6 pt-6">
                    <img src="{book['picture_url']}" 
                         alt="{book['book_name']}" 
                         class="rounded-xl shadow max-h-64 object-cover" />
                </figure>
                <div class="card-body">
                    <div class="flex justify-between items-start">
                        <h2 class="card-title text-2xl book-title">{book['book_name']}</h2>
                        <div class="badge badge-primary book-category">
                            <i class="fas fa-book-quran mr-2"></i>{book['category']}
                        </div>
                    </div>
                    <p class="text-sm text-gray-600">{book['description'][:150]}...</p>
                    <div class="flex items-center gap-2 mt-2">
                        <span class="font-semibold flex items-center">
                            <i class="fas fa-user-pen mr-2"></i>Author:
                        </span>
                        <span class="book-author">{book['author_name']}</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <div class="rating rating-sm">
                            {generate_rating_stars(book['ratings'])}
                        </div>
                        <span class="text-sm">({book['ratings']}/5)</span>
                    </div>
                    <div class="card-actions justify-end mt-4">
                        <button onclick="document.getElementById('book-modal-{book['book_id']}').showModal()" 
                                class="btn btn-primary">
                            <i class="fas fa-book-open mr-2"></i>Read Now
                        </button>
                        <a href="{book['download_url']}" 
                           class="btn btn-outline" 
                           target="_blank"
                           download="{quote(book['book_name'])}.pdf">
                            <i class="fas fa-download"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Modal for this book -->
            {serve_card_modal(book)}
        """

    # Close main containers
    content += """
                </div>
                
                <!-- Pagination -->
                <div class="flex justify-center mt-12">
                    <div class="join">
                        <button class="join-item btn">«</button>
                        <button class="join-item btn">Page 1</button>
                        <button class="join-item btn">»</button>
                    </div>
                </div>
            </div>
        </div>
    """

    # Add footer
    content += serve_footer()
    
    # Add additional JavaScript for loading states and error handling
    content += """
        <script>
            // Show loading state
            function showLoading(element) {
                element.classList.add('loading');
                element.disabled = true;
            }
            
            // Hide loading state
            function hideLoading(element) {
                element.classList.remove('loading');
                element.disabled = false;
            }

            // Error toast notification
            function showError(message) {
                const toast = document.createElement('div');
                toast.className = 'toast toast-error';
                toast.textContent = message;
                document.body.appendChild(toast);
                setTimeout(() => toast.remove(), 3000);
            }
            
            // Initialize tooltips and other UI elements
            document.addEventListener('DOMContentLoaded', function() {
                // Any additional initialization can go here
            });
        </script>
    """
    
    return content
