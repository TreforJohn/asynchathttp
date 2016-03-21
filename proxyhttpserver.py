"""
Initial version of the proxy server which is just the cut and paste of the original
asynchat http server.

to do:
-- change the name of this core class to be more appropriate;
-- add the asynchat handlers for the forwarded and return http requests and responses.
-- reduce the list of imported modules to only those that are needed.
"""

import asynchat, asyncore, socket, select, urllib
import posixpath, sys, cgi, cStringIO, os, traceback, shutil
import mimetools, time
import cgi
import mimetypes
import asynchathttpserver
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

__version__ = "0.1"

class ToyHttpServer(asyncore.dispatcher):
	
	def __init__ (self, ip='', port=8081, webroot=os.getcwd(), handler=RequestHandler, pathhandlers={}):
		
		self.webroot=webroot
		self.path_handlers = pathhandlers
		self.handler = handler
		asyncore.dispatcher.__init__ (self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)

		self.set_reuse_addr()
		self.bind ((ip, port))
		self.listen (100)

		print "[httpd] ToyHTTPServer running on port %s, serving from %s" % (port, self.webroot)

	def handle_accept (self):
		try:
			pair = self.accept()
			if pair is not None:
				sock, addr = pair
				self.handler(sock,addr,webroot=self.webroot, path_handlers=self.path_handlers)
		except socket.error:
			self.log_info ('[https] warning: server accept() threw an exception', 'warning')
			return

if __name__=="__main__":
	
	def about(query_string=''):
		f = StringIO()
		f.write("hi %s" % query_string)
		return (f,'text/plain')

	# launch the server on the specified port
	s = ToyHttpServer(port=8081, pathhandlers={'/about': about})

	try:
		while True:
			asyncore.loop(timeout=2, count=10)
			print '[control] poll'
	except KeyboardInterrupt:
		print "Crtl+C pressed. Shutting down."
