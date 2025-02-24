from dash import html
import dash_bootstrap_components as dbc

def serve_islamic_content():
    """
    Returns the content for the Islamic book library page.
    """
    return html.Div([
        # Hero Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H1([
                            "Islamic Book Library"
                        ], className="text-6xl font-bold mb-6 leading-tight text-center"),
                        html.P(
                            "Explore a collection of Islamic books covering various topics such as Quran, Hadith, Fiqh, and more.",
                            className="text-xl text-center text-base-content/80 mb-8"
                        ),
                    ], md=12),
                ], className="min-h-[50vh] items-center"),
            ], fluid=True),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),

        # Book Collection Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H2("Book Collection", 
                               className="text-4xl font-bold mb-12 text-center"),
                        dbc.Row([
                            # Book Cards
                            dbc.Col(create_book_card(
                                title="The Noble Quran",
                                description="The holy book of Islam, containing the words of Allah as revealed to Prophet Muhammad (PBUH). This translation includes detailed commentary and contextual explanations.",
                                author="Translation by Dr. Muhammad Muhsin Khan",
                                category="Sacred Text",
                                rating=5.0,
                                image_url="/api/placeholder/300/400",
                                link="https://example.com/quran"
                            ), md=4),
                            dbc.Col(create_book_card(
                                title="Sahih al-Bukhari",
                                description="The most authentic collection of Hadiths, containing the sayings and actions of Prophet Muhammad (PBUH). Comprehensive compilation with detailed chain of narration.",
                                author="Imam Muhammad al-Bukhari",
                                category="Hadith",
                                rating=4.9,
                                image_url="/api/placeholder/300/400",
                                link="https://example.com/bukhari"
                            ), md=4),
                            dbc.Col(create_book_card(
                                title="Fiqh us-Sunnah",
                                description="A comprehensive guide to Islamic jurisprudence based on the Quran and Sunnah. Covers various aspects of Islamic law and daily practices.",
                                author="Sayyid Saabiq",
                                category="Fiqh",
                                rating=4.8,
                                image_url="/api/placeholder/300/400",
                                link="https://example.com/fiqh"
                            ), md=4),
                        ], className="gap-6"),
                    ], className="py-20")
                ])
            ], fluid=True),
            className="bg-base-100"
        ),

        # Call to Action Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H2("Want to Contribute?", 
                               className="text-4xl font-bold mb-6 text-center"),
                        html.P(
                            "If you have Islamic books or resources to share, feel free to reach out to us.",
                            className="text-xl text-center text-base-content/80 mb-8"
                        ),
                        html.Div([
                            dbc.Button([
                                html.I(className="fas fa-envelope mr-2"),
                                "Contact Us"
                            ], href="/contact", size="lg",
                               className="btn btn-primary hover:scale-105 transition-transform"),
                        ], className="text-center")
                    ], md=8, className="mx-auto"),
                ], className="py-20")
            ], fluid=True),
            className="bg-base-200"
        ),
    ])

def create_book_card(title, description, author, category, rating, image_url, link):
    """
    Helper function to create consistent book cards with enhanced information.
    
    Parameters:
    - title: str, title of the book
    - description: str, book description
    - author: str, name of the author
    - category: str, book category/genre
    - rating: float, book rating (0-5)
    - image_url: str, URL of the book cover image
    - link: str, URL to read the book online
    """
    return html.Div([
        html.Div([
            # Book Cover Image
            html.Img(
                src=image_url,
                alt=f"Cover of {title}",
                className="w-full h-48 object-cover rounded-t-xl"
            ),
            html.Div([
                # Category Badge
                html.Span(
                    category,
                    className="bg-primary/10 text-primary px-3 py-1 rounded-full text-sm mb-2 inline-block"
                ),
                # Title
                html.H3(title, className="text-xl font-bold mb-2"),
                # Author
                html.P([
                    html.I(className="fas fa-user mr-2"),
                    author
                ], className="text-base-content/70 text-sm mb-2"),
                # Rating
                html.Div([
                    html.Span([
                        html.I(className="fas fa-star text-yellow-400"),
                        f" {rating}/5"
                    ], className="text-sm font-bold"),
                ], className="mb-3"),
                # Description
                html.P(
                    description,
                    className="text-base-content/70 text-sm mb-4 line-clamp-3"
                ),
                # Read Online Button
                dbc.Button(
                    [html.I(className="fas fa-book-reader mr-2"), "Read Online"],
                    href=link,
                    target="_blank",
                    className="btn btn-primary w-full hover:scale-105 transition-transform"
                ),
            ], className="p-4")
        ], className="rounded-xl bg-base-200 hover:shadow-lg transition-all duration-300 h-full flex flex-col")
    ], className="h-full")
