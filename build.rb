require 'yaml'
require 'open-uri'

ARTIFACTS_URL = 'https://raw.githubusercontent.com/Bhupesh-V/Bhupesh-V.github.io/refs/heads/master/_data/artifacts.yml'
BASE_DOMAIN   = 'https://bhupesh'

FOOTER = <<~FOOTER


  ### Hire

  - [Know how we can collaborate professionally](https://bhupesh.me/hire)
FOOTER

def fetch_artifacts
  yaml_content = URI.open(ARTIFACTS_URL, 'User-Agent' => 'Mozilla/5.0').read
  data = YAML.safe_load(yaml_content) || []

  data.first(10).map do |item|
    title    = item['title'] || ''
    url      = item['url'].to_s
    art_type = item['type'] || ''

    # Append domain if link has no domain
    unless url.start_with?('http://', 'https://')
      url = "#{BASE_DOMAIN}#{url.start_with?('/') ? '' : '/'}#{url}"
    end

    { title: title, url: url, type: art_type }
  end
end

def main
  artifacts = fetch_artifacts

  File.open('README.md', 'w') do |file|
    file.puts "<details open>\n  <summary>Recent Artifacts</summary>\n  <ul>"
    artifacts.each do |a|
      file.puts "    <li>[#{a[:type]}] <a href=\"#{a[:url]}\">#{a[:title]}</a></li>"
    end
    file.puts "  </ul>\n</details>"
    file.puts FOOTER
  end

  puts "README.md updated successfully with 10 recent artifacts."
end

main
