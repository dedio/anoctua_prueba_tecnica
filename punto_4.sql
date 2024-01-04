SELECT
    indice_tiempo,
    MAX(tipo_cambio_bna_vendedor)
FROM
    cotizaciones
GROUP BY 
    CAST(strftime('%m', indice_tiempo) AS INTEGER)
ORDER BY 
    CAST(strftime('%m', indice_tiempo) AS INTEGER)
;
