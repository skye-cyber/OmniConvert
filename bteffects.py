    def RoundedButton(self, text, default_color=(0.2, 0.6, 0.8, 1), pressed_color=(0.1, 0.4, 0.6, 1), **kwargs):
        """Create a rounded button with specific properties."""
        btn = Button(
            text=text,
            height=40,  # You can adjust the height
            **kwargs
        )

        # Set transparent background to remove default white
        btn.background_normal = ''  # No background image
        btn.background_color = (0, 0, 0, 0)  # Fully transparent background

        with btn.canvas.before:
            # Initial color and rounded rectangle background
            btn.color_instruction = Color(*default_color)
            btn.rect = RoundedRectangle(
                size=btn.size,
                pos=btn.pos,
                radius=[20]  # Radius for rounded corners
            )

        # Bind position and size updates to redraw the button
        btn.bind(pos=self.btn_update_rect, size=self.btn_update_rect)

        # Bind touch down (click) and release events
        btn.bind(on_press=lambda instance: self.on_press_callback(instance, pressed_color))
        btn.bind(on_release=lambda instance: self.on_release_callback(instance, default_color))

        return btn

    def btn_update_rect(self, instance, *args):
        """Update the button's rectangle position and size."""
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def on_press_callback(self, instance, pressed_color):
        """Change color and size animation when button is pressed."""
        instance.color_instruction.rgba = pressed_color
        # Animate the size increase by 2%
        anim = Animation(size=(instance.size[0] * 1.1, instance.size[1] * 1.1), duration=0.1)
        anim += Animation(size=instance.size, duration=0.2)
        anim.start(instance)

    def on_release_callback(self, instance, default_color):
        """Restore color and size animation when button is released."""
        instance.color_instruction.rgba = default_color
        # Animate the size back to normal
        anim = Animation(size=(instance.size[0] / 1.1, instance.size[1] / 1.1), duration=0.1)
        anim += Animation(size=instance.size, duration=0.2)
        anim.start(instance)
