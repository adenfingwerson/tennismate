import re

with open('index.html', 'r') as f:
    html = f.read()

# Add a media query to shrink modal padding on small screens to prevent clipping
media_query = """
        @media (max-width: 600px) {
            .modal-content { padding: 32px 24px; }
            .radio-option { padding: 12px; }
            .btn-modal { padding: 12px; font-size: 0.9rem; }
            .modal-title { font-size: 1.5rem; }
        }
    </style>
"""

html = html.replace('</style>', media_query)

with open('index.html', 'w') as f:
    f.write(html)

print("Mobile responsive fix applied.")
