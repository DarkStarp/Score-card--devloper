import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import(VerticalBarChart)
from reportlab.graphics.charts.piecharts import(Pie)
from reportlab.graphics.shapes import String
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.colors import Color, PCMYKColor
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.colors import black, red, purple, green, maroon, brown, pink, white, HexColor
from reportlab.lib.validators import Auto