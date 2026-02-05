import pandas as pd
import streamlit as st

import streamlit.components.v1 as components

power_bi_embed_code = "https://app.powerbi.com/view?r=eyJrIjoiZjAxNzQzOGUtNWYzZS00MmY1LWEyMGItM2IxMWQzMjE0ZWMyIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9"

components.iframe(power_bi_embed_code, width=1440, height=900)
