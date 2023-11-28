curl "https://www2.census.gov/programs-surveys/cps/datasets/2023/march/asecpub23csv.zip" -o asecpub23csv.zip

mkdir -p data
mv asecpub23csv.zip data/
cd data
unzip asecpub23csv.zip
rm asecpub23csv.zip
