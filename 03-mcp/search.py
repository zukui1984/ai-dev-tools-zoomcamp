import minsearch
import glob
import os

# Collect all md and mdx files
md_files = glob.glob('fastmcp-main/**/*.md', recursive=True)
mdx_files = glob.glob('fastmcp-main/**/*.mdx', recursive=True)
all_files = md_files + mdx_files

documents = []
for file in all_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove the first part
    filename = file.split('fastmcp-main' + os.sep, 1)[1]
    documents.append({
        'content': content,
        'filename': filename
    })

# Create index
index = minsearch.Index(text_fields=['content'], keyword_fields=['filename'])
index.fit(documents)

def search(query, num_results=5):
    return index.search(query, num_results=num_results)

# Test
if __name__ == "__main__":
    results = search("demo")
    if results:
        print("First file:", results[0]['filename'])
    else:
        print("No results")