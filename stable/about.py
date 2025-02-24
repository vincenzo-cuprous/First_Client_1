from dash import html
import dash_bootstrap_components as dbc

def serve_about():
    """
    Returns a redesigned about page with modern styling and improved content organization.
    """
    return html.Div([
        # Hero Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H1(
                            "About Me",
                            className="text-5xl font-bold mb-6 text-center"
                        ),
                        html.Div(
                            html.P(
                                "Transforming ideas into elegant solutions",
                                className="text-xl text-base-content/80 text-center"
                            ),
                            className="mb-12"
                        )
                    ], className="text-center")
                ])
            ], fluid=True),
            className="pt-20 pb-12 bg-gradient-to-b from-base-200 to-base-100"
        ),

        # Main Content Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    # Profile and Bio
                    dbc.Col([
                        html.Div([
                            html.Div(
                                className="w-48 h-48 rounded-full bg-primary/10 mb-8 mx-auto overflow-hidden",
                                children=[
                                    html.I(
                                        className="fas fa-user-circle text-7xl text-primary/40",
                                        style={"lineHeight": "12rem", "width": "100%", "textAlign": "center"}
                                    )
                                ]
                            ),
                            html.H2("Full Stack Developer", className="text-2xl font-bold mb-4 text-center"),
                            html.P(
                                """I'm a passionate developer with 2+ years of experience in building web applications 
                                and solving complex problems. My journey in tech has been driven by curiosity 
                                and a constant desire to learn and grow.""",
                                className="text-base-content/80 mb-6 text-center"
                            ),
                            html.Div([
                                create_tech_badge("JavaScript"),
                                create_tech_badge("Python"),
                                create_tech_badge("Go"),
                                create_tech_badge("Rust"),
                                create_tech_badge("React"),
                                create_tech_badge("Cloud"),
                            ], className="flex flex-wrap justify-center gap-2 mb-8")
                        ], className="bg-base-100 p-8 rounded-2xl shadow-lg")
                    ], md=6, className="mb-8"),

                    # Stats and Achievements
                    dbc.Col([
                        html.Div([
                            html.H2("Impact & Achievements", className="text-2xl font-bold mb-6"),
                            
                            # Stats Grid
                            html.Div([
                                create_stat_card(
                                    "Years Experience",
                                    "2+",
                                    "fas fa-clock"
                                ),
                                create_stat_card(
                                    "Projects Completed",
                                    "50+",
                                    "fas fa-check-circle"
                                ),
                                create_stat_card(
                                    "Happy Clients",
                                    "100%",
                                    "fas fa-heart"
                                ),
                            ], className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8"),

                            # Key Focus Areas
                            html.Div([
                                create_focus_area(
                                    "Problem Solving",
                                    "Approaching challenges with analytical thinking and creative solutions",
                                    "fas fa-lightbulb"
                                ),
                                create_focus_area(
                                    "Clean Code",
                                    "Writing maintainable, efficient, and well-documented code",
                                    "fas fa-code"
                                ),
                                create_focus_area(
                                    "Continuous Learning",
                                    "Staying updated with latest technologies and best practices",
                                    "fas fa-graduation-cap"
                                ),
                            ], className="space-y-4")
                        ], className="bg-base-100 p-8 rounded-2xl shadow-lg h-full")
                    ], md=6)
                ], className="gap-8"),
            ], fluid=True, className="max-w-7xl"),
            className="py-12"
        ),

        # Call to Action Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H2("Let's Build Something Together", 
                               className="text-3xl font-bold mb-4 text-center"),
                        html.P(
                            "Interested in collaborating? Let's discuss your next project.",
                            className="text-xl text-base-content/80 mb-6 text-center"
                        ),
                        html.Div([
                            dbc.Button([
                                html.I(className="fas fa-paper-plane mr-2"),
                                "Get in Touch"
                            ], href="/contact", size="lg",
                               className="btn btn-primary hover:scale-105 transition-transform"),
                        ], className="text-center")
                    ], md=8, className="mx-auto")
                ])
            ], fluid=True),
            className="py-20 bg-base-200"
        )
    ])

def create_tech_badge(text):
    """Helper function to create consistent technology badges."""
    return html.Span(
        text,
        className="px-3 py-1 rounded-full bg-primary/10 text-primary text-sm font-medium"
    )

def create_stat_card(title, value, icon):
    """Helper function to create consistent stat cards."""
    return html.Div([
        html.I(className=f"{icon} text-2xl text-primary mb-2"),
        html.Div(value, className="text-3xl font-bold mb-1"),
        html.Div(title, className="text-sm text-base-content/70"),
    ], className="bg-base-200 p-6 rounded-xl text-center hover:scale-105 transition-transform")

def create_focus_area(title, description, icon):
    """Helper function to create consistent focus area cards."""
    return html.Div([
        html.Div([
            html.I(className=f"{icon} text-xl text-primary mr-3"),
            html.H3(title, className="text-lg font-semibold"),
        ], className="flex items-center mb-2"),
        html.P(description, className="text-base-content/70"),
    ], className="p-4 rounded-lg bg-base-200")
