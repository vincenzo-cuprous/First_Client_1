from dash import html
import dash_bootstrap_components as dbc

def serve_skills():
    """
    Returns a redesigned skills page with modern styling and improved visual hierarchy.
    """
    return html.Div([
        # Hero Section
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H1(
                            "Technical Skills",
                            className="text-5xl font-bold mb-6 text-center"
                        ),
                        html.P(
                            "Expertise across the full development stack",
                            className="text-xl text-base-content/80 text-center mb-12"
                        )
                    ], className="text-center")
                ])
            ], fluid=True),
            className="pt-20 pb-12 bg-gradient-to-b from-base-200 to-base-100"
        ),

        # Main Skills Section
        html.Section(
            dbc.Container([
                # Frontend Skills
                dbc.Row([
                    dbc.Col([
                        create_skill_section(
                            "Frontend Development",
                            "Building responsive and interactive user interfaces",
                            "fas fa-code",
                            "primary",
                            [
                                ("HTML/CSS/JavaScript", 90, "Proficient in modern web standards"),
                                ("React & Modern JS", 85, "Component-based architecture"),
                                ("Tailwind CSS", 88, "Utility-first styling"),
                                ("Python & Dash", 82, "Data-driven interfaces"),
                                ("WebAssembly (Go)", 75, "Performance optimization"),
                                ("Rust & Yew", 70, "Type-safe frontend")
                            ]
                        )
                    ], lg=4, className="mb-8"),

                    # Backend Skills
                    dbc.Col([
                        create_skill_section(
                            "Backend Development",
                            "Creating robust and scalable server solutions",
                            "fas fa-server",
                            "secondary",
                            [
                                ("Node.js & Express", 88, "RESTful API development"),
                                ("Python & Flask", 85, "Microservices architecture"),
                                ("Go & Gin", 80, "High-performance backends"),
                                ("Rust & Actix", 75, "System programming"),
                                ("REST API Design", 90, "API architecture"),
                                ("Database Design", 85, "Data modeling")
                            ]
                        )
                    ], lg=4, className="mb-8"),

                    # DevOps Skills
                    dbc.Col([
                        create_skill_section(
                            "DevOps & Cloud",
                            "Implementing modern deployment solutions",
                            "fas fa-cloud",
                            "accent",
                            [
                                ("Docker", 90, "Containerization"),
                                ("Kubernetes", 82, "Container orchestration"),
                                ("AWS Services", 85, "Cloud infrastructure"),
                                ("CI/CD Pipelines", 88, "Automated deployment"),
                                ("Infrastructure as Code", 80, "Terraform"),
                                ("Monitoring & Logging", 85, "System observability")
                            ]
                        )
                    ], lg=4, className="mb-8")
                ], className="mb-12"),

                # Tools & Technologies Grid
                dbc.Row([
                    dbc.Col([
                        html.H2("Tools & Technologies", className="text-3xl font-bold mb-8 text-center"),
                        html.Div([
                            create_tool_card("VS Code", "fas fa-code"),
                            create_tool_card("Git", "fab fa-git-alt"),
                            create_tool_card("Docker", "fab fa-docker"),
                            create_tool_card("AWS", "fab fa-aws"),
                            create_tool_card("Linux", "fab fa-linux"),
                            create_tool_card("Node.js", "fab fa-node-js"),
                            create_tool_card("Python", "fab fa-python"),
                            create_tool_card("React", "fab fa-react")
                        ], className="grid grid-cols-2 md:grid-cols-4 gap-4")
                    ])
                ])
            ], fluid=True, className="max-w-7xl"),
            className="py-12"
        ),

        # Call to Action
        html.Section(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.H2(
                            "Want to see these skills in action?",
                            className="text-3xl font-bold mb-4 text-center"
                        ),
                        html.P(
                            "Check out my projects or get in touch to discuss your next project.",
                            className="text-xl text-base-content/80 mb-6 text-center"
                        ),
                        html.Div([
                            dbc.Button(
                                [html.I(className="fas fa-laptop-code mr-2"), "View Projects"],
                                href="/projects",
                                className="btn btn-primary mr-4 hover:scale-105 transition-transform"
                            ),
                            dbc.Button(
                                [html.I(className="fas fa-envelope mr-2"), "Contact Me"],
                                href="/contact",
                                className="btn btn-outline hover:scale-105 transition-transform"
                            )
                        ], className="flex justify-center gap-4")
                    ], md=8, className="mx-auto")
                ])
            ], fluid=True),
            className="py-20 bg-base-200"
        )
    ])

def create_skill_section(title, description, icon, color, skills):
    """Helper function to create a skill section with progress bars."""
    return html.Div([
        html.Div([
            html.I(className=f"{icon} text-2xl text-{color} mr-3"),
            html.H2(title, className="text-2xl font-bold")
        ], className="flex items-center mb-4"),
        html.P(description, className="text-base-content/70 mb-6"),
        html.Div([
            create_skill_bar(name, percentage, detail, color) for name, percentage, detail in skills
        ], className="space-y-4")
    ], className="bg-base-100 p-8 rounded-2xl shadow-lg h-full")

def create_skill_bar(name, percentage, detail, color):
    """Helper function to create a skill bar with details."""
    return html.Div([
        html.Div([
            html.Span(name, className="font-medium"),
            html.Span(f"{percentage}%", className=f"text-{color}")
        ], className="flex justify-between mb-2"),
        html.Div([
            html.Div(
                className=f"h-2 bg-{color} rounded-full",
                style={"width": f"{percentage}%"}
            )
        ], className="w-full bg-base-200 rounded-full"),
        html.P(detail, className="text-sm text-base-content/60 mt-1")
    ])

def create_tool_card(name, icon):
    """Helper function to create a tool card."""
    return html.Div([
        html.I(className=f"{icon} text-2xl mb-2"),
        html.Div(name, className="font-medium")
    ], className="bg-base-200 p-4 rounded-xl text-center hover:scale-105 transition-transform")
