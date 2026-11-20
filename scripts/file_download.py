from pathlib import Path
import urllib.request
import zipfile
import pandas as pd


class DatasetLoader:

    def __init__(self, url, arquivos, data_dir="data", zip_name="occupancy_data.zip"):
        self.url = url
        self.arquivos = arquivos
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.zip_name = zip_name

        self.raw_dir.mkdir(parents=True, exist_ok=True)

    def csv_path(self, arquivo):
        return self.data_dir / (Path(arquivo).stem + ".csv")

    def download(self):
        zip_path = self.data_dir / self.zip_name

        urllib.request.urlretrieve(self.url, zip_path)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(self.raw_dir)

        zip_path.unlink()

    def preparar(self):
        # baixa o zip só se algum arquivo ainda não estiver na pasta
        faltando = [
            a for a in self.arquivos
            if not self.csv_path(a).exists() and not (self.raw_dir / a).exists()
        ]

        if faltando:
            print(f"Baixando arquivos: {faltando}")
            self.download()

        for arquivo in self.arquivos:
            destino = self.csv_path(arquivo)

            if destino.exists():
                print(f"Arquivo encontrado: {destino}")
                continue

            df_temp = pd.read_csv(self.raw_dir / arquivo)
            df_temp.to_csv(destino, index=False)
            print(f"Arquivo criado: {destino}")

    def load_dataframes(self):
        self.preparar()

        return {
            Path(a).stem: pd.read_csv(self.csv_path(a))
            for a in self.arquivos
        }


loader = DatasetLoader(
    url="https://archive.ics.uci.edu/ml/machine-learning-databases/00357/occupancy_data.zip",
    arquivos=["datatraining.txt", "datatest.txt", "datatest2.txt"]
)

dfs = loader.load_dataframes()
df = dfs["datatest"]