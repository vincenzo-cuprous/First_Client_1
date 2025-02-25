# projects.py
from dash import html
import dash_bootstrap_components as dbc

def create_project_card(title, description, image_url, button_text="View Details"):
    """Creates a project card with a title, description, image, and a button."""
    return dbc.Card(
        [
            dbc.CardImg(src=image_url, top=True, className="rounded-t-lg"),
            dbc.CardBody(
                [
                    html.H3(title, className="card-title text-primary mb-3"),
                    html.P(description, className="card-text text-secondary mb-4"),
                    dbc.Button(
                        [
                            html.I(className="fas fa-info-circle mr-2"),
                            button_text
                        ],
                        color="primary",
                        className="btn btn-primary"
                    )
                ]
            )
        ],
        className="card h-100 shadow-sm"
    )

def serve_projects():
    """Returns the projects page content for the Dash app."""
    projects = [
        {
            "title": "E-Commerce Platform",
            "description": "Full-stack e-commerce solution with payment integration.",
            "image_url": "https://placehold.co/600x400"
        },
        {
            "title": "Portfolio Website",
            "description": "Personal portfolio website showcasing skills and projects.",
            "image_url": "https://placehold.co/600x400"
        },
        {
            "title": "Task Management App",
            "description": "A task management application with real-time collaboration.",
            "image_url": "https://placehold.co/600x400"
        },
        # Add more projects here as needed
    ]

    project_cards = [
        dbc.Col(create_project_card(**project), md=6, lg=4, className="mb-4")
        for project in projects
    ]

    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2(
                                "My Projects",
                                className="text-center mb-5 display-4 font-weight-bold text-primary"
                            ),
                            dbc.Row(
                                project_cards,
                                className="justify-content-center"
                            )
                        ],
                        className="py-5"
                    )
                ],
                className="bg-light py-5"
            )
        ],
        fluid=True
    )
