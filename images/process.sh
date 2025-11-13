#!/usr/bin/env bash

set -exuo pipefail

function ganim() {
 CDATE=$(date +%Y-%m-%d-%H-%M)

 if [ "${2}" == "sat" ]
 then
  python ${2}.py
 elif [ "${2}" == "forecast" ]
 then
  python ${2}.py
 else
  DD=$(date +%H)

  if [ "${2}" == "sun" ] && [ ${DD} -ne 00 ] && [ ${DD} -ne 06 ] && [ ${DD} -ne 12 ] && [ ${DD} -ne 18 ]
  then
   return 0
  fi

  wget -O ${2}_${CDATE}.${3} ${1}

  if [ $(file ${2}_${CDATE}.${3} | grep "ASCII text" | wc -l) -eq 1 ]
  then
   rm -rf ${2}_${CDATE}.${3}
  fi
 fi

 N=15

 if [ $(ls ${2}_*.${3} | wc -l) -gt ${N} ]
 then
  git rm -rf $(ls ${2}_*.${3} | head -n -${N})
  rm -rf $(ls ${2}_*.${3} | head -n -${N})
 fi

 if [ "${2}" == "sat" ] && [ $(ls ${2}2_*.${3} | wc -l) -gt ${N} ]
 then
  git rm -rf $(ls ${2}2_*.${3} | head -n -${N})
  rm -rf $(ls ${2}2_*.${3} | head -n -${N})
 fi

 if [ "${2}" == "sat" ]
 then
  convert -resize 1000x1000 -delay 100 -loop 0 ${2}_*.${3} ${2}.webp
  convert -resize 1000x1000 -delay 100 -loop 0 ${2}2_*.${3} ${2}2.webp
 elif [ "${2}" != "forecast" ]
 then
  convert -resize 1000x1000 -delay 100 -loop 0 ${2}_*.${3} ${2}.webp
 fi
}

ganim https://meteo.org.pl/img/slp.png pressure png
ganim https://meteo.org.pl/img/gt.png temperature png
ganim https://meteo.org.pl/img/sat.jpg sat jpg
ganim https://meteo.org.pl/img/sat.jpg forecast jpg
ganim https://services.swpc.noaa.gov/images/aurora-forecast-northern-hemisphere.jpg aurora jpg
ganim https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIIF.jpg sun jpg

exit 0
