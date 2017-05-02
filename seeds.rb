# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'csv'

csv_text = File.read(Rails.root.join('lib', 'seeds', 'fileTable.csv'))
csv = CSV.parse(csv_text, :headers => true, :col_sep => '|', :encoding => 'UTF-8')
csv.each do |row|
	t = Image.new
	t.state = row['state']
	t.root_file = row['root_file']
	t.file_paths = row['file_paths']
	t.text = row['text']
	t.save
	puts "#{t.root_file} saved"
end

puts "There are now #{Image.count} rows in the image data table"