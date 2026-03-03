#!/usr/bin/env ruby

# Custom 404 handler for Jekyll local development
# This script ensures proper 404 handling in local development

require 'webrick'

module WEBrick
  class HTTPResponse
    def setup_header
      super
      if @status == 404
        # Set content type for 404 page
        self['content-type'] = 'text/html; charset=utf-8'
      end
    end
  end
end