#!/usr/bin/env python3
import os
import re

# SVG content for each icon
email_svg = '''<svg class="contact-icon" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
                        <path d="M1920 428.266v1189.54l-464.16-580.146-88.203 70.585 468.679 585.904H83.684l468.679-585.904-88.202-70.585L0 1617.805V428.265l959.944 832.441L1920 428.266ZM1919.932 226v52.627l-959.943 832.44L.045 278.628V226h1919.887Z" fill-rule="evenodd"/>
                    </svg>'''

linkedin_svg = '''<svg class="contact-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>'''

github_svg = '''<svg class="contact-icon" viewBox="0 0 98 96" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"/>
                    </svg>'''

x_svg = '''<svg class="contact-icon" viewBox="0 0 1200 1227" xmlns="http://www.w3.org/2000/svg">
                        <path d="M714.163 519.284L1160.89 0H1055.03L667.137 450.887L357.328 0H0L468.492 681.821L0 1226.37H105.866L515.491 750.218L842.672 1226.37H1200L714.137 519.284H714.163ZM569.165 687.828L521.697 619.934L144.011 79.6944H306.615L611.412 515.685L658.88 583.579L1055.08 1150.3H892.476L569.165 687.854V687.828Z"/>
                    </svg>'''

spotify_svg = '''<svg class="contact-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
                    </svg>'''

def update_html_file(file_path):
    """Update a single HTML file to use SVG contact icons"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains contact-image divs
        if '<div class="contact-image email"></div>' in content:
            print(f"Updating {file_path}")
            
            # Replace email icon
            content = content.replace('<div class="contact-image email"></div>', email_svg)
            
            # Replace LinkedIn icon
            content = content.replace('<div class="contact-image linkedin"></div>', linkedin_svg)
            
            # Replace GitHub icon
            content = content.replace('<div class="contact-image github"></div>', github_svg)
            
            # Replace Spotify icon
            content = content.replace('<div class="contact-image spotify"></div>', spotify_svg)
            
            # Add X icon after GitHub and before Spotify
            # Find the pattern: GitHub icon followed by Spotify icon
            github_spotify_pattern = github_svg + '\n                </a>\n                <a href="https://open.spotify.com/user/uniponpeg?si=3d2258ef77b74a61" target="_blank">\n                    ' + spotify_svg
            
            x_github_spotify_pattern = github_svg + '\n                </a>\n                <a href="https://twitter.com/sophiawliu" target="_blank">\n                    ' + x_svg + '\n                </a>\n                <a href="https://open.spotify.com/user/uniponpeg?si=3d2258ef77b74a61" target="_blank">\n                    ' + spotify_svg
            
            content = content.replace(github_spotify_pattern, x_github_spotify_pattern)
            
            # Write the updated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def find_html_files(directory):
    """Recursively find all HTML files in a directory"""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    # Get all HTML files
    html_files = find_html_files('.')
    
    # Filter out files we've already updated manually
    already_updated = [
        './index.html',
        './work/index.html',
        './blog.phia/index.html',
        './work/soph.ai/index.html'
    ]
    
    files_to_update = [f for f in html_files if f not in already_updated]
    
    print(f"Found {len(files_to_update)} HTML files to update")
    
    updated_count = 0
    for file_path in files_to_update:
        if update_html_file(file_path):
            updated_count += 1
    
    print(f"Successfully updated {updated_count} files")

if __name__ == "__main__":
    main()
