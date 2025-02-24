# contact.py
from dash import html
import dash_bootstrap_components as dbc

def serve_contact():
    """Returns the contact page content for the Dash app with Tailwind CSS, DaisyUI, and Font Awesome icons."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("Contact Me", className="text-3xl font-bold text-center mb-8 text-primary"),
                dbc.Card([
                    dbc.CardBody([
                        dbc.Form([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Name", className="label-text text-base-content"),
                                    dbc.Input(type="text", placeholder="Your Name", className="input input-bordered w-full")
                                ], className="mb-4")
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Email", className="label-text text-base-content"),
                                    dbc.Input(type="email", placeholder="Your Email", className="input input-bordered w-full")
                                ], className="mb-4")
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Message", className="label-text text-base-content"),
                                    dbc.Textarea(placeholder="Your Message", className="textarea textarea-bordered w-full h-24")
                                ], className="mb-4")
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(
                                        [html.I(className="fas fa-paper-plane mr-2"), "Send Message"],
                                        color="primary",
                                        className="btn btn-primary mt-6 w-full"
                                    )
                                ])
                            ])
                        ])
                    ])
                ], className="card bg-base-100 shadow-xl p-6")
            ], className="max-w-2xl mx-auto")
        ], className="min-h-screen py-20 bg-base-200")
    ], fluid=True)
