from tkinter import Tk, Frame, Canvas, BOTH, Radiobutton
import math

def main():
    width = 800
    height = 500

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title("Scene")
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    # Night and day radiobutton.
    # wrapper = Radiobutton()
    # 
    # position = wrapper.anchor
    # ####

    # switch = tk.Radiobutton(Canvas, anchor = tk.SW)

    root.mainloop()

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters:
        scene_left - left side of the region; less than scene_right
        scene_top - top of the region; less than scene_bottom
        scene_right - right side of the region
        scene_bottom - bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    ## tree_left = scene_left + 500
    ## tree_top = scene_top + 100
    ## tree_height = 150
    ## draw_pine_tree(canvas, tree_left, tree_top, tree_height)  

    sky_left = 0
    sky_top = 0
    sky_right = 799
    sky_bottom = 350
    draw_sky(canvas, sky_left, sky_top, sky_right, sky_bottom,)

    # draw_hills(canvas, scene_left, scene_top, scene_right, scene_bottom)

    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom)
    
    draw_sun(canvas, -25, -25, scale=2.5) # ray_count=4
    
    clouds_left = 150 + 75
    clouds_top = 50
    clouds_right = 250 + 75
    clouds_bottom = 150
    draw_clouds(canvas, clouds_left, clouds_top, clouds_right, clouds_bottom)
    clouds_left = 350 + 50
    clouds_top = 50
    clouds_right = 450 + 50
    clouds_bottom = 150
    draw_clouds(canvas, clouds_left, clouds_top, clouds_right, clouds_bottom)
    clouds_left = 550 + 25
    clouds_top = 50
    clouds_right = 650 + 25
    clouds_bottom = 150
    draw_clouds(canvas, clouds_left, clouds_top, clouds_right, clouds_bottom)
    clouds_left = 799 - 49
    clouds_top = 50
    clouds_right = 799 +51
    clouds_bottom = 150
    draw_clouds(canvas, clouds_left, clouds_top, clouds_right, clouds_bottom)

    draw_ghost_tree(canvas, 495 - 35, 200, "#db0000")
    draw_ghost_tree(canvas, 590 - 35, 200, "#cf51cd")
    draw_ghost_tree(canvas, 685 - 35, 200, "#00b8cb")
    draw_ghost_tree(canvas, 780 - 35, 200, "#be6620")
    
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 50) # 100 is how far apart  ## Take out this line to omit the grid.
    '''
    draw_sun(canvas, 200, 200, ray_count=4)
    draw_sun(canvas, 300, 400, scale=.5) # With objects based on parameters and constants we make another identical sun wherever we want!
    draw_sun(canvas, 500, 50, scale=3, ray_count = 20) # Position determined by top left corner. ## We can also adjust it's size with the scale function.
    '''

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_ghost_tree(canvas, scene_left, scene_top, body_color, eye_color = "#e3e4e5", pupil_color = "#0061ca"):
    diameter = 75 # width and height
    # trunk_width = 20
    trunk_length = (diameter * 1.7)
    # skirt_thickness = 15
    
    circle_right = scene_left + (diameter) -1 # Top right corner
    circle_bottom = scene_top + (diameter) # Bottom right corner   # For the ghost-tree top
    
    rectangle_right = scene_left + (diameter) # Top right corner
    rectangle_bottom = scene_top + (diameter) # Bottom right corner
    
    second_point_x = scene_left + (diameter * (1/6))
    second_point_y = scene_top + (diameter * (8/10))
    third_point_x = scene_left +(diameter * (2/6))
    third_point_y = scene_top +  (diameter) + 1
    fourth_x = scene_left + (diameter * (3/6))
    fourth_y = scene_top + (diameter * (8/10))
    fifth_x = scene_left + (diameter * (4/6))
    fifth_y = scene_top + (diameter) + 1
    sixth_x = scene_left + (diameter * (5/6))
    sixth_y = scene_top + (diameter * (8/10))
    seventh_x = scene_left + (diameter * (6/6))
    seventh_y = scene_top + (diameter) - 1
    eighth_x = scene_left             #SAME AS FIRST
    eighth_y = scene_top + diameter   #SAME AS FIRST
    ### NOPE JUST 8 POINTS (aka 4 skirt-tips) ###

    left_eye_right = scene_left + (diameter) 
    left_eye_bottom = scene_top + (diameter)
    
    left_pupil_right = scene_left + (diameter) - (diameter * (83/128))
    left_pupil_bottom = scene_top + (diameter) - (diameter * (1/2)) + 3

    right_eye_right = scene_left + (diameter)
    right_eye_bottom = scene_top + (diameter)

    right_pupil_right = scene_left + (diameter) - (diameter * (29/100))
    right_pupil_bottom = scene_top + (diameter) - (diameter * (1/2)) + 3

    canvas.create_rectangle(scene_left, scene_top + (diameter/2), rectangle_right, rectangle_bottom, fill=body_color, width=False) # For the ghost-tree bottom

    canvas.create_rectangle(third_point_x, scene_top + (diameter/2), fifth_x, rectangle_bottom - (diameter/2) + trunk_length, fill="#68352c", width=False) # Tree Trunk
    
    canvas.create_oval(scene_left, scene_top, circle_right, circle_bottom, fill=body_color, width=False) # Treetop

    canvas.create_polygon(scene_left, scene_top + diameter, second_point_x, second_point_y, third_point_x, third_point_y, fourth_x, fourth_y, fifth_x, fifth_y, sixth_x, sixth_y, seventh_x, seventh_y, eighth_x, eighth_y, fill="#101010", width=False) # Tree skirt cutout

    canvas.create_polygon(third_point_x, third_point_y, fourth_x, fourth_y, fifth_x, fifth_y, third_point_x, third_point_y, fill="#68352c", width=False) # Tree skirt trunk fill-in



    canvas.create_oval(scene_left + (diameter * (1/5)), scene_top + (diameter * (1/3)), left_eye_right - (diameter * (9/16)), left_eye_bottom - (diameter * (1/3)), fill=eye_color) # left eye (white = default)
    canvas.create_oval(scene_left + (diameter * (9/16)), scene_top + (diameter * (1/3)), right_eye_right - (diameter * (1/5)), right_eye_bottom - (diameter * (1/3)), fill=eye_color) # right eye (white = default)
    
    canvas.create_oval(scene_left + (diameter * (1/5)), scene_top + (diameter * (1/3)) + 3, left_pupil_right,  left_pupil_bottom, fill = pupil_color) # Left eye pupil (blue = default)
    canvas.create_oval(scene_left + (diameter * (9/16)), scene_top + (diameter * (1/3)) + 3, right_pupil_right, right_pupil_bottom, fill = pupil_color) # Right eye pupil (blue = default)
   
def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters:
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    ## canvas.create_rectangle(trunk_left, skirt_bottom,
    ##         trunk_right, trunk_bottom,
    ##         outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

def draw_grid(canvas, left, top, right, bottom, grid_spacing):

    text_horizontal_margin = 22  ## This gives space from the edge to read the text # adjusts from the middle of the text.
    text_vertical_margin = 10    # This is a metric. 
    # line_frequency = 50
    print_text_frequency = 100

    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):    ## These for loops are our drawing code. Ideally, they would have no numbers in them.
        # canvas.create_line(0, 100, 799, 100)  ## (x1, y1, x2, y2)
        canvas.create_line(left, i, right, i)
        # if i % print_text_frequency == 0:
        #     canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")

    # Draw vertical lines         
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        # if i % print_text_frequency == 0:
        #     canvas.create_text(i, top + text_vertical_margin, text=f"{i}")
    
    # Draw the grid-point numbers according to print_text_frequency
    for y in range(top, bottom, grid_spacing):
        for x in range(left, right, grid_spacing):
            if y % print_text_frequency == 0 and x % print_text_frequency == 0:
                canvas.create_text(x + text_horizontal_margin, y + text_vertical_margin, text=f"{x}, {y}")

def draw_sky(canvas, sky_left, sky_top, sky_right, sky_bottom):
    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom, fill="#101010", width=False) 
    
def draw_ground(canvas, scene_left, scene_top, width, height):
    scene_right = scene_left + width
    scene_bottom = scene_top + height
    scene_left = 0
    scene_top = 350
    # scene_right = 799
    # scene_bottom = 499
    canvas.create_rectangle(scene_left, scene_top, scene_right, scene_bottom, fill="#006400", width=False)

def draw_clouds(canvas, clouds_left, clouds_top, clouds_right, clouds_bottom):
    canvas.create_oval(clouds_left, clouds_top, clouds_right, clouds_bottom, fill="#DCDCDC", width=False)

def draw_sun(canvas, sun_left, sun_top, scale=1, ray_count = 10):  # We set a default value to start from.
    # In functions, put metrics at the top and then drawing code afterwards.
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_length = 100 * scale
    ray_width = 3 * scale
    ## If we put ray_count up in the parameter on line 51 and give it to the suns on lines 46—48 then we can have a variable amount of rays on the sun.

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height /2)

    top_point_x = 150 + 75 - 10 + 14 # ref. first clouds_left
    top_point_y = 50 - 6 # ref. first clouds_top ## rise over run
    bottom_point_x = 150 + 75 - 10 + 14 ## MONEY!! B^)
    bottom_point_y = 150 + 6 # ref. first clouds_bottom

    # canvas.create_oval(x,y, x + 100, y + 100, fill="fff794", width=False) # This is the wrong way to do this. 
    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="#e9e800", width=False) 
    
    # This is the sun body.
    ## Setting width=False or 0 or None gets rid of the border.
    # canvas.create_line(sun_center_x, sun_center_y, sun_center_x, sun_center_x - 100, width=3, fill="#ff0000") # This is the ray of sunshine.
    for i in range(ray_count):
        # Trigonometry
        # angle = (360 / ray_count) * i  ## Wrong way to do this. Python doesn't understand degrees, only radians.
        angle = (2 * math.pi / ray_count) * i   ## This is the correct way.  What's a radian?
        ray_x = sun_center_x + math.cos(angle) * ray_length  ## What does cosine do?
        ray_y = sun_center_y + math.sin(angle) * ray_length  ## What does sine do?
        # canvas.create_line(sun_center_x, sun_center_y, sun_center_x, sun_center_x - ray_length, width=ray_width, fill="#ff0000") # This is the ray of sunshine. # Correct way to do this.
        #### canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill="#ff0000") # Even better way to do this. ### What just happened here?
    ''' This is the pie cut out. '''
    canvas.create_polygon(sun_center_x, sun_center_y, top_point_x, top_point_y, bottom_point_x, bottom_point_y, sun_center_x, sun_center_y, fill="#101010", width=False)

# def draw_hills(canvas, arc_left, arc_top, arc_right, arc_bottom):
#     arc_left = -100
#     arc_top = 300
#     arc_right = 400
#     arc_bottom = 400
#     canvas.create_arc(arc_left, arc_top, arc_right, arc_bottom, fill="#006400")

# Call the main function so that
# this program will start executing.
main()











