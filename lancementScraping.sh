
cd /home/pi/palleon_genius_scrapingProducers/

gap=50

echo "Valeur depart: `cat /home/pi/palleon_genius_scrapingProducers/IDProducteurCourant.txt`"

DOSSIER="/home/pi/output/palleon_genius_scrapingProducers/"
SOUSDOSSIER="$(date '+%Y-%m')/"
FORMAT=".json"
FICHIER=$(date '+%Y-%m-%d%H_%M_%S')
filename="$DOSSIER$SOUSDOSSIER$FICHIER$FORMAT"

# Run scraper on specific range
/usr/local/bin/scrapy crawl genius -o $filename -a gap=$gap --nolog

value=$((`cat /home/pi/palleon_genius_scrapingProducers/IDProducteurCourant.txt` + gap))
echo "Valeur arrivee: $value"

echo "$value" > /home/pi/palleon_genius_scrapingProducers/IDProducteurCourant.txt
