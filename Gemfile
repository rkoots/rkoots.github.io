source "https://rubygems.org"

# GitHub Pages gem includes all required dependencies
gem "github-pages", group: :jekyll_plugins

# Windows specific gems
platforms :mingw, :x64_mingw, :mswin do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
  gem "wdm", "~> 0.1.1"
end

# JRuby specific gems
platforms :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
  gem "http_parser.rb", "~> 0.6.0"
end