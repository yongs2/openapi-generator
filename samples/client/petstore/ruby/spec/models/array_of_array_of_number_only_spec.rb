=begin
#OpenAPI Petstore

#This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

The version of the OpenAPI document: 1.0.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.0.0-SNAPSHOT

=end

require 'spec_helper'
require 'json'
require 'date'

# Unit tests for Petstore::ArrayOfArrayOfNumberOnly
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'ArrayOfArrayOfNumberOnly' do
  before do
    # run before each test
    @instance = Petstore::ArrayOfArrayOfNumberOnly.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of ArrayOfArrayOfNumberOnly' do
    it 'should create an instance of ArrayOfArrayOfNumberOnly' do
      expect(@instance).to be_instance_of(Petstore::ArrayOfArrayOfNumberOnly)
    end
  end
  describe 'test attribute "array_array_number"' do
    it 'should work' do
      # assertion here. ref: https://rspec.info/features/3-12/rspec-expectations/built-in-matchers/
    end
  end

end
