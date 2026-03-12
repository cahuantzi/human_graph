import svgwrite

class SVGCreator:

    def create_circle_svg(filename, center_x, center_y, radius, color):
    # The size is set to ensure the whole circle is visible.
        dwg = svgwrite.Drawing(filename, size=(f'{center_x + radius + 10}px', f'{center_y + radius + 10}px'))

        # Add the circle element to the drawing
        # cx and cy define the center coordinates, r defines the radius
        circle = dwg.circle(center=(center_x, center_y), r=radius, fill=color)
        dwg.add(circle)

        # Save the SVG file
        dwg.save()

        print(f"Successfully created {filename}")