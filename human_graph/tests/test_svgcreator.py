import dashboard.figures.svg_creator as svg_creator


def test_create_circle_svg():
    filename = "test_circle.svg"
    center_x = 50
    center_y = 50
    radius = 40
    color = "red"

    svg_creator.SVGCreator.create_circle_svg(filename, center_x, center_y, radius, color)

    # Check if the file was created successfully
    import os
    assert os.path.exists(filename), "SVG file was not created."

    # Clean up the created file after the test
    #os.remove(filename)