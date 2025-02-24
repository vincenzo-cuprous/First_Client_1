from dash import html

def serve_islamic_content():
    """
    Returns the content for the Islamic book library page using DaisyUI components.
    """
    return html.Div([
        # Hero Section
        html.Section(
            html.Div([
                html.Div([
                    html.H1(
                        "Islamic Book Library",
                        className="text-6xl font-bold mb-6 text-center"
                    ),
                    html.P(
                        "Explore a collection of Islamic books covering various topics such as Quran, Hadith, Fiqh, and more.",
                        className="text-xl text-center text-base-content/80 mb-8"
                    ),
                ], className="max-w-4xl mx-auto px-4"),
            ], className="hero min-h-[50vh] bg-base-200"),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),

        # Book Collection Section
        html.Section(
            html.Div([
                html.H2(
                    "Book Collection", 
                    className="text-4xl font-bold mb-12 text-center"
                ),
                html.Div([
                    # Book Cards Grid (only one card remains)
                    html.Div([
                        create_book_card(
                            title="The Noble Quran",
                            description="The holy book of Islam, containing the words of Allah as revealed to Prophet Muhammad (PBUH). This translation includes detailed commentary and contextual explanations.",
                            author="Translation by Dr. Muhammad Muhsin Khan",
                            category="Sacred Text",
                            rating=5.0,
                            image_url="/api/placeholder/300/400",
                            link="https://example.com/quran"
                        ),
                    ], className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"),
                ], className="container mx-auto px-4 py-20"),
            ], className="bg-base-100"),
        ),

        # Call to Action Section
        html.Section(
            html.Div([
                html.Div([
                    html.H2(
                        "Want to Contribute?",
                        className="text-4xl font-bold mb-6 text-center"
                    ),
                    html.P(
                        "If you have Islamic books or resources to share, feel free to reach out to us.",
                        className="text-xl text-center text-base-content/80 mb-8"
                    ),
                    html.Div([
                        html.A([
                            html.I(className="fas fa-envelope mr-2"),
                            "Contact Us"
                        ], 
                        href="/contact",
                        className="btn btn-primary btn-lg hover:scale-105 transition-transform"),
                    ], className="text-center"),
                ], className="max-w-2xl mx-auto px-4 py-20"),
            ], className="bg-base-200"),
        ),
    ])

def create_book_card(title, description, author, category, rating, image_url, link):
    """
    Helper function to create consistent book cards with DaisyUI styling.
    """
    return html.Div([
        # Card container with DaisyUI card class
        html.Div([
            # Image container
            html.Figure(
                html.Img(
                    src=image_url,
                    alt=f"Cover of {title}",
                    className="w-full h-48 object-cover rounded-t-2xl"
                ),
                className="relative"
            ),
            # Card body
            html.Div([
                # Category badge
                html.Div([
                    html.I(className="fas fa-tag mr-2"),
                    html.Span(
                        category,
                        className="badge badge-primary badge-outline"
                    ),
                ], className="mb-2 flex items-center"),
                # Title
                html.H2([
                    html.I(className="fas fa-book mr-2"),
                    title
                ], className="card-title text-xl mb-2 flex items-center"),
                # Author
                html.P([
                    html.I(className="fas fa-user mr-2"),
                    author
                ], className="text-base-content/70 text-sm mb-2"),
                # Rating
                html.Div([
                    create_rating_stars(rating),
                    html.Span(
                        f"{rating}/5",
                        className="ml-2 text-sm font-bold"
                    )
                ], className="flex items-center mb-3"),
                # Description
                html.P([
                    html.I(className="fas fa-info-circle mr-2"),
                    description
                ], className="text-base-content/70 text-sm mb-4 line-clamp-3"),
                # Action buttons
                html.Div([
                    html.A([
                        html.I(className="fas fa-book-reader mr-2"),
                        "Read Online"
                    ],
                    href=link,
                    target="_blank",
                    className="btn btn-primary w-full hover:scale-105 transition-transform"),
                ], className="card-actions justify-end"),
            ], className="card-body"),
        ], className="card bg-base-200 shadow-xl hover:shadow-2xl transition-all duration-300"),
    ], className="w-full")

def create_rating_stars(rating):
    """
    Creates a star rating display using Font Awesome icons.
    """
    full_stars = int(rating)
    has_half_star = rating % 1 >= 0.5
    empty_stars = 5 - full_stars - (1 if has_half_star else 0)
    
    stars = []
    
    # Add full stars
    for _ in range(full_stars):
        stars.append(html.I(className="fas fa-star text-yellow-400"))
    
    # Add half star if applicable
    if has_half_star:
        stars.append(html.I(className="fas fa-star-half-alt text-yellow-400"))
    
    # Add empty stars
    for _ in range(empty_stars):
        stars.append(html.I(className="far fa-star text-yellow-400"))
    
    return html.Div(stars, className="flex gap-1")
