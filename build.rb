require 'yaml'
require 'open-uri'
require 'date'

ARTIFACTS_URL = 'https://raw.githubusercontent.com/Bhupesh-V/Bhupesh-V.github.io/refs/heads/master/_data/artifacts.yml'
BASE_DOMAIN   = 'https://bhupesh.me'

FOOTER = <<~FOOTER


  ### Hire

  - [Know how we can collaborate professionally](https://bhupesh.me/hire)
FOOTER

def fetch_artifacts
  yaml_content = URI.open(ARTIFACTS_URL, 'User-Agent' => 'Mozilla/5.0').read
  data = YAML.safe_load(yaml_content, permitted_classes: [Date]) || []

  # Sort by date descending (most recent first)
  # Handles missing dates gracefully by placing them at the end
  sorted_data = data.sort_by do |item|
    d = item['date'].to_s
    d.empty? ? '0000-00' : d
  end.reverse

  sorted_data.first(10).map do |item|
    title    = item['title'] || 'Untitled'
    url      = item['url'].to_s
    art_type = item['type'] || 'general'

    unless url.start_with?('http://', 'https://')
      url = "#{BASE_DOMAIN}#{url.start_with?('/') ? '' : '/'}#{url}"
    end

    { title: title, url: url, type: art_type.downcase }
  end
end

def main
  artifacts = fetch_artifacts

  File.open('README.md', 'w') do |file|
    file.puts "<details open>\n  <summary>Recent Artifacts</summary>\n  <br>\n  <ul>"
    
    artifacts.each do |a|
      # Modern layout: clean link text with an inline code badge on the right
      file.puts "    <li><a href=\"#{a[:url]}\"><b>#{a[:title]}</b></a> <code>#{a[:type]}</code></li>"
    end
    
    file.puts "  </ul>\n</details>"
    file.puts FOOTER
  end

  puts "README.md updated successfully with 10 most recent artifacts."
end

main
