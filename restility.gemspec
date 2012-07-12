Gem::Specification.new do |s|
  s.name = "restility"
  s.version = '0.0.4'
  s.date = Time.now.strftime('%F')
  s.summary = "Set of tools for writing REST style web services."
  s.homepage = "https://github.com/openSUSE/restility"
  s.email = "cschum@suse.de"
  s.authors = ["Cornelius Schumacher"]

  s.files = %w( License.txt )
  s.files += Dir.glob("config/**/*")
  s.files += Dir.glob("lib/**/*")
  s.files += Dir.glob("script/**/*")
  s.files += Dir.glob("tasks/**/*")
  s.files += Dir.glob("test/**/*")

  s.executables = %w( rest_doc rest_test )
  s.description = "Generates REST documentation in Docbook and HTML format."

end