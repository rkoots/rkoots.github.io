source "https://rubygems.org"

# Basic Jekyll and plugins for local development
gem "jekyll", "~> 4.3"
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

# Windows and JRuby specific gems
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# JRuby specific gems
platforms :jruby do
  gem "http_parser.rb", "~> 0.6.0"
end