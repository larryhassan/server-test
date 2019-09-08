imple search / replace
editor.replace("old", "new")

# Regular expressions search and replace
editor.rereplace(r"^([A-Z]{3,5})--\1", r"CODE: \1")

# Call a Scintilla function
editor.appendText("Changed codes\r\n");

# Save the file
newFilename = notepad.getCurrentFilename() + ".changed"
notepad.saveAs(newFilename);

# Write to the console window
console.write("Saved as %s\n" % newFilename)

# Create a new document
notepad.new()

# Run a command on the file, and output results to the new file
console.run('compiler.exe "%s"' % newFilename, editor)
