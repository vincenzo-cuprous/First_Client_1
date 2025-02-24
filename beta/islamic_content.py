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
                                "The Quran",
                                "The holy book of Islam, containing the words of Allah as revealed to Prophet Muhammad (PBUH).",
                                "fas fa-book-quran",
                                "https://example.com/quran"
                            ), md=4),
                            dbc.Col(create_book_card(
                                "Sahih al-Bukhari",
                                "A collection of authentic Hadiths compiled by Imam al-Bukhari.",
                                "fas fa-book",
                                "https://example.com/bukhari"
                            ), md=4),
                            dbc.Col(create_book_card(
                                "Fiqh us-Sunnah",
                                "A comprehensive book on Islamic jurisprudence based on the Sunnah.",
                                "fas fa-balance-scale",
                                "https://example.com/fiqh"
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

def create_book_card(title, description, icon_class, link):
    """
    Helper function to create consistent book cards.
    """
    return html.Div([
        html.Div([
            html.I(className=f"{icon_class} text-3xl text-primary mb-4"),
            html.H3(title, className="text-xl font-bold mb-2"),
            html.P(description, className="text-base-content/70 mb-4"),
            dbc.Button(
                "Read Online",
                href=link,
                target="_blank",
                className="btn btn-outline-primary hover:scale-105 transition-transform"
            ),
        ], className="p-6 rounded-xl bg-base-200 hover:scale-105 transition-transform text-center")
    ])
