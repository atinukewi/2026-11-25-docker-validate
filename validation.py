import pointblank as pb
from palmerpenguins import load_penguins

penguins = load_penguins()
penguins

values = (
    pb.Validate(
        data=penguins,
        label="Penguin measurements",
        thresholds=(0.01, 0.05, 0.10)
    )
    .col_vals_in_set(columns="species", set=["Adelie", "Chinstrap", "Gentoo"])
    .col_vals_between(columns="bill_length_mm", left=30, right=60, na_pass=True)
    .rows_distinct()
    .interrogate()
)