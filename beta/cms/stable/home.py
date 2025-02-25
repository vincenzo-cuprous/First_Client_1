from dash import html
import dash_bootstrap_components as dbc

def serve_home():
    """
    Returns the home page content for the Dash app with a modern, dynamic layout.
    Navbar and footer are handled by the main app layout.
    """
    return html.Div([
        # Hero Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H1([
                            "Creating ",
                            html.Span("Digital", className="text-primary"),
                            " Experiences"
                        ], className="text-6xl font-bold mb-6 leading-tight"),
                        html.P(
                            "Full Stack Developer crafting innovative solutions with modern technologies",
                            className="text-xl text-base-content/80 mb-8"
                        ),
                        dbc.Row([
                            dbc.Col(
                                dbc.Button([
                                    html.I(className="fas fa-rocket mr-2"),
                                    "View Projects"
                                ], href="/projects", size="lg", 
                                   className="btn btn-primary hover:scale-105 transition-transform"),
                                width="auto"
                            ),
                            dbc.Col(
                                dbc.Button([
                                    html.I(className="fas fa-paper-plane mr-2"),
                                    "Get in Touch"
                                ], href="/contact", size="lg", outline=True,
                                   className="btn btn-outline hover:scale-105 transition-transform"),
                                width="auto"
                            ),
                        ], className="gap-4"),
                    ], md=8, lg=6),
                ], className="min-h-[90vh] items-center"),
            ], fluid=True),
            className="bg-gradient-to-br from-base-100 to-base-200"
        ),

        # Skills Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H2("Skills & Expertise", 
                               className="text-4xl font-bold mb-12 text-center"),
                        dbc.Row([
                            # Skill Cards
                            dbc.Col(create_skill_card(
                                "Frontend", 
                                "React, Vue, TailwindCSS",
                                "fas fa-code"
                            ), md=4),
                            dbc.Col(create_skill_card(
                                "Backend",
                                "Python, Node.js, PostgreSQL",
                                "fas fa-server"
                            ), md=4),
                            dbc.Col(create_skill_card(
                                "DevOps",
                                "Docker, AWS, CI/CD",
                                "fas fa-cloud"
                            ), md=4),
                        ], className="gap-6"),
                    ], className="py-20")
                ])
            ], fluid=True),
            className="bg-base-100"
        ),

        # Quick Contact Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H2("Let's Work Together", 
                               className="text-4xl font-bold mb-6 text-center"),
                        html.P(
                            "Have a project in mind? Let's discuss how we can make it happen.",
                            className="text-xl text-center text-base-content/80 mb-8"
                        ),
                        html.Div([
                            dbc.Button([
                                html.I(className="fas fa-envelope mr-2"),
                                "Start a Conversation"
                            ], href="/contact", size="lg",
                               className="btn btn-primary hover:scale-105 transition-transform"),
                        ], className="text-center")
                    ], md=8, className="mx-auto"),
                ], className="py-20")
            ], fluid=True),
            className="bg-base-200"
        ),
    ])

def create_skill_card(title, description, icon_class):
    """Helper function to create consistent skill cards."""
    return html.Div([
        html.Div([
            html.I(className=f"{icon_class} text-3xl text-primary mb-4"),
            html.H3(title, className="text-xl font-bold mb-2"),
            html.P(description, className="text-base-content/70"),
        ], className="p-6 rounded-xl bg-base-200 hover:scale-105 transition-transform")
    ])
