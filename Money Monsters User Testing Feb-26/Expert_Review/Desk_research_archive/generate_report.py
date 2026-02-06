import json

# Read the JSON file
with open('/Users/mattspeak/Library/Mobile Documents/iCloud~md~obsidian/Documents/ObsidianMatt/WORK/Mosaic/Money Monsters User Testing Feb-26/Research/Desk_research/Innovators.json', 'r') as f:
    data = json.load(f)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
        .company-card { border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; margin-bottom: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .company-header { display: flex; align-items: center; margin-bottom: 15px; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px; }
        .company-logo { width: 40px; height: 40px; margin-right: 15px; border-radius: 50%; }
        h1 { color: #2c3e50; text-align: center; margin-bottom: 40px; }
        h2 { margin: 0; color: #2c3e50; font-size: 1.5em; }
        .company-url { color: #3498db; text-decoration: none; font-size: 0.9em; display: block; margin-top: 5px; }
        .main-image { max-width: 100%; height: auto; border-radius: 4px; margin: 15px 0; display: block; }
        .summary { background-color: #f9f9f9; padding: 15px; border-left: 4px solid #3498db; border-radius: 4px; }
        .summary h3 { margin-top: 0; color: #2c3e50; }
        .sub-pages { margin-top: 20px; font-size: 0.9em; color: #666; }
    </style>
</head>
<body>
    <h1>Innovators in Financial Literacy</h1>
"""

for result in data.get('results', []):
    title = result.get('title', 'Unknown Company')
    url = result.get('url', '#')
    summary = result.get('summary', 'No summary available.')
    image = result.get('image')
    favicon = result.get('favicon')
    
    formatted_summary = summary.replace('\n', '<br>').replace('### ', '<h4>').replace('**', '<b>')
    
    favicon_html = f'<img src="{favicon}" class="company-logo" onerror="this.style.display=\'none\'">' if favicon else ''
    image_html = f'<img src="{image}" class="main-image" onerror="this.style.display=\'none\'">' if image else ''
    
    html_content += f"""
    <div class="company-card">
        <div class="company-header">
            {favicon_html}
            <div>
                <h2>{title}</h2>
                <a href="{url}" class="company-url" target="_blank">{url}</a>
            </div>
        </div>
        
        {image_html}
        
        <div class="summary">
            {formatted_summary}
        </div>
    </div>
    """

html_content += """
</body>
</html>
"""

with open('/Users/mattspeak/Library/Mobile Documents/iCloud~md~obsidian/Documents/ObsidianMatt/WORK/Mosaic/Money Monsters User Testing Feb-26/Research/Desk_research/innovators_report.html', 'w') as f:
    f.write(html_content)

print("HTML report generated successfully.")
