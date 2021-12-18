import numpy as np
from bokeh.io import  show, output_file
from bokeh.plotting import figure
from bokeh.models.tools import HoverTool


""" 
https://github.com/bokeh/bokeh
https://docs.bokeh.org/en/dev/docs/first_steps.html
 """

output_file('bokeh testing.html')

# create a new plot
p = figure(plot_width=800, plot_height=800, 
        title="multi-graph: have a fun time",
        x_range=(0, 6), y_range=(3, 12),
        tools = [HoverTool()], tooltips = '(@x, @y)'

        )
# add a circle renderer with x and y 
p.circle([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 
        radius=0.1, size=5,  # if you implict radius, then size will be covered
        line_color='navy', fill_color='orange', 
        fill_alpha=0.5, legend_label='circ')

# change existed graph

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
my_line = p.line(x, y, 
                legend_label="temp", line_width=2, 
                line_color='red')
glyph = my_line.glyph # access glyph attribute
glyph.line_color = 'green'

# how to customize legend
p.legend.label_text_font = 'times'
p.legend.label_text_font_size = '20px'
p.legend.label_text_font_style = 'italic'
p.legend.label_text_color = 'navy'

# how to cutomize headline
p.title.text_font_size = '20px'
p.title_location = 'above'
p.title.text_color = 'navy'

# how to use annotations
from bokeh.models import BoxAnnotation

low_box = BoxAnnotation(top=2, fill_alpha=0.3, fill_color='red')
mid_box = BoxAnnotation(bottom=2, top=5, fill_alpha=0.3, fill_color='green')
high_box = BoxAnnotation(bottom=5, fill_alpha=0.1, fill_color='red')
p.add_layout(low_box)
p.add_layout(mid_box)
p.add_layout(high_box)


# how to use theme
from bokeh.io import curdoc
curdoc().theme = 'caliber'

# responsive plot sizing
p.sizing_mode = 'scale_both'
p.sizing_mode = 'stretch_both'

# change axis
p.xaxis.axis_label = 'x'
p.xaxis.axis_line_width = 2
p.yaxis.axis_label = 'y'
p.yaxis.major_label_text_color = 'orange'
p.yaxis.major_label_orientation = 'horizontal'

# use axis ticks
from bokeh.models import NumeralTickFormatter
p.yaxis[0].formatter = NumeralTickFormatter(format='$0.00')

# enabling logrithmic axes
""" y_axis_type = 'log' """

# enable datetime axes
# from bokeh.models import DatetimeTickFormatter
# dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)]
# p.x_axis_type = 'datetime'
# p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# customize grid
p.xgrid.grid_line_color = 'navy'
p.ygrid.grid_line_dash = [6, 4]

# use bands and bounds
p.ygrid.band_fill_color = 'olive'
p.ygrid.band_fill_alpha = 0.1

# customize toolbar
p.toolbar.autohide = True

# tooltips
# from bokeh.models.tools import HoverTool
# # p.tools = [HoverTool()]
# # p.tooltips = '(@x, @y)'

show(p)