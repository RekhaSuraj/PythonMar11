import pandas as pd

p1 = pd.date_range('20250516',periods=10)
print(p1)

# DatetimeIndex(['2025-05-16', '2025-05-17', '2025-05-18', '2025-05-19',
#                '2025-05-20', '2025-05-21', '2025-05-22', '2025-05-23',
#                '2025-05-24', '2025-05-25'],
#               dtype='datetime64[ns]', freq='D')


# Params:
# start – Left bound for generating dates.
# end – Right bound for generating dates.
# periods – Number of periods to generate.
# freq – Frequency strings can have multiples, e. g. '5h'. See :ref:`here  ` for a list of frequency aliases.
# tz – Time zone name for returning localized DatetimeIndex, for example 'Asia/ Hong_Kong'. By default, the resulting DatetimeIndex is timezone-naive unless timezone-aware datetime-likes are passed.
# normalize – Normalize start/ end dates to midnight before generating date range.
# name – Name of the resulting DatetimeIndex.
# inclusive – Include boundaries; Whether to set each bound as closed or open. .. versionadded:: 1.4.0
# unit – Specify the desired resolution of the result. .. versionadded:: 2.0.0
# kwargs – For compatibility. Has no effect on the result.