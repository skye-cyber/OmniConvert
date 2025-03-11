
        # Set the system cursor to "wait" (usually a loading spinner)
        Window.set_system_cursor('wait')

        # You can change it back to default once the app is loaded
        Window.set_system_cursor('pointer')  # Reset to normal arrow
         # Create a layout
        layout = BoxLayout()

        # Create and add a spinner (simulating loading)
        spinner = Spinner(text="Loading...", values=("Loading...",))
        layout.add_widget(spinner)

        # Set the window icon (the image should be in the same directory or specify the full path)
        Window.set_icon('/home/skye/Pictures/whatsapp_icon.png')  # Use an image in .png format (ideally a square image like 64x64 or 128x128
        # Change the background color (RGBA format: Red, Green, Blue, Alpha)
        Window.clearcolor = (0.2, 0.6, 0.8, 1)  # Light blue color
