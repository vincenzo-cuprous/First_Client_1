# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_navbar(active_section='home'):
    """Creates the navigation bar component with Font Awesome icons and DaisyUI/Tailwind styling."""
    return dbc.Navbar(
        dbc.Container(
            [
                # Portfolio Brand
                html.A(
                    "My Portfolio",
                    href="/",
                    className="text-xl font-bold text-base-content"  # DaisyUI text color
                ),
                # Navigation Links
                dbc.Nav(
                    [
                        dbc.NavLink(
                            [html.I(className="fas fa-home mr-2"), "Home"],
                            href="/",
                            active=active_section == "home",  # Active state for Home
                            className=f"btn btn-ghost {'btn-active' if active_section == 'home' else ''}"  # DaisyUI active class
                        ),
                        dbc.NavLink(
                            [html.I(className="fas fa-user mr-2"), "About"],
                            href="/about",
                            active=active_section == "about",  # Active state for About
                            className=f"btn btn-ghost {'btn-active' if active_section == 'about' else ''}"  # DaisyUI active class
                        ),
                        dbc.NavLink(
                            [html.I(className="fas fa-tools mr-2"), "Skills"],
                            href="/skills",
                            active=active_section == "skills",  # Active state for Skills
                            className=f"btn btn-ghost {'btn-active' if active_section == 'skills' else ''}"  # DaisyUI active class
                        ),
                        dbc.NavLink(
                            [html.I(className="fas fa-project-diagram mr-2"), "Projects"],
                            href="/projects",
                            active=active_section == "projects",  # Active state for Projects
                            className=f"btn btn-ghost {'btn-active' if active_section == 'projects' else ''}"  # DaisyUI active class
                        ),
                        dbc.NavLink(
                            [html.I(className="fas fa-envelope mr-2"), "Contact"],
                            href="/contact",
                            active=active_section == "contact",  # Active state for Contact
                            className=f"btn btn-ghost {'btn-active' if active_section == 'contact' else ''}"  # DaisyUI active class
                        ),
                        # Theme Toggle Button
                        dbc.Button(
                            html.I(className="fas fa-moon"),
                            id="theme-toggle",
                            className="btn btn-ghost"
                        )
                    ],
                    className="ml-auto flex gap-4",  # Tailwind flex and gap utilities
                    navbar=True
                )
            ],
            fluid=True,
            className="px-4"  # Tailwind padding
        ),
        sticky="top",
        className="bg-base-200 shadow-lg z-50",  # DaisyUI background and shadow
        id="navbar"
    )

def create_footer():
    """Creates the footer component with theme toggle functionality and CDN links."""
    return html.Footer(
        [
            # Tailwind CSS CDN
            html.Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
            ),
            # DaisyUI CDN
            html.Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/daisyui@4.7.2/dist/full.min.css"
            ),
            # Font Awesome CDN
            html.Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
            ),
            # Theme Store (for light/dark mode)
            dcc.Store(id="theme-store", data="light"),
            # JavaScript to apply the theme
            html.Script(
                """
                // Function to apply the theme
                function applyTheme(theme) {
                    const htmlElement = document.documentElement;
                    htmlElement.setAttribute('data-theme', theme);
                }

                // Listen for changes to the theme-store
                dash_clientside.onUpdate('theme-store', function(data) {
                    applyTheme(data.data);
                });

                // Apply the initial theme
                const initialTheme = document.getElementById('theme-store').getAttribute('data');
                applyTheme(initialTheme);
                """
            )
        ]
    )

def serve_page_content(children):
    """Serves the page content with the correct background and layout."""
    return html.Div(
        children,
        className="bg-base-100 min-h-screen",  # DaisyUI background and full height
        id="page-content"
    )

def create_layout(active_section='home', children=None):
    """Creates the full layout with navbar, content, and footer."""
    return html.Div(
        [
            # Navbar
            create_navbar(active_section=active_section),
            # Page Content
            serve_page_content(children),
            # Footer
            create_footer()
        ],
        className="flex flex-col",  # Tailwind flex layout
        id="main-layout"
    )
