# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 01:02:18 2020

@author: madpa
"""

import glassdoor_scrapper as gs
import  pandas as pd

ds_job_data_df = gs.get_jobs('data scientist', 10, False)