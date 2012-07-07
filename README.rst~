========================
What is markuptotexttag?
========================

	This module, written for pygtk, converts valid pango markup strings into
	GtkTextTags which allow GtkTextViews to display the same formatted text as
	you would display in a GtkLabel.

Why?
----

	GtkTextTags can be complicated to use, especially if you're using other widgets
	that use pango markup strings to format text(like GtkLabels or CellRenderers).
	This package provides a simple way to convert those markup strings into
	the GtkTextTags, allowing you to easily apply the same formatting to the
	text if you need to put it in a GtkTextView.


How?
----

	It's easy to use::
	
		from markuptotexttag import convertMarkup
		
		markup_string = '<span foreground="blue">Test string</span>'
		textview = gtk.TextView() #Create a TextView
		props = convertMarkup(markup_string) #Convert the markup string into MarkupProps
		buff = textview.get_buffer() #Get the textview's buffer
		buff.set_text(props.text) #Set the buffer's text
		tag_table = buff.get_tag_table() #Get the buffer's tag table
		
		#Assign texttags
		for tag, start, end in props:
			tag_table.add(tag)
			start_iter = buff.get_iter_at_offset(start)
			end_iter = buff.get_iter_at_offset(end)
			buff.apply_tag(tag, start_iter, end_iter)
			
		
	
