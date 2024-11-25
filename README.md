# Selenium News Scraping and Topic Modeling with Transformers

<h2>Overview</h2>
<p>This repository contains a Python-based pipeline for collecting news stories by country using NewsAPI, extracting full articles using Selenium and ChromeDriver, and performing topic modeling using Hugging Face's Transformers.</p>
<h2>Requirements</h2>
<ul>
<li>Python 3.8+</li>
<li>NewsAPI key</li>
<li>ChromeDriver</li>
<li>Hugging Face Transformers library</li>
</ul>
<h2>Pipeline Steps</h2>
<h3>Step 1: News Story Collection using NewsAPI</h3>
<p>Use the <code>requests</code> library to send a GET request to NewsAPI with the desired country parameter.</p>
<p>Parse the JSON response and extract the article links.</p>
<h3>Step 2: Full Article Extraction using Selenium and ChromeDriver</h3>
<p>Use Selenium to navigate to each article link and extract the full article text.</p>
<p>Utilize ChromeDriver for headless browsing.</p>
<h3>Step 3: Topic Modeling using Hugging Face Transformers</h3>
<p>Preprocess the extracted article text using Hugging Face's Transformers library.</p>
<p>Utilize a pre-trained transformer model (e.g., BERT, DistilBERT) to generate topic embeddings.</p>
<p>Calculate topic scores using a suitable algorithm (e.g., k-means clustering).</p>
<h2>Usage</h2>
<ol>
<li>Clone this repository: <code>git clone --this repo--- </code></li>
<li>Install required libraries: <code>pip install -r requirements.txt</code></li>
<li>Set environment variables for NewsAPI key and ChromeDriver path.</li>
</ol>
<h2>Contributing</h2>
<p>Contributions are welcome! Please submit a pull request with a clear description of your changes.</p>
<h2>License</h2>
<p>This repository is licensed under the MIT License.</p>
