# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'csv'

csv_text = File.read(Rails.root.join('lib', 'seeds', 'icpsrData.csv'))
csv = CSV.parse(csv_text, :headers => true, :col_sep => '|', :encoding => 'UTF-8', :quote_char => ";")
csv.each do |row|
	t = ICPSR.new
	t.name = row['name']
	t.date_execution = row['date_execution']
	t.age = row['age']
	t.race = row['race']
	t.sex = row['sex']
	t.occupation = row['occupation']
	t.crime = row['crime']
	t.execution_method = row['execution_method']
	t.location_execution = row['location_execution']
	t.jurisdiction = row['jurisdiction']
	t.state = row['state']
	t.county_conviction = row['county_conviction']
	t.compensation_case = row['compensation_case']
	t.icpsr_state = row['icpsr_state']
	t.save
	puts "#{t.name} saved"
end

puts "There are now #{ICPSR.count} rows in the icpsr table"