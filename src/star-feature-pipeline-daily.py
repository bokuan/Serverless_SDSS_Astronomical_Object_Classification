import os
import modal

LOCAL = False

if LOCAL == False:
   stub = modal.Stub("iris_daily")
   image = modal.Image.debian_slim().pip_install(["hopsworks"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("HOPSWORKS_API_KEY"))
   def f():
       g()


def get_random_star():
    import pandas as pd
    import random
    file_path = "https://raw.githubusercontent.com/bokuan/ID2223/main/res/star_classification.csv"


    header_df = pd.read_csv(file_path, nrows=0)
    total_rows = 100001
    start_row = random.randint(20002, total_rows - 100)

    star_df = pd.read_csv(file_path, skiprows=range(0, start_row), nrows=100, names=header_df.columns)
    star_df = star_df[['u', 'g', 'r', 'i', 'z','class', 'redshift']]
    star_df.rename(columns={'class': 'type'}, inplace=True)
    star_df['type'], star_df['redshift'] = star_df['redshift'].copy(), star_df['type'].copy()
    star_df.columns = star_df.columns.to_series().replace({'type': 'redshift', 'redshift': 'type'}).tolist()
    print(star_df)

    return star_df


def g():
    import hopsworks
    import pandas as pd

    # project = hopsworks.login()
    # fs = project.get_feature_store()
    project = hopsworks.login(project="ID2223_23_lab1")
    fs = project.get_feature_store()

    star_df = get_random_star()

    star_fg = fs.get_feature_group(name="star",version=1)

    star_fg.insert(star_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        # modal.runner.deploy_stub(stub)
        with stub.run():
            f.remote()
