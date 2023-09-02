#!/usr/bin/env python
"""
Concatenate data on household characteristics across rounds.
"""
import pandas as pd

x = []
for t in ['2007']:
    df = pd.read_parquet('../'+t+'/_/household_characteristics.parquet')
    df['t'] = t
    regions = pd.read_parquet('../'+t+'/_/household_characteristics.parquet')
    df = pd.merge(left = df, right = regions, how = 'left', left_index = True, right_index = True)
    x.append(df)

concatenated = pd.concat(x)

of = pd.read_parquet('../var/other_features.parquet')

concatenated = concatenated.join(of, on=['j','t'])
concatenated = concatenated.reset_index().set_index(['j','t','m'])
concatenated.columns.name = 'k'

concatenated.to_parquet('../var/household_characteristics.parquet')