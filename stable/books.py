from dash import html, dcc

def serve_book_page():
    """
    Returns the content for the book details page using DaisyUI and Font Awesome.
    """
    return html.Div([
        # Hero Section
        html.Section(
            html.Div([
                html.Div([
                    html.H1(
                        "Book Details",
                        className="text-6xl font-bold mb-6 text-center"
                    ),
                    html.P(
                        "Explore detailed information about the book, including reviews and download options.",
                        className="text-xl text-center text-base-content/80 mb-8"
                    ),
                ], className="max-w-4xl mx-auto px-4"),
            ], className="hero min-h-[30vh] bg-base-200"),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),

        # Book Details Section
        html.Section(
            html.Div([
                # Book Information
                html.Div([
                    # Book Image
                    html.Div([
                        html.Img(
                            src="/api/placeholder/400/600",  # Placeholder image URL
                            alt="Book Cover",
                            className="w-full h-auto rounded-lg shadow-lg"
                        ),
                    ], className="w-full md:w-1/3 lg:w-1/4 mb-8 md:mb-0"),

                    # Book Details
                    html.Div([
                        # Book Name with Icon
                        html.H2(
                            [html.I(className="fas fa-book mr-2"), "The Noble Quran"],
                            className="text-4xl font-bold mb-4 flex items-center"
                        ),
                        # Author Name with Icon
                        html.P(
                            [html.I(className="fas fa-user mr-2"), "Author: Dr. Muhammad Muhsin Khan"],
                            className="text-xl text-base-content/80 mb-4 flex items-center"
                        ),
                        # Category with Icon
                        html.P(
                            [html.I(className="fas fa-tag mr-2"), "Category: Sacred Text"],
                            className="text-xl text-base-content/80 mb-4 flex items-center"
                        ),
                        # Rating with Icon
                        html.Div([
                            create_rating_stars(5.0),
                            html.Span(
                                "5.0/5",
                                className="ml-2 text-xl font-bold"
                            )
                        ], className="flex items-center mb-4"),
                        # Description with Icon
                        html.P(
                            [html.I(className="fas fa-info-circle mr-2"), 
                             "Description: The holy book of Islam, containing the words of Allah as revealed to Prophet Muhammad (PBUH). This translation includes detailed commentary and contextual explanations."
                            ],
                            className="text-lg text-base-content/80 mb-8 flex items-start"
                        ),
                        # Buttons for Download and Preview
                        html.Div([
                            html.Button(
                                [html.I(className="fas fa-download mr-2"), "Download"],
                                className="btn btn-primary mr-4 hover:scale-105 transition-transform"
                            ),
                            html.Button(
                                [html.I(className="fas fa-eye mr-2"), "Preview"],
                                className="btn btn-secondary hover:scale-105 transition-transform"
                            ),
                        ], className="flex flex-wrap gap-4 mb-8"),
                    ], className="w-full md:w-2/3 lg:w-3/4 md:pl-8"),
                ], className="flex flex-col md:flex-row container mx-auto px-4 py-12"),

                # Comment Section
                html.Div([
                    html.H2(
                        "Comments",
                        className="text-3xl font-bold mb-6"
                    ),
                    # Comment Input Form
                    html.Div([
                        html.Textarea(
                            id="comment-input",
                            placeholder="Write your comment here...",
                            className="textarea textarea-bordered w-full mb-4"
                        ),
                        html.Button(
                            [html.I(className="fas fa-paper-plane mr-2"), "Submit Comment"],
                            id="submit-comment",
                            className="btn btn-primary hover:scale-105 transition-transform"
                        ),
                    ], className="mb-8"),
                    # Display Comments
                    html.Div(id="comments-list", className="space-y-4", children=[
                        # Example Comment
                        html.Div([
                            html.P(
                                "This is an amazing book! Highly recommended.",
                                className="text-base-content/80"
                            ),
                            html.P(
                                "By: User123",
                                className="text-sm text-base-content/60"
                            ),
                        ], className="bg-base-200 p-4 rounded-lg"),
                    ]),
                ], className="container mx-auto px-4 py-12 bg-base-100"),
            ], className="bg-base-100"),
        ),
    ])

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
